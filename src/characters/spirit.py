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
        pass
    
   def common_guess_input(self):
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
        self.guess_character()
        pass

    def introduce(self):
        print("I am Mavka")

    def guess_character(self):
        guess = self.common_guess_input()
        
        if guess == 's': 
            print(self.speech) #чот чат гпт накатав мені таку промову, хаха
            print(self.riddle)  # Print the riddle if guessed correctly
        else:
            self.rem_life()
    
    def rem_life(self):
        if self.player.lives >= 1:
            self.player.lives -= 1  # Забирає життя, якщо їх кількість більше = 1
            print("Mavka has wounded you!")
        else:
            print("Game over")

# Дає загадки про вогонь.
class Perelisnyk(Spirit):
    def introduce(self):
        pass

    def do_action(self):
        pass

# Дає 2 загадки.
class ForestGuardian(Spirit):
    def introduce(self):
        pass

    def do_action(self):
        pass

# Дає гроші (спонсор)
class Demon(Spirit):
    def introduce(self):
        pass

    def do_action(self):
        pass

if __name__ == "__main__":
    player = Player("a")
    mavka = Mavka(player)
    mavka.do_action()

