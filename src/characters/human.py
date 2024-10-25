from abc import abstractmethod
import random
from random import randint
from src.game.player import Player  # Імпорт класу Player
from ..characters.character import Character
from constants import *
from utils import *

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
        print(load_speech(self, MAN_SPEECH_PATH))

    def do_action(self):
        self.introduce()
        if self.guess_character() == 'h': 
            print(MAN_GUESSED)
        else:
            print("Guessed wrongly!")
            # реалізувати логіку додавання 2 нових персонажів на шляху (шлях стає довшим)
        

# Gives a hint in exchange for an item, otherwise lies.
class Peasant(Human):
    def __init__(self, player):
        super().__init__(player)
        self.hint_given = False #а нащо нам ця змінна?

    def introduce(self):
        print(load_speech(self, PEASANT_SPEECH_PATH))

    def do_action(self):
        self.introduce()
        if self.guess_character() == 'h': 
            print(PEASANT_INTRO)
            self.guessed_correctly()
        else:
            print("Guessed wrongly!")
            # реалізувати логіку додавання 2 нових персонажів на шляху (шлях стає довшим)
    
    def guessed_correctly(self):
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
        # Check if the player has any items to trade
        if not self.player.items or all(item is None for item in self.player.items):
            print(PEASANT_NO_ITEMS_FOR_TRADE)
            return

        print("Select an item to trade for a hint:")
        for idx, item in enumerate(self.player.items):
            if item is None:
                print(f"Slot {idx + 1}: Empty")
            else:
                print(f"Slot {idx + 1}: {item}")

        trade_index = int(input("Enter the number of the item you want to trade: ")) - 1

        # Check if the trade index is valid
        if 0 <= trade_index < len(self.player.items) and self.player.items[trade_index] is not None:
            traded_item = self.player.items[trade_index]
            self.player.items[trade_index] = None  # Remove the chosen item from player inventory.
            print(PEASANT_TRADE_THANKS.format(traded_item))

            # Randomly decide whether to give the player a hint about people or spirits.
            human_or_spirit = random.randint(0, 1)

            if human_or_spirit == 1:
                remaining_spirits = self.player.remaining_spirits
                print(PEASANT_REMAINING_SPIRITS.format(remaining_spirits))
            else:
                remaining_people = self.player.remaining_people
                print(PEASANT_REMAINING_PEOPLE.format(remaining_people))
        else:
            print("Invalid trade option.")


# Sells items like wormwood from spirits or bartka (an axe) from a bandit, which can be traded later.
class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        print(MERCHANT_INTRO)

    def do_action(self):
        self.introduce()
        item_mapping = self.get_item_mapping()
        
        visit_shop = input(SHOP_CHOICE).strip().lower()
        if visit_shop == VISIT_SHOP_YES:
            while self.player.coins > 7:
                action = input("\nWould you like to 'buy' or 'trade'? ").strip().lower()

                if action not in ['buy', 'trade']:
                    print("Invalid option. Please choose 'buy' or 'trade'.")
                    continue
                
                if action == 'buy':
                    self.handle_purchase(item_mapping)

                elif action == 'trade':
                    self.handle_trade(item_mapping)
        else:
            print(VISIT_SHOP_NO)

    def get_item_mapping(self):
        return {
            BUY_VARENUCHA: ("VARENUCHA", VARENUCHA),
            BUY_WORMWOOD: ("WORMWOOD", WORMWOOD),
            BUY_BARTKA: ("BARTKA", BARTKA),
        }

    def handle_purchase(self, item_mapping):
        print(DISPLAY)
        answer_buy = input(GOODS).strip().lower()

        if answer_buy in item_mapping:
            item_name, item_cost = item_mapping[answer_buy]
            index = int(answer_buy) - 1  # Use the input as the index directly

            if self.player.items[index] is None:
                if self.player.coins >= item_cost:
                    self.player.items[index] = item_name
                    self.player.coins -= item_cost
                    print(MERCHANT_PURCHASE_THANKS)
                else:
                    print(MERCHANT_NOT_ENOUGH_COINS)
                    self.handle_trade(item_mapping)
            else:
                print("You already have this item in your inventory!")
        else:
            print(MERCHANT_NO_PURCHASE)

    def handle_trade(self, item_mapping):
        print(MERCHANT_TRADE)
        trade_ans = input(MERCHANT_TRADE_OPTION).strip().lower()

        if trade_ans == MARCHANT_TRADE_YES:
            print(TRADES)
            print("Select an item from your inventory to trade:")
            for idx, item in enumerate(self.player.items):
                if item is None:
                    print(f"Slot {idx + 1}: Empty")
                else:
                    print(f"Slot {idx + 1}: {item}")

            trade_index = int(input("Enter the number of the item you want to trade: ")) - 1

            if 0 <= trade_index < len(self.player.items) and self.player.items[trade_index] is not None:
                traded_item = self.player.items[trade_index]
                self.player.items[trade_index] = None
                print("Select the new item you want to receive:")
                for idx, (item_name, _) in enumerate(item_mapping.values()):
                    print(f"{idx + 1}: {item_name}")

                new_item_choice = int(input("Enter the number of the new item: ")) - 1

                # Check if the new_item_choice is valid
                if new_item_choice < 0 or new_item_choice >= len(item_mapping):
                    print("Invalid item selection.")
                    return

                # Get the actual item name for the new choice
                new_item_name = item_mapping[list(item_mapping.keys())[new_item_choice]][0]

                # Check if the player already has the new item
                if new_item_name in self.player.items:
                    print(f"You already have {new_item_name} in your inventory!")
                else:
                    # Add new item to inventory
                    self.player.items[new_item_choice] = new_item_name
                    print(f"You traded {traded_item} for {new_item_name}!")
            else:
                print("Invalid trade option.")
        else:
            print(MERCHANT_TRADE_NOT_OCCURED)


# Gives the player a chance to pay off, otherwise... :(
class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        print(BANDIT_INTRO)

    def do_action(self):
        self.introduce()

        # Check if the player has at least 2 non-None items to pay
        actual_item_count = sum(1 for item in self.player.items if item is not None)

        if actual_item_count < ITEMS_PAY_AMOUNT and self.player.coins < COINS_PAY_AMOUNT:
            print("Not enough items or coins!")
            self.kill_player()
            return
        
        answer = input(BANDIT_PAY_PROMPT).strip().lower()

        if answer == PAY_YES:
            pay_answer = input(BANDIT_PAY_WITH_PROMPT).strip().lower()
            
            if pay_answer == 'items':
                self.pay_bandit_with_items(actual_item_count)
            elif pay_answer == 'coins':
                self.pay_bandit_with_coins()
            else:
                print("Invalid option.")
                self.kill_player()
        else:
            self.kill_player()

    def pay_bandit_with_items(self, actual_item_count):
        if actual_item_count < ITEMS_PAY_AMOUNT:
            print("Not enough items to pay the Bandit!")
            self.kill_player()
            return

        items_removed = 0
        for i in range(len(self.player.items)):
            if self.player.items[i] is not None:
                pay_item = self.player.items[i]
                self.player.items[i] = None
                print(f"You gave {pay_item} to the Bandit.")
                items_removed += 1
                if items_removed >= ITEMS_PAY_AMOUNT:
                    break
        print(BANDIT_PAY_THANKS)

    def pay_bandit_with_coins(self):
        if self.player.coins < COINS_PAY_AMOUNT:
            print("Not enough coins to pay the Bandit!")
            self.kill_player()
            return

        self.player.coins -= COINS_PAY_AMOUNT
        print(f"You paid the Bandit {COINS_PAY_AMOUNT} coins.")
        print(BANDIT_PAY_THANKS)

    def kill_player(self):
        rem_life(self)
        print(BANDIT_KILL_MESSAGE)
