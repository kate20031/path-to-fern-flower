from game.player import Player
from game.game import Game

if __name__ == "__main__":
    player = Player("a")
    game = Game(player)
    game.run()
