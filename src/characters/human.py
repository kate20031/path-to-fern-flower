from abc import ABC, abstractmethod
from ..characters.character import Character

class Human(Character):
   @abstractmethod
   def sabotage(self):
      pass 

# Просто ставить питання.
class Man(Human):
    def introduce(self):
        pass

    def sabotage(self):
        pass

# Дає підказку за товар, інакше - бреше.
class Peasant(Human):
    def introduce(self):
        pass

    def sabotage(self):
        pass

# Продає товар молоко, від духів, від бандита який потім можна виміняти.
class Merchant(Human):
    def introduce(self):
        pass

    def sabotage(self):
        pass 

# Дає шанс відкупитись, інакше - :(
class Bandit(Human):
    def introduce(self):
        pass

    def sabotage(self):
        pass
