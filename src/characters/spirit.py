from abc import abstractmethod
from characters.character import Character
from game.player import Player
from constants import *
from utils import *
SPIRIT_TYPE = 's'

class Spirit(Character):
    """Represents a base Spirit class with shared behavior for spirit characters."""

    @abstractmethod
    def __init__(self, player: Player):
        """Initialize with a player instance."""
        self.player = player

    def do_action(self):
        """Abstract method for performing an action, implemented by subclasses."""
        pass

    def guess_character(self):
        """Prompts player to guess if the character is human or spirit."""
        return input("Is it a human or a spirit? (h/s): ").strip().lower()


class Mavka(Spirit):
    """If guessed correctly, player skips the next two character encounters."""

    def __init__(self, player: Player):
        self.player = player
        #super().__init__(player)

    def do_action(self):
        """Introduces Mavka and presents a riddle if guessed correctly; else, removes a life."""
        self.introduce()
        if self.guess_character() == SPIRIT_TYPE:
            print(MAVKA_INTRO)
            self.give_riddle()  # Implement riddle logic
        else:
            print(MAVKA_KILLS)
            rem_life(self.player)

    def give_riddle(self):
        """Presents a riddle to the player."""
        print(load_speech(self, MAVKA_RIDDLE_PATH))

    def introduce(self):
        """Introduces Mavka through a scripted speech."""
        print(load_speech(self, MAVKA_SPEECH_PATH))


class Perelisnyk(Spirit):
    """Gives riddles related to fire. Can be further differentiated from Mavka."""

    def __init__(self, player: Player):
        self.player = player
        #super().__init__(player)

    def do_action(self):
        """Introduces Perelisnyk and presents a riddle if guessed correctly; else, removes a life."""
        self.introduce()
        if self.guess_character() == SPIRIT_TYPE:
            print(PERELISNYK_INTRO)
            self.give_riddle()  # Implement riddle logic
        else:
            print(PERELISNYK_KILLS)
            rem_life(self.player)

    def give_riddle(self):
        """Presents a fire-themed riddle to the player."""
        print(load_speech(self, PERELISNYK_RIDDLE_PATH))

    def introduce(self):
        """Introduces Perelisnyk through a scripted speech."""
        print(load_speech(self, PERELISNYK_SPEECH_PATH))


class ForestGuardian(Spirit):
    """Gives 2 riddles to the player in general. If the Player chooses to listen to the Undead, gives 3 riddles."""

    def __init__(self, player: Player, undead_met: str, rejection_flag: str):
        #super().__init__(player)
        self.player = player
        self.riddle_num = 2  # Default riddle number (2)
        self.undead_met = undead_met  # "yes" or "no" whether Undead has been met
        self.rejection_flag = rejection_flag  # "yes" or "no" if the player rejected the Undead's story

    def do_action(self):
        """Introduces the Forest Guardian and presents riddles based on the player's encounter with the Undead."""
        self.introduce()

        # If the player has met the Undead
        if self.undead_met == "yes":
            # If the player accepted the Undead's story, give 3 riddles
            if self.rejection_flag == "no":
                self.riddle_num = 3
            else:
                self.riddle_num = 2  # If the player rejected the Undead's story, give only 2 riddles
        else:
            # Default behavior for the Forest Guardian
            self.riddle_num = 2

        # Ask riddles based on the player's previous decisions
        if self.guess_character() == SPIRIT_TYPE:
            print(FORESTGUARDIAN_INTRO)
            self.give_riddle()  # Ask riddles
        else:
            print(FORESTGUARDIAN_KILLS)
            rem_life(self.player)

    def give_riddle(self):
        """Presents riddles to the player."""
        print(load_speech(self, FORESTGUARDIAN_RIDDLE1_PATH))
        if self.riddle_num == 3:
            print(load_speech(self, FORESTGUARDIAN_RIDDLE2_PATH))
            print(FORESTGUARDIAN_ADD_RIDDLE)
            print(load_speech(self, FORESTGUARDIAN_RIDDLE3_PATH))  # Third riddle
        else:
            print(load_speech(self, FORESTGUARDIAN_RIDDLE2_PATH))

    def introduce(self):
        """Introduces the Forest Guardian through a scripted speech."""
        print(load_speech(self, FORESTGUARDIAN_SPEECH_PATH))



class Demon(Spirit):
    """Demon character. If player guesses the riddle correctly, they receive a reward. If not, the Demon takes a large amount of coins."""

    def __init__(self, player: Player):
        self.player = player
        #super().__init__(player)
        self.riddle = load_speech(self, DEMON_RIDDLE_PATH)
        self.speech = load_speech(self, DEMON_SPEECH_PATH)

    def do_action(self):
        """Performs Demon's action based on player's guess.
        If correct, presents a riddle; otherwise, takes coins or
        items, or kills."""
        stolen_coins = 0
        if self.guess_character() == SPIRIT_TYPE:
            print(self.speech)
            print(self.riddle)  # Print the riddle if guessed correctly
        else:
            if self.player.coins > 0:
                stolen_coins = min(self.player.coins, 10)  # Steal up to 10 coins
                self.player.coins -= stolen_coins
                print(DEMON_STEALS_COINS)
                print(f"Demon has stolen {stolen_coins} coins!")
            else:
                # Check if the player has any items
                if any(count > 0 for count in self.player.items.values()):
                    print(DEMON_GIVES_A_CHANCE)
                    answer = input(DEMON_BRIBE).strip().lower()
                    if answer == GIVE_TO_DEMON:
                        # Remove the first available item
                        for item, count in self.player.items.items():
                            if count > 0:
                                self.player.items[item] -= 1
                                break
                        print(DEMON_RETREATS)
                    else:
                        print(DEMON_KILLS)
                        rem_life(self.player)
                else:
                    print(DEMON_KILLS)
                    rem_life(self.player)
