import random

def load_speech(self, file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""

def rem_life(player):
    if player.lives >= 1:
        player.lives -= 1
        print("You have lost 1 life")
    else:
        print("Game over")

def create_new_character(self) -> None:
    from src.characters.human import Merchant, Peasant, Man, Bandit
    from src.characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
    from src.characters.silent import Nurse, Robber, Traveler, Witch, Undead
    character_classes = [Man, Peasant, Merchant, Bandit, Mavka, Perelisnyk, ForestGuardian, Demon, Witch, Undead, Nurse, Robber, Traveler]
     # List of all character classes (without Undead being duplicated here)
    # Add Undead(s) to the character pool based on the desired number of Undead encounters
    undead_count = random.randint(1, 2)  # Decide whether we encounter 1 or 2 Undead characters
    
    # Add Undead to the character pool if needed
    for _ in range(undead_count):
        character_classes.append(Undead)  # Append Undead to the list of classes to allow 1 or 2 occurrences

    # Select a random character class from the available classes
    new_character = random.choice(character_classes)(self.player)
    return new_character