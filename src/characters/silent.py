from abc import ABC, abstractmethod
import random
from src.game.player import Player  # Імпорт класу Player

class Silent(ABC):
    @abstractmethod
    def do_action(self):
        pass

# Додає + 1 життя.
class Nurse(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

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
        self.player = player  # Зберігаємо екземпляр Player

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
        self.player = player  # Зберігаємо екземпляр Player
        self.speech = self.load_speech('assets/texts/traveller_speech.txt')

    def do_action(self):
        self.give_hint()
        pass

    def load_speech(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return ""

    def give_hint(self):
        print(self.speech)

# Забирає 1 життя.
class Witch(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

    def do_action(self):
        self.rem_life()
        pass

    def rem_life(self):
        if self.player.lives >= 1:
            self.player.lives -= 1  # Забирає життя, якщо їх кількість більше = 1
            print("A witch has enchanted you!")
        else:
            print("Game over")

# Питає, чи хочеш дізн. про іст. смерті,
# якщо ні - забирає життя / предмет персонажа (дає вибір),
# так - розповідь і пропуск ходу.
class Undead(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player
        self.name = "Undead"
        self.speech = self.load_speech('assets/texts/undead_speech.txt')

    @staticmethod
    def ask_question():
        question = "Do you want to know how I died? (yes/no)"
        return input(question).strip().lower() == 'yes'

    def tell_story(self):
        print(self.speech)

    def load_speech(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return ""

    def process_answer(self, answer):
        if answer:
            self.tell_story()
        else:
            choice = input("Lose a life or an item? (life/item): ").strip().lower()
            if choice == 'life':
                self.rem_life()
            else:
                self.player.del_item(random.randint(0, len(self.player.items) - 1))
                print("You lost an item instead of a life.")
    
    def rem_life(self):
        if self.player.lives >= 1:
            self.player.lives -= 1  # Забирає життя, якщо більше = 
            print("You have lost 1 life")
        else:
            print("Game over")

    def do_action(self):
        print("I am Undead")
        answer = self.ask_question()
        self.process_answer(answer)
