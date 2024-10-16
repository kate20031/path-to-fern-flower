from ..characters.silent import Nurse, Robber, Traveler, Witch, Undead
#ONLY FOR SILENT CHARACTERS
class Game:
    def __init__(self):
        self.character_classes = [Nurse, Robber, Traveler, Witch, Undead]
        self.characters = self.create_characters()


    def create_characters(self):
        # Instantiate each character class automatically
        return [character_class() for character_class in self.character_classes]


    def run(self):
        for character in self.characters:
            character.do_action()  # Call the do_action method for each character


if __name__ == "__main__":
    game = Game()
    game.run()
