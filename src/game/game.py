import random
from src.characters.human import Merchant, Peasant, Man, Bandit
from src.characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
from src.characters.silent import Nurse, Robber, Traveler, Witch, Undead
from src.game.player import Player
from utils import *

total_people = 0
met_people = 0
total_spirits = 0
met_spirits = 0
total_silent = 0
met_silent = 0

class Game:
    def __init__(self, pl):
        self.player = pl
        global total_people, total_spirits, total_silent

        self.people_classes = [Man, Peasant, Merchant, Bandit]
        self.spirit_classes = [Mavka, Perelisnyk, ForestGuardian, Demon]
        self.silent_classes = [Witch, Undead, Nurse, Robber, Traveler]

        total_people = len(self.people_classes)
        total_spirits = len(self.spirit_classes)
        total_silent = len(self.silent_classes)

        self.character_classes = self.people_classes + self.spirit_classes + self.silent_classes
        self.characters = self.create_characters()

        # Track if the Undead has been encountered
        self.first_encountered_undead = False
        self.rejection_flag = None  # To store player's answer to the Undead's question

    def create_characters(self):
        characters = []
        
        # Create characters using the utility function, allowing for 1 or 2 Undead encounters
        for _ in range(7):  # Let's assume we want to create 7 characters in the game
            # Create a new character using the utility function
            new_character = create_new_character(self)  # Passing the Game instance to the helper function
            
            # Add the newly created character to the characters list
            characters.append(new_character)

        return characters

    def run(self):
        global met_people, met_spirits, met_silent

        for character in self.characters:
            character.do_action()

            if not self.player.is_alive:
                print("Game Over. You are dead.")
                break  # Stop the game if the player is dead

            if isinstance(character, tuple(self.people_classes)):
                met_people += 1
                character.guess_character()
            elif isinstance(character, tuple(self.spirit_classes)):
                met_spirits += 1
                character.guess_character()

                # Handle behavior for ForestGuardian based on Undead's first encounter
                if isinstance(character, ForestGuardian):
                    if self.first_encountered_undead:
                        if self.rejection_flag == "no":
                            # If the player accepted the Undead's story, give 3 riddles
                            character.riddle_num = 3
                        else:
                            # If the player rejected the Undead's story, give 2 riddles (default)
                            character.riddle_num = 2
                    else:
                        # If the Undead hasn't been encountered, default behavior applies
                        character.riddle_num = 2

            else:
                met_silent += 1
                
                if isinstance(character, Undead):
                    # Handle the first and second encounter with Undead
                    if self.first_encountered_undead:
                        # This is the second encounter, we process rejection or life deduction
                        if self.rejection_flag == "no":
                            rem_life(self.player)  # Deduct a life if we rejected the Undead
                    else:
                        # First encounter with Undead
                        self.first_encountered_undead = True
                        self.rejection_flag = character.rejection_flag  # Store the player's response

        self.player.set_characters_counters(total_people - met_people, total_spirits - met_spirits)
        self.player.set_characters_list(self.characters)



if __name__ == "__main__":
    player = Player("a")
    game = Game(player)
    game.run()
