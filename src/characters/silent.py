from abc import ABC, abstractmethod
import random

from src.game.player import Player  # Import the Player class
from src.constants import TRAVELER_SPEECH_PATH, UNDEAD_SPEECH_PATH, UNDEAD_MOURN
from src.utils import load_speech, rem_life

class Silent(ABC):
    @abstractmethod
    def do_action(self):
        pass

    # def __init__(self, player: Player):
    #     self.player = player  # Store an instance of Player



class Nurse(Silent):
    """Adds +1 life."""
    def __init__(self, pl: Player):
        # super().__init__(player)
        self.player = pl

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
    def __init__(self, pl: Player):
        self.player = pl
        #super().__init__(player)

    def do_action(self):
        self.steal_item()
        pass

    def steal_item(self):
        # Check if the player has protection from humans (assume it's represented by the Bartka item)
        if self.player.items.get("Bartka", 0) > 0:
            print("The Robber decided not to steal because you have protection.")
            return

        # Check if there are any items to steal
        available_items = [item for item, count in self.player.items.items() if count > 0]
        if available_items:
            # Select a random item to steal
            stolen_item = random.choice(available_items)
            self.player.items[stolen_item] -= 1  # Decrease the item count
            print(f"The Robber stole one {stolen_item}.")
        else:
            print("The Robber found nothing to steal.")


class Traveler(Silent):
    """Gives a hint about future characters (can make a counter for spirits and humans)."""
    def __init__(self, pl: Player):
        # super().__init__(pl)
        self.player = pl
        self.speech = load_speech(self, TRAVELER_SPEECH_PATH)

    def do_action(self):
        self.give_hint()
        pass

    def give_hint(self):
        print(self.speech)


# Takes away 1 life.
class Witch(Silent):
    def __init__(self, pl: Player):
        self.player = pl
        #super().__init__(player)

    def do_action(self):
        rem_life(self.player)
        pass


class Undead(Silent):
    """Asks if you want to learn about the cause of death,
    if no - takes a life or an item (offers choice),
    if yes - tells a story and skips a turn."""
    
    def __init__(self, pl: Player, already_met: str, rejection_flag: str):
        # super().__init__(player)
        self.player = pl
        self.name = "Undead"
        self.speech = load_speech(self, UNDEAD_SPEECH_PATH)
        self.already_met = already_met  # "yes" or "no" indicating whether the Undead has been met
        self.rejection_flag = rejection_flag  # "yes" or "no" indicating whether the player rejected the story

    @staticmethod
    def ask_question():
        question = "Do you want to know how I died? (yes/no): "
        return input(question).strip().lower() 

    def tell_story(self):
        print(self.speech)

    def meet_consequences(self, answer):
        if answer:
            self.tell_story()
        else:
            if self.rejection_flag == "no":
                print("You listened to the Undead's story, and they reward you with 5 coins.")
                self.player.coins += 5  # Add coins to the player's inventory
            else:
                print("You rejected the Undead's story earlier, and now they revenge you.")
                if self.player.items:  # Check if the player has items
                    while True:
                        choice = input("Lose a life or an item? (life/item): ").strip().lower()
                        if choice == 'life':
                            rem_life(self.player)
                            break
                        elif choice == 'item':
                            item_index = random.randint(0, len(self.player.items) - 1)
                            self.player.del_item(item_index)
                            print("You lost an item instead of a life.")
                            break
                        else:
                            print("Invalid choice. Please enter 'life' or 'item'.")
                else:
                    print("You have no items to lose. Losing a life instead.")
                    rem_life(self.player)

    def do_action(self):
        """Introduces the Undead and asks the player if they accept the story."""
        print("I am Undead")

        if self.already_met == "yes":
            # If the Undead has been met before, process consequences based on rejection_flag
            self.meet_consequences(self.rejection_flag)
        else:
            # First encounter with Undead: ask the player if they want to hear the story
            answer = self.ask_question()

            if answer == "no":
                print(UNDEAD_MOURN)
                return "yes"  # Player rejected, return "yes"
            else:
                self.tell_story()
                return "no"  # Player accepted, return "no"
