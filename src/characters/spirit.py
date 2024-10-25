from abc import ABC, abstractmethod
from ..characters.character import Character
from src.game.player import Player  # Імпорт класу Player
from constants import *
from utils import *

class Spirit(Character):
   @abstractmethod

   def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

   def do_action(self):
      pass 
   
   def guess_character(self):
        return input("Is it a human or a spirit? (h/s): ").strip().lower()


 # Якщо вгадаєш, пропускаєш наступний 2 наступних зустрічних персонажів.
class Mavka(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.introduce()
        if self.guess_character() == 's': 
            print(MAVKA_INTRO) 
            self.give_riddle() #реалізувати логіку загадки
        else:
            print(MAVKA_KILLS)
            rem_life(self)

    def give_riddle(self):
        print(load_speech(self, MAVKA_RIDDLE_PATH))

    def introduce(self):
        print(load_speech(self, MAVKA_SPEECH_PATH))
       

# Дає загадки про вогонь.
# можна ще щось додати особливе, щоб відрізнялося від Мавки?
class Perelisnyk(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.introduce()
        if self.guess_character() == 's': 
            print(PERELISNYK_INTRO) 
            self.give_riddle() #реалізувати логіку загадки
        else:
            print(PERELISNYK_KILLS)
            rem_life(self)

    def give_riddle(self):
        print(load_speech(self, PERELISNYK_RIDDLE_PATH))

    def introduce(self):
        print(load_speech(self, PERELISNYK_SPEECH_PATH))


# Дає 2 загадки.
class ForestGuardian(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def do_action(self):
        self.introduce()
        if self.guess_character() == 's': 
            print(FORESTGUARDIAN_INTRO) 
            self.give_riddle() #реалізувати логіку загадки
        else:
            print(FORESTGUARDIAN_KILLS)
            rem_life(self)

    def give_riddle(self):
        print(load_speech(self, FORESTGUARDIAN_RIDDLE1_PATH))
        print(load_speech(self, FORESTGUARDIAN_RIDDLE2_PATH))

    def introduce(self):
        print(load_speech(self, FORESTGUARDIAN_SPEECH_PATH))


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
                if self.player.items[0]:
                    print(DEMON_GIVES_A_CHANCE)
                    answer = input(DEMON_BRIBE).strip().lower()
                    if answer == GIVE_TO_DEMON:
                        self.player.items[0] = None
                        print(DEMON_RETREATS)
                    else: 
                        self.kill_player()
                else:
                    self.kill_player()

    def kill_player(self):
        print(DEMON_KILLS)
        rem_life()


