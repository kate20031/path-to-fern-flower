import random
from src.characters.human import Merchant, Peasant, Man, Bandit
from src.characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
from src.characters.silent import Nurse, Robber, Traveler, Witch, Undead

def load_speech(self, file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""

def rem_life(player):
    if player.lives >= 1:
        player.lives -= 1  # Забирає життя, якщо більше =
        print("You have lost 1 life")
    else:
        print("Game over")


def create_new_character(self) -> None:
    character_classes = [Man, Peasant, Merchant, Bandit, Mavka, Perelisnyk, ForestGuardian, Demon,Witch, Undead, Nurse, Robber, Traveler]
    new_character = random.choice(character_classes)(self.player)
    return new_character