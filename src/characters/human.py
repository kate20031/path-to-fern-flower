from abc import abstractmethod

from src.game.player import Player  # Імпорт класу Player
from src.characters.character import Character
from src.constants import *
from src.utils import *

# Constants for types
HUMAN_TYPE = 'h'
SPIRIT_TYPE = 's'



class Human(Character):
    @abstractmethod
    def do_action(self):
        pass

    def guess_character(self) -> str:
        return input(f"Is it a human or a spirit? ({HUMAN_TYPE}/{SPIRIT_TYPE}): ").strip().lower()

    def display_inventory(self) -> None:
        for idx, item in enumerate(self.player.items):
            print(f"Slot {idx + 1}: {item if item else 'Empty'}")

    def select_item(self) -> int:
        """Prompts the player to select an item index for trading or paying."""
        while True:
            try:
                self.display_inventory()
                choice = int(input("Enter the number of the item: ")) - 1  # Convert to zero-based index

                # Check if choice is valid
                if 0 <= choice < len(self.player.items):
                    if self.player.items[choice] is not None and self.player.items[choice] > 0:
                        return choice
                    else:
                        print("You cannot trade this item because you have none.")
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")
            except IndexError:  # Handle any unexpected IndexErrors
                print("Invalid choice. Try again.")


class Man(Human):
    """Asks a question, if players makes a mistake ->
    adds 2 new characters a player will meet with later."""
    def __init__(self, player: Player):
        #super().__init__(player)
        self.player = player

    def introduce(self) -> None:
        print(load_speech(self, MAN_SPEECH_PATH))

    def do_action(self) -> None:
        self.introduce()
        if self.guess_character() == HUMAN_TYPE:
            print(MAN_GUESSED)
        else:
            print("Guessed wrongly!")
            character1 = create_new_character(self)
            character2 = create_new_character(self)
            self.player.add_new_character(character1)
            self.player.add_new_character(character2)

class Peasant(Human):
    """Gives a hint in exchange for an item, otherwise lies."""
    def __init__(self, player: Player):
        #super().__init__(player)
        self.player = player

    def introduce(self) -> None:
        print(load_speech(self, PEASANT_SPEECH_PATH))

    def do_action(self) -> None:
        self.introduce()
        if self.guess_character() == HUMAN_TYPE:
            print(PEASANT_INTRO)
            self.handle_trade_offer()
        else:
            print("Guessed wrongly!")
            # Add logic to add 2 new characters in path

    def handle_trade_offer(self) -> None:
        print(PEASANT_TRADE_PROMPT)
        if len(self.player.items) > HINT_THRESHOLD:
            answer = input(PEASANT_MULTI_ITEM_PROMPT).strip().lower()
            if answer == TRADE_YES:
                self.trade_for_hint()
            else:
                print(PEASANT_NO_TRADE)
        else:
            print(PEASANT_NO_ITEMS)

    def trade_for_hint(self) -> None:
        """Handles trading an item for a hint."""
        if not any(self.player.items):
            print(PEASANT_NO_ITEMS_FOR_TRADE)
            return

        trade_index = self.select_item()
        traded_item = self.player.items[trade_index]
        self.player.items[trade_index] = None
        print(PEASANT_TRADE_THANKS.format(traded_item))

        hint_type = random.choice(["spirits", "people"])
        hint = self.player.remaining_spirits if hint_type == "spirits" else self.player.remaining_people
        print(f"Remaining {hint_type}: {hint}")



class Merchant(Human):
    """Sells items like wormwood from spirits or bartka (an axe) from a bandit, which can be traded later."""
    def __init__(self, player: Player):
        self.player = player
        #super().__init__(player)

    def introduce(self) -> None:
        print(MERCHANT_INTRO)

    def do_action(self) -> None:
        """
        Handles the merchant's interaction with the player, allowing them to buy or trade items.
        """
        self.introduce()

        if input(SHOP_CHOICE).strip().lower() == VISIT_SHOP_YES:
            item_mapping = self.get_item_mapping()
            while self.player.coins > MIN_COINS_FOR_SHOP:
                print("\nWhat would you like to do?")
                print("1. Buy items")
                print("2. Trade items")
                print("3. Leave the shop")
                action = input("Enter your choice (1/2/3): ").strip()

                if action == '1':  # Buy
                    self.handle_purchase(item_mapping)
                elif action == '2':  # Trade
                    self.handle_trade(item_mapping)
                elif action == '3':  # Leave shop
                    print("You decide to leave the shop. Come back anytime!")
                    break
                else:  # Invalid input
                    print("Invalid option. Please choose 1, 2, or 3.")
        else:
            print(VISIT_SHOP_NO)

    def get_item_mapping(self) -> dict:
        return {
            BUY_VARENUCHA: ("VARENUCHA", VARENUCHA),
            BUY_WORMWOOD: ("WORMWOOD", WORMWOOD),
            BUY_BARTKA: ("BARTKA", BARTKA),
        }

    def handle_purchase(self, item_mapping: dict) -> None:
        print(DISPLAY)
        item_choice = input(GOODS).strip().lower()

        if item_choice in item_mapping:
            item_name, item_cost = item_mapping[item_choice]
            index = int(item_choice) - 1
            if self.player.coins >= item_cost and self.player.items[index] is None:
                self.player.items[index] = item_name
                self.player.coins -= item_cost
                print(MERCHANT_PURCHASE_THANKS)
            else:
                print(MERCHANT_NOT_ENOUGH_COINS if self.player.coins < item_cost else "You already have this item!")
        else:
            print(MERCHANT_NO_PURCHASE)

    def handle_trade(self, item_mapping: dict) -> None:
        """
        Handles the trade of items between the player and the merchant.
        :param item_mapping: A dictionary mapping item options to their names and costs.
        """
        print(MERCHANT_TRADE)
        if input(MERCHANT_TRADE_OPTION).strip().lower() == MARCHANT_TRADE_YES:
            trade_item = input("Enter the name of the item you want to trade: ").strip()

            if trade_item in self.player.items and self.player.items[trade_item] > 0:
                self.player.items[trade_item] -= 1  # Remove one count of the traded item
                print(f"You traded {trade_item}. Choose your new item:")

                for idx, (item_key, (item_name, _)) in enumerate(item_mapping.items(), start=1):
                    print(f"{idx}: {item_name}")

                new_item_choice = input("Enter the number of the new item: ").strip()
                if new_item_choice in item_mapping:
                    new_item_name, _ = item_mapping[new_item_choice]
                    self.player.items[new_item_name] += 1  # Add the new item to the inventory
                    print(f"You traded {trade_item} for {new_item_name}!")
                else:
                    print("Invalid choice. Trade cancelled.")
            else:
                print(f"You don't have {trade_item} in your inventory.")
        else:
            print(MERCHANT_TRADE_NOT_OCCURED)


class Bandit(Human):
    """Gives the player a chance to pay off, otherwise... :("""
    def __init__(self, player: Player):
        self.player = player
        #super().__init__(player)

    def introduce(self) -> None:
        print(BANDIT_INTRO)

    def do_action(self) -> None:
        self.introduce()

        actual_item_count = sum(1 for item in self.player.items if item is not None)
        if actual_item_count < ITEMS_PAY_AMOUNT and self.player.coins < COINS_PAY_AMOUNT:
            print("Not enough items or coins!")
            rem_life(self.player)
            return

        if input(BANDIT_PAY_PROMPT).strip().lower() == PAY_YES:
            if input(BANDIT_PAY_WITH_PROMPT).strip().lower() == 'items':
                self.pay_with_items()
            else:
                self.pay_with_coins()
        else:
            rem_life(self.player)

    def pay_with_items(self) -> None:
        """Pays the bandit using items if the player has enough."""
        items_to_pay = ITEMS_PAY_AMOUNT
        for i, item in enumerate(self.player.items):
            if item and items_to_pay > 0:
                print(f"You gave {item} to the Bandit.")
                self.player.items[i] = None
                items_to_pay -= 1
        print(BANDIT_PAY_THANKS)

    def pay_with_coins(self) -> None:
        """Pays the bandit using coins if the player has enough."""
        if self.player.coins < COINS_PAY_AMOUNT:
            print("Not enough coins to pay the Bandit!")
            rem_life(self.player)
        else:
            self.player.coins -= COINS_PAY_AMOUNT
            print(f"You paid the Bandit {COINS_PAY_AMOUNT} coins.")
            print(BANDIT_PAY_THANKS)
