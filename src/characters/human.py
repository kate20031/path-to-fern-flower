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


# Simply asks a question.
class Man(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print(MAN_ACTION)

# Gives a hint in exchange for an item, otherwise lies.
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

# Sells items like milk from spirits or from a bandit, which can be traded later.
class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print(MERCHANT_ACTION)

# Gives the player a chance to pay off, otherwise... :(
class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        print(BANDIT_ACTION)

    def do_action(self):
        print(BANDIT_ACTION)

        # Check if the player has enough items to pay
        if len(self.player.items) >= PAY_AMOUNT:
            answer = input(BANDIT_PAY_PROMPT).strip().lower()
            if answer == 'yes':
                self.pay_bandit()
            else:
                self.kill_player()
        else:
            print(BANDIT_KILL_MESSAGE)
            self.kill_player()

    def pay_bandit(self):
        # Remove required number of items from player's inventory
        for _ in range(PAY_AMOUNT):
            self.player.items.pop(0)
        print(BANDIT_PAY_THANKS)

    def kill_player(self):
        self.player.is_alive = False
        print(BANDIT_KILL_MESSAGE)
