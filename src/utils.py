import random

def load_speech(self, file_path):  # Removed 'self' since it isn't required
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

def create_new_character(self):
    from characters.human import Merchant, Peasant, Man, Bandit
    from characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
    from characters.silent import Nurse, Robber, Traveler, Witch, Undead

    # Base list of characters (without Undead initially)
    character_classes = [Man, Peasant, Merchant, Bandit, Mavka, Perelisnyk, ForestGuardian, Demon, Witch, Nurse, Robber, Traveler]

    # Add 1 or 2 Undead characters to the mix
    undead_count = random.randint(1, 2)
    for _ in range(undead_count):
        character_classes.append(Undead)

    # Randomly select a character class
    chosen_class = random.choice(character_classes)

    # Handle Undead-specific logic
    if chosen_class == Undead:
        # Determine parameters for the Undead
        already_met = "yes" if self.first_encountered_undead else "no"
        rejection_flag = self.rejection_flag if self.first_encountered_undead else None
        new_character = chosen_class(self.player, already_met, rejection_flag)

        # Update the first encounter flag
        self.first_encountered_undead = True

    # Handle ForestGuardian-specific logic
    elif chosen_class == ForestGuardian:
        undead_met = "yes" if self.first_encountered_undead else "no"
        rejection_flag = self.rejection_flag
        new_character = chosen_class(self.player, undead_met, rejection_flag)

    # Handle all other characters
    else:
        new_character = chosen_class(self.player)

    return new_character