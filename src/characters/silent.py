from abc import ABC, abstractmethod

class Silent(ABC):
   @abstractmethod
   def do_action(self):
       pass