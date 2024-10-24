from abc import abstractmethod

from sqlalchemy.sql.functions import random

from ..characters.character import Character

class Human(Character):
   @abstractmethod
   def do_action(self):
      pass

   def guess_character(self):
        return input("Is it a human or a spirit? (h/s): ").strip().lower()

# Просто ставить питання.
class Man(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Man")

# Дає підказку за товар, інакше - бреше.
class Peasant(Human):
    def __init__(self, player):
        super().__init__(player)
        self.hint_given = False

    def introduce(self):
        print("Good evening. I'm just a poor peasant, trying to survive in this wilderness.")

    def do_action(self):

        print("I am Peasant. Do you have anything to trade?")

        # Check if player has more than 1 item
        if len(self.player.items) > 1:
            answer = input("You have several items. Do you want to trade one for a hint? (yes/no): ").strip().lower()
            if answer == 'yes':
                self.trade_for_hint()
            else:
                print("Without a trade, I cannot help you. Perhaps you should head west.")
        else:
            print("You have nothing to trade! Maybe next time.")

    def trade_for_hint(self):
        if self.player.items:
            traded_item = self.player.items.pop(0)  # Remove one item from player inventory
            print(f"Thank you for the {traded_item}! Here's your hint: 'The spirits are always truthful.'")
            human_or_spirit = random(0, 1)

            if human_or_spirit == 1:
                remaining_spirits = self.player.remaining_spirits
                print(f"There are {remaining_spirits} spirits you have yet to meet.")
            else:
                remaining_people = self.player.remaining_people
                print(f"There are {remaining_people} people you have yet to meet.")
        else:
            print("You don't have enough items to trade.")

# Продає товар молоко, від духів, від бандита який потім можна виміняти.
class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Merchant")

# Дає шанс відкупитись, інакше - :(
class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Bandit")
