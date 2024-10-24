from abc import ABC, abstractmethod
from ..characters.character import Character
from src.game.player import Player  # Імпорт класу Player
from constants import *
from utils import load_speech

class Spirit(Character):
   @abstractmethod

   def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

   def do_action(self):
      pass 
   
   def guess_character(self):
        return input("Is it a human or a spirit? (h/s): ").strip().lower()

 # Якщо вгадаєш, пропускаєш наступний хід.
class Mavka(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)
        self.riddle =load_speech(self, MAVKA_RIDDLE_PATH)
        self.speech = load_speech(self, MAVKA_SPEECH_PATH)

    def do_action(self):
        self.introduce()
        if self.guess_character() == 's': 
            print(self.speech) #чот чат гпт накатав мені таку промову, хаха
            print(self.riddle)  # Print the riddle if guessed correctly
        else:
            self.rem_life()
        pass

    def introduce(self):
        print("I am Mavka")
       
    
    def rem_life(self):
        if self.player.lives >= 1:
            self.player.lives -= 1  # Забирає життя, якщо їх кількість більше = 1
            print("Mavka has wounded you!")
        else:
            print("Game over")

# Дає загадки про вогонь.
class Perelisnyk(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def guess_character(self):
        pass

    def do_action(self):
        print("I am Perelisnyk")

# Дає 2 загадки.
class ForestGuardian(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def guess_character(self):
        pass

    def do_action(self):
        print("I am ForestGuardian")

# Демон(чорт). Якщо вгадати загадку - дає багато грошей, якщо ні - забирає багато грошей
class Demon(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)
        self.riddle =load_speech(self, DEMON_RIDDLE_PATH)
        self.speech = load_speech(self, DEMON_SPEECH_PATH)

    def do_action(self):
        if self.guess_character() == 's': 
            print(self.speech) 
            print(self.riddle)  # Print the riddle if guessed correctly
        else:
            if self.player.coins:
                if self.player.coins>=10: 
                    stolen_coins = 10
                    self.player.coins-= stolen_coins
                else: 
                    stolen_coins = stolen_coins
                    self.player.coins = 0
                print(DEMON_STEALS_COINS)
                print(f"Demon has stolen {stolen_coins} coins!")
            else:
                print(DEMON_SEES_NO_COINS)
                self.rem_life()
    
    def rem_life(self):
        if self.player.lives >= 1:
            self.player.lives -= 1  # Забирає життя, якщо їх кількість більше = 1
            print("Demon has wounded you!")
        else:
            print("Game over")

