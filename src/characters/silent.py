from abc import ABC, abstractmethod
import random
from src.game.player import Player  # Import the Player class
from constants import TRAVELER_SPEECH_PATH, UNDEAD_SPEECH_PATH
from utils import load_speech, rem_life

class Silent(ABC):
    @abstractmethod
    def do_action(self):
        pass

    def __init__(self, player: Player):
        self.player = player  # Store an instance of Player



class Nurse(Silent):
    """Adds +1 life."""
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.add_life()

    def add_life(self):
        if self.player.lives < 3:
            self.player.lives += 1  # Add a life if there are fewer than 3
            print("You have been healed!")
        else:
            print("You don`t need more lives")



class Robber(Silent):
    """Harmful character, steals silently."""
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.steal_item()
        pass

    def steal_item(self):
        if self.player.items[2]:  # if there’s protection from humans, does not steal
            print("A robber has been defeated!")
            self.player.del_item(2)
        else:
            random_index = random.randint(0, 1)  # steals an item for trade or protection from spirits
            stolen_item = self.player.del_item(random_index)
            print(f"A robber has stolen {stolen_item} from your equipment")



class Traveler(Silent):
    """Gives a hint about future characters (can make a counter for spirits and humans)."""
    def __init__(self, player: Player):
        super().__init__(player)
        self.speech = load_speech(self, TRAVELER_SPEECH_PATH)

    def do_action(self):
        self.give_hint()
        pass

    def give_hint(self):
        print(self.speech)


# Takes away 1 life.
class Witch(Silent):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        rem_life(self.player)
        pass


class Undead(Silent):
    """Asks if you want to learn about the cause of death,
    if no - takes a life or an item (offers choice),
    if yes - tells a story and skips a turn."""
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
                if choice == 'life':
                    rem_life(self.player)
                else:
                    self.player.del_item(random.randint(0, len(self.player.items) - 1))
                    print("You lost an item instead of a life.")
            else:
                rem_life(self.player)

    def do_action(self):
        print("I am Undead")
        answer = self.ask_question()
        self.process_answer(answer)
