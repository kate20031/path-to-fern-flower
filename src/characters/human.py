from abc import abstractmethod
from sqlalchemy.sql.functions import random
from ..characters.character import Character
from constants import *

# Constants for types
HUMAN_TYPE = 'h'
SPIRIT_TYPE = 's'

class Human(Character):
    @abstractmethod
    def do_action(self):
        pass

    def guess_character(self):
        return input(f"Is it a human or a spirit? ({HUMAN_TYPE}/{SPIRIT_TYPE}): ").strip().lower()

class Man(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print(MAN_ACTION)

class Peasant(Human):
    def __init__(self, player):
        super().__init__(player)
        self.hint_given = False

    def introduce(self):
        print(PEASANT_INTRO)

    def do_action(self):
        print(PEASANT_ACTION)
        print(PEASANT_TRADE_PROMPT)

        # Check if player has more than 1 item.
        if len(self.player.items) > HINT_THRESHOLD:
            answer = input(PEASANT_MULTI_ITEM_PROMPT).strip().lower()
            if answer == TRADE_YES:
                self.trade_for_hint()
            else:
                print(PEASANT_NO_TRADE)
        else:
            print(PEASANT_NO_ITEMS)

    def trade_for_hint(self):
        if self.player.items:
            traded_item = self.player.items.pop(0)  # Remove one item from player inventory.
            print(PEASANT_TRADE_THANKS.format(traded_item))

            # Randomly decide whether to give player hint about people or a spirits.
            human_or_spirit = random(0, 1)

            if human_or_spirit == 1:
                remaining_spirits = self.player.remaining_spirits
                print(PEASANT_REMAINING_SPIRITS.format(remaining_spirits))
            else:
                remaining_people = self.player.remaining_people
                print(PEASANT_REMAINING_PEOPLE.format(remaining_people))
        else:
            print(PEASANT_NO_ITEMS_FOR_TRADE)

class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print(MERCHANT_ACTION)

class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print(BANDIT_ACTION)
