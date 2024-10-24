from abc import ABC, abstractmethod
import random
from src.game.player import Player  # Імпорт класу Player
from constants import TRAVELER_SPEECH_PATH, UNDEAD_SPEECH_PATH
from utils import load_speech, rem_life

class Silent(ABC):
    @abstractmethod
    def do_action(self):
        pass

    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

# Додає + 1 життя.
class Nurse(Silent):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.add_life()

    def add_life(self):
        if self.player.lives < 3:
            self.player.lives += 1  # Додаємо життя, якщо їх менше 3
            print("You have been healed!")
        else:
            print("You don`t need more lives")

# Персонаж-шкідник, краде мовчки.
class Robber(Silent):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.steal_item()
        pass

    def steal_item(self):
        if self.player.items[2]: # якщо в нас є захист від людей, не краде
            print("A robber has been defeated!")
            self.player.del_item(2)
        else:
            random_index = random.randint(0, 1) # краде річ для обміну чи захист від духів
            stolen_item = self.player.del_item(random_index)
            print(f"A robber has stolen {stolen_item} from your equipment")

# Дає підказку про майбутніх персонажів (можна зробити лічильник на духів і людей).
class Traveler(Silent):
    def __init__(self, player: Player):
        super().__init__(player)
        self.speech = load_speech(self, TRAVELER_SPEECH_PATH)

    def do_action(self):
        self.give_hint()
        pass

    def give_hint(self):
        print(self.speech)

# Забирає 1 життя.
class Witch(Silent):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        rem_life(self)
        pass

# Питає, чи хочеш дізн. про іст. смерті,
# якщо ні - забирає життя / предмет персонажа (дає вибір),
# так - розповідь і пропуск ходу.
class Undead(Silent):
    def __init__(self, player: Player):
        super().__init__(player)
        self.name = "Undead"
        self.speech = load_speech(self, UNDEAD_SPEECH_PATH)

    @staticmethod
    def ask_question():
        question = "Do you want to know how I died? (yes/no)"
        return input(question).strip().lower() == 'yes'

    def tell_story(self):
        print(self.speech)

    def process_answer(self, answer):
        if answer:
            self.tell_story()
        else:
            if self.player.items: 
                choice = input("Lose a life or an item? (life/item): ").strip().lower()
                if choice == 'life' :
                    rem_life(self)
                else:
                    self.player.del_item(random.randint(0, len(self.player.items) - 1))
                    print("You lost an item instead of a life.")
            else:
                rem_life(self)

    def do_action(self):
        print("I am Undead")
        answer = self.ask_question()
        self.process_answer(answer)
