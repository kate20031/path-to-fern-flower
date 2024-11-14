import unittest
from unittest.mock import patch, MagicMock, mock_open

from src.characters.silent import Nurse, Witch
from src.game.player import Player
from src.characters.spirit import Mavka, Demon
from src.characters.human import Merchant, Bandit
from constants import *

class TestSpiritCharacters(unittest.TestCase):

    def setUp(self):
        self.player = Player("player")
        self.player.coins = 15
        self.player._items = dict(Varenucha=0, Wormwood=0, Bartka=0)

    @patch('src.characters.spirit.input', return_value='h')
    @patch('builtins.open', new_callable=mock_open, read_data='Mocked text data')
    def test_mavka_do_action_wrong_guess(self, mock_input, mock_file):
        """Test that Mavka reduces the player's lives by 1 when the player guesses incorrectly."""
        mavka = Mavka(self.player)
        initial_lives = self.player.lives
        mavka.do_action()
        self.assertEqual(self.player.lives, initial_lives - 1)

    @patch('builtins.open', unittest.mock.mock_open(read_data="Mocked text data"))
    @patch('src.characters.spirit.input', return_value='s')
    def test_demon_steals_coins_on_wrong_guess(self, mock_input):
        """Test that the Demon does not steal coins when the player makes a wrong guess."""
        demon = Demon(self.player)
        demon.do_action()
        self.assertEqual(self.player.coins, 15)

    @patch('builtins.open', unittest.mock.mock_open(read_data="Mocked text data"))
    @patch('src.characters.spirit.input', side_effect=['h', 'yes'])
    def test_demon_steals_item_if_no_coins(self, mock_input):
        """Test that the Demon steals an item if the player has no coins and the 'Varenucha' item is available."""
        self.player.coins = 0
        self.player._items = {'Varenucha': 1, 'Wormwood': 0, 'Bartka': 0}
        initial_lives = self.player.lives
        demon = Demon(self.player)
        demon.do_action()
        self.assertEqual(0, self.player.items['Varenucha'])
        self.assertEqual(initial_lives, self.player.lives)

    @patch('builtins.open', unittest.mock.mock_open(read_data="Mocked text data"))
    @patch('src.characters.spirit.input', return_value='no')
    def test_demon_removes_life_if_no_items(self, mock_input):
        """Test that the Demon removes a life if the player has no items to steal."""
        self.player.coins = 0
        self.player._items = {'Varenucha': 0, 'Wormwood': 0, 'Bartka': 0}
        initial_lives = self.player.lives
        demon = Demon(self.player)
        demon.do_action()
        self.assertEqual(self.player.lives, initial_lives - 1)

    @patch('builtins.input', side_effect=['yes', 'buy', '1'])  # Simulate player choosing 'yes' to visit the shop and selecting item 1 (Varenucha)
    def test_merchant_trade(self, mock_input):
        """Test the Merchant's trade, where the player buys an item (Varenucha) from the Merchant."""
        merchant = Merchant(self.player)
        initial_varenucha_count = self.player.items.get('Varenucha', 0)

        with patch('src.characters.human.load_speech', return_value="Hello, I am a Merchant.") as mock_speech:
            merchant.do_action()

            self.assertIn('Varenucha', self.player.items)
            self.assertEqual(self.player.items.get('Varenucha', 0), initial_varenucha_count + 1)  # Check that the count of 'Varenucha' increased by 1

            mock_input.assert_any_call(SHOP_CHOICE)
            mock_input.assert_any_call(GOODS)

    @patch('builtins.input', side_effect=['yes', 'items'])
    def test_bandit_pay_with_items(self, mock_input):
        """Test the Bandit class, where player chooses to pay with items (Varenucha)."""
        self.player._items = {'Varenucha': 1, 'Wormwood': 0, 'Bartka': 0}
        bandit = Bandit(self.player)
        with patch('src.characters.human.load_speech', return_value="Hello, I am a Bandit.") as mock_speech:
            # Record the initial number of items
            initial_item_count = sum(1 for item in self.player.items.values() if item > 0)
            initial_varenucha_count = self.player.items['Varenucha']
            bandit.do_action()
            final_varenucha_count = self.player.items['Varenucha']
            self.assertEqual(initial_item_count - 1, sum(1 for item in self.player.items.values() if item > 0))
            self.assertEqual(initial_varenucha_count - 1, final_varenucha_count)

    @patch('builtins.input', side_effect=['s', 'no'])
    def test_bandit_no_pay(self, mock_input):
        """Test that the Bandit does not take items if the player refuses to pay."""
        self.player._items = {'Varenucha': 1, 'Wormwood': 0, 'Bartka': 0}
        bandit = Bandit(self.player)
        with patch('src.characters.human.load_speech', return_value="Hello, I am a Bandit.") as mock_speech:
            bandit.do_action()
            self.assertEqual(2, self.player.lives)

    @patch('builtins.print')
    def test_nurse_add_life(self, mock_print):
        """Test that the Nurse increases the player's lives by 1 and prints a healing message."""
        self.player.lives = 2
        nurse = Nurse(self.player)
        nurse.add_life()
        self.assertEqual(self.player.lives, 3)
        mock_print.assert_called_with("You have been healed!")

    @patch('builtins.print')
    def test_nurse_no_more_life(self, mock_print):
        """Test that the Nurse does not increase lives if the player is at maximum lives and prints a message."""
        self.player.lives = 3  # Set lives to max
        nurse = Nurse(self.player)
        nurse.add_life()
        self.assertEqual(self.player.lives, 3)
        mock_print.assert_called_with("You don`t need more lives")

    @patch('src.characters.silent.rem_life')
    def test_witch_rem_life(self, mock_rem_life):
        """Test that the Witch calls the rem_life function to remove a life from the player."""
        witch = Witch(self.player)
        witch.do_action()
        mock_rem_life.assert_called_with(self.player)

if __name__ == "__main__":
    unittest.main()

