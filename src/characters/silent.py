from abc import ABC, abstractmethod

class Silent(ABC):
   @abstractmethod
   def do_action(self):
       pass

# Додає + 1 життя.
class Nurse(Silent):
    def do_action(self):
        print("I am Nurse")
        pass

# Персонаж-шкідник, краде мовчки.
class Robber(Silent):
    def do_action(self):
        print("I am Robber")
        pass

# Дає підказку про майбутніх персонажів (можна зробити лічильник на духів і людей).
class Traveler(Silent):
    def do_action(self):
        print("I am Traveller")
        pass

# Забирає 1 життя.
class Witch(Silent):
    def do_action(self):
        print("I am Witch")
        pass


# Питає, чи хочеш дізн. про іст. смерті, якщо ні - кікаєш персонажа,
# так - розповідь і пропуск ходу.

class Undead(Silent):
    def __init__(self):
        self.name = "Undead"
        self.speech = self.load_speech('assets/texts/undead_speech.txt')

    @staticmethod
    def ask_question():
        question = "Do you want to know how I died? (yes/no)"
        return input(question).strip().lower() == 'yes'

    def tell_story(self):
        print(self.speech)

    def load_speech(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return ""

    def process_answer(self, answer, life_count):
        if answer:
            self.tell_story()
        else:
            life_count -= 1
        return life_count

    def do_action(self):
        print("I am Undead")
        answer = self.ask_question()
        life_count = 3
        life_count = self.process_answer(answer, life_count)
        print(f"Remaining lives: {life_count}")
