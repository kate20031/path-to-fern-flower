from abc import ABC, abstractmethod
from ..characters.character import Character

class Spirit(Character):
   @abstractmethod
   def give_riddle(self):
      pass 

 # Якщо вгадаєш, пропускаєш наступний хід.
class Mavka(Spirit):
    def introduce(self):
        pass

    def give_riddle(self):
        pass

# Дає загадки про вогонь.
class Perelisnyk(Spirit):
    def introduce(self):
        pass

    def give_riddle(self):
        pass

# Дає 2 загадки.
class ForestGuardian(Spirit):
    def introduce(self):
        pass

    def give_riddle(self):
        pass

# Дає гроші (спонсор)
class Demon(Spirit):
    def introduce(self):
        pass

    def give_riddle(self):
        pass
