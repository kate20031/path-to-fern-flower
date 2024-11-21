from game.game import Game
from game.player import Player

if __name__ == "__main__":
    player = Player()
    game = Game(player)
    game.run()
