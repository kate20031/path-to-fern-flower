import unittest
from unittest.mock import patch, mock_open

from src.characters.human import Merchant, Peasant
from src.characters.spirit import Mavka
from src.game.player import Player
from path_to_fern_flower.utils import load_speech, rem_life, create_new_character

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.player = Player("TestPlayer")

    @patch('builtins.open', new_callable=mock_open, read_data="Hello, world!")
    def test_load_speech_success(self, mock_file):
        # Tests if the load_speech function correctly reads from a file
        file_path = 'path/to/speech.txt'
        speech = load_speech(self, file_path)
        self.assertEqual(speech, "Hello, world!")
        mock_file.assert_called_with(file_path, 'r')

    def test_rem_life_success(self):
        # Tests if the rem_life function successfully decreases the player's lives
        initial_lives = self.player.lives
        rem_life(self.player)
        self.assertEqual(self.player.lives, initial_lives - 1)
        self.assertNotEqual(self.player.lives, 0)

    @patch('builtins.print')
    def test_rem_life_game_over(self, mock_print):
        # Tests if the rem_life function handles the case where the player has only 1 life left and it becomes 0
        self.player.lives = 1
        rem_life(self.player)
        self.assertEqual(self.player.lives, 0)
        mock_print.assert_called_with("You have lost 1 life")

    @patch('random.choice')
    def test_create_new_character(self, mock_random_choice):
        # Tests if the create_new_character function correctly creates a Merchant character
        mock_random_choice.return_value = Merchant
        character = create_new_character(self)
        self.assertIsInstance(character, Merchant)

    @patch('random.choice')
    def test_create_new_character_multiple_classes(self, mock_random_choice):
        # Tests if the create_new_character function can create different types of characters (Peasant, Mavka)
        mock_random_choice.return_value = Peasant
        character = create_new_character(self)
        self.assertIsInstance(character, Peasant)

        mock_random_choice.return_value = Mavka
        character = create_new_character(self)
        self.assertIsInstance(character, Mavka)

if __name__ == '__main__':
    unittest.main()

