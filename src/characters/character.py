from abc import ABC, abstractmethod

class Character(ABC):
   @abstractmethod
   def introduce(self):
      print ("Hi!")
      return
