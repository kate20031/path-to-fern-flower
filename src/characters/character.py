from abc import ABC, abstractmethod

from src.game.player import Player


class Character(ABC):
   @abstractmethod
   def introduce(self):
      pass

   def __init__(self, player: Player):
      self.player = player  # Зберігаємо екземпляр Player