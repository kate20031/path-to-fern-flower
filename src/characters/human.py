from abc import ABC, abstractmethod
from ..characters.character import Character

class Human(Character):
   @abstractmethod
   def do_action(self):
      pass 
   
   def guess_character(self):
        return input("Is it a human or a spirit? (h/s): ").strip().lower()

# Просто ставить питання.
class Man(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Man")

# Дає підказку за товар, інакше - бреше.
class Peasant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Peasant")

# Продає товар молоко, від духів, від бандита який потім можна виміняти.
class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Merchant")

# Дає шанс відкупитись, інакше - :(
class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        print("I am Bandit")
