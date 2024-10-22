from abc import ABC, abstractmethod
from ..characters.character import Character

class Human(Character):
   @abstractmethod
   def do_action(self):
      pass 

# Просто ставить питання.
class Man(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        pass

# Дає підказку за товар, інакше - бреше.
class Peasant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        pass

# Продає товар молоко, від духів, від бандита який потім можна виміняти.
class Merchant(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        pass 

# Дає шанс відкупитись, інакше - :(
class Bandit(Human):
    def __init__(self, player):
        super().__init__(player)

    def introduce(self):
        pass

    def do_action(self):
        pass
