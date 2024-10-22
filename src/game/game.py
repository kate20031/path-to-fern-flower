#Global counters for total and met characters
from src.game.player import Player

total_people = 0
met_people = 0
total_spirits = 0
met_spirits = 0

# game.py
from src.characters.silent import Nurse, Robber, Traveler, Witch, Undead

#ONLY FOR SILENT CHARACTERS
class Game:
    def __init__(self, player):
        self.player = player
        global total_people, total_spirits

        # Definition which characters are people and which are spirits
        self.people_classes = [Nurse, Robber, Traveler]
        self.spirit_classes = [Witch, Undead]

        # Count all people and spirit characters
        total_people = len(self.people_classes)
        total_spirits = len(self.spirit_classes)

        self.character_classes = self.people_classes + self.spirit_classes
        self.characters = self.create_characters(player)

    def create_characters(self, player):
        return [character_class(self.player) for character_class in self.character_classes]


    def run(self):
        global met_people, met_spirits

        for character in self.characters:
            character.do_action()

            # Update the met counters
            if isinstance(character, tuple(self.people_classes)):
                met_people += 1
                #print(f"Met {met_people} out of {total_people} people.")
            elif isinstance(character, tuple(self.spirit_classes)):
                met_spirits += 1
                #print(f"Met {met_spirits} out of {total_spirits} spirits.")

if __name__ == "__main__":
    player = Player("a")
    game = Game(player)
    game.run()
