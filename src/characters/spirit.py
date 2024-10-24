from abc import ABC, abstractmethod
from ..characters.character import Character
from src.game.player import Player  # Імпорт класу Player
from constants import MAVKA_RIDDLE_PATH, MAVKA_SPEECH_PATH

class Spirit(Character):
   @abstractmethod

   def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

   def do_action(self):
      pass 
   
   def guess_character(self):
        return input("Is it a human or a spirit? (h/s): ").strip().lower()
        
   def load_speech(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return ""

 # Якщо вгадаєш, пропускаєш наступний хід.
class Mavka(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)
        self.riddle = self.load_speech(MAVKA_RIDDLE_PATH)
        self.speech = self.load_speech(MAVKA_SPEECH_PATH)

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

# Дає гроші (спонсор)
class Demon(Spirit):
    def __init__(self, player: Player):
        super().__init__(player)

    def guess_character(self):
        pass

    def do_action(self):
        print("I am Demon")



