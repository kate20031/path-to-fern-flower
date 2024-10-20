from abc import ABC, abstractmethod
import random
from ..game.player import Player  # Імпорт класу Player

class Silent(ABC):
    @abstractmethod
    def do_action(self):
        pass

# Додає + 1 життя.
class Nurse(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

    def do_action(self):
        print("I am Nurse")
        self.add_life()

    def add_life(self):
        if self.player._lives < 3:
            self.player.add_life()  # Додаємо життя, якщо їх менше 3
        else:
            print("No need for more lives.")

# Персонаж-шкідник, краде мовчки.
class Robber(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

    def do_action(self):
        print("I am Robber")
        # Взаємодія з гравцем, якщо потрібно
        pass

    def steal_item(self):
        if self.player._items:
            random_number = random.uniform(1, 2)
            #тут треба повертати інформацію про вкрадений предмет в початковий клас Player

# Дає підказку про майбутніх персонажів (можна зробити лічильник на духів і людей).
class Traveler(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

    def do_action(self):
        print("I am Traveller")
        # Взаємодія з гравцем, якщо потрібно
        pass

# Забирає 1 життя.
class Witch(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player

    def do_action(self):
        print("I am Witch")
        # Взаємодія з гравцем, якщо потрібно
        pass

# Питає, чи хочеш дізн. про іст. смерті, якщо ні - кікаєш персонажа,
# так - розповідь і пропуск ходу.
class Undead(Silent):
    def __init__(self, player: Player):
        self.player = player  # Зберігаємо екземпляр Player
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

if __name__ == "__main__":
    player_instance = Player("Liam")  # Створюємо екземпляр Player
    nurse = Nurse(player_instance)  # Передаємо екземпляр Player медсестрі
    nurse.do_action()  # Викликаємо метод do_action