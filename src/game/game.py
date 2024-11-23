import os
import sys
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.game.player import Player
from src.characters.human import Man, Peasant, Merchant, Bandit
from src.characters.silent import Witch, Undead, Nurse, Robber, Traveler
from src.characters.spirit import Mavka, ForestGuardian, Demon, Perelisnyk

from src.utils import create_new_character

total_people = 0
met_people = 0
total_spirits = 0
met_spirits = 0
total_silent = 0
met_silent = 0

class Game:
    def __init__(self, pl):
        self.player = pl
        global total_people, total_spirits, total_silent

        self.people_classes = [Man, Peasant, Merchant, Bandit]
        self.spirit_classes = [Mavka, Perelisnyk, ForestGuardian, Demon]
        self.silent_classes = [Witch, Undead, Nurse, Robber, Traveler]

        total_people = len(self.people_classes)
        total_spirits = len(self.spirit_classes)
        total_silent = len(self.silent_classes)

        # Ініціалізація атрибутів для відслідковування зустрічей з Undead
        self.first_encountered_undead = False  # Перша зустріч з Undead
        self.rejection_flag = None  # Чи відмовився гравець від історії Undead

        self.character_classes = self.people_classes + self.spirit_classes + self.silent_classes
        self.characters = self.create_characters()
        self.create_game_window()

    def create_characters(self):
        characters = []
        
        # Створення персонажів із можливістю зустріти 1 чи 2 Undead
        for _ in range(7):  # Припустимо, ми хочемо створити 7 персонажів у грі
            # Створюємо нового персонажа за допомогою утилітної функції, передаючи статус зустрічі з Undead
            new_character = create_new_character(self)
            
            # Додаємо новоствореного персонажа до списку
            characters.append(new_character)

        return characters

    def create_game_window(self):
        self.window = tk.Tk()
        self.window.title("Path to Fern Flower")

        # Load and display background image
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        image_path = os.path.join(base_dir, "static/images/background.png")
        img = Image.open(image_path)
        img = img.resize((425, 283))  # Resize image to fit the window
        img_tk = ImageTk.PhotoImage(img)

        label_image = tk.Label(self.window, image=img_tk)
        label_image.image = img_tk
        label_image.pack(pady=20)

        # Player information display
        player_info = f"Nickname: {self.player.nickname}  Coins: {self.player.coins}  Lives: {self.player.lives}\nItems: {self.player.items}"
        label_info = tk.Label(self.window, text=player_info, font=("Arial", 14))
        label_info.pack(pady=10)

        # Buttons for Human and Spirit choices
        button_human = tk.Button(self.window, text="Human", font=("Arial", 12), command=self.on_human_choice)
        button_spirit = tk.Button(self.window, text="Spirit", font=("Arial", 12), command=self.on_spirit_choice)

        button_human.pack(side=tk.LEFT, padx=40)
        button_spirit.pack(side=tk.RIGHT, padx=40)

        # Display character image
        self.character_label = tk.Label(self.window)
        self.character_label.pack(pady=20)

        # Dialogue box for interaction with characters
        self.dialogue_box = tk.Label(self.window, text="", font=("Arial", 12), width=50, height=4, anchor="w", justify="left")
        self.dialogue_box.pack(pady=10)

        self.window.mainloop()

    def on_human_choice(self):
        messagebox.showinfo("Human", "You chose Human!")
        self.run_game_loop("human")

    def on_spirit_choice(self):
        messagebox.showinfo("Spirit", "You chose Spirit!")
        self.run_game_loop("spirit")

    def run_game_loop(self, choice):
        global met_people, met_spirits, met_silent

        for character in self.characters:
            # Display character image dynamically based on type
            self.display_character_image(character)

            # Dynamically create interaction buttons
            self.show_choice_buttons(character)

            if not self.player.is_alive:
                print("Game Over. You are dead.")
                self.window.quit()
                break

            # Check if the character is a human
            if any(isinstance(character, cls) for cls in self.people_classes):
                met_people += 1
                self.dialogue_box.config(text=f"You met a {character.__class__.__name__}!")
                character.guess_character()
            
            # Check if the character is a spirit
            elif any(isinstance(character, cls) for cls in self.spirit_classes):
                met_spirits += 1
                self.dialogue_box.config(text=f"You met a {character.__class__.__name__}!")
                character.guess_character()
            
            # If it's a silent entity (Undead, Witch, etc.)
            else:
                met_silent += 1
                self.dialogue_box.config(text=f"You met a {character.__class__.__name__}!")

        # Update player counters for met characters
        self.player.set_characters_counters(total_people - met_people, total_spirits - met_spirits)
        self.player.set_characters_list(self.characters)

    def display_character_image(self, character):
        # Отримуємо ім'я класу персонажа (дочірнього класу)
        character_class_name = character.__class__.__name__
        print(f"Displaying image for class: {character_class_name}")  # Діагностичний вивід
        
        # Формуємо шлях до зображення, використовуючи ім'я дочірнього класу
        image_path = self.get_character_image_path(character_class_name)

        # Відкриваємо зображення
        img = Image.open(image_path)
        img = img.resize((60, 60))  # Змінюємо розмір зображення для вікна
        img_tk = ImageTk.PhotoImage(img)

        # Оновлюємо зображення на екрані
        self.character_label.config(image=img_tk)
        self.character_label.image = img_tk  # Зберігаємо посилання на зображення

    def get_character_image_path(self, character_class_name):
        print(f"Getting image for class: {character_class_name}")  # Діагностичний вивід
        # Базовий шлях до зображень
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        
        # Формуємо шлях до зображення, залежно від точного імені класу персонажа
        image_path = os.path.join(base_dir, f"static/images/{character_class_name}.png")
        
        return image_path


    def show_choice_buttons(self, character):
        # Hide the buttons for now and show the options
        if isinstance(character):
            button_human = tk.Button(self.window, text="Talk to this Human", font=("Arial", 12), command=self.on_human_choice)
            # button_human = tk.Button(self.window, text="Talk to this Human", font=("Arial", 12), command=self.on_human_choice)
            # button_spirit = tk.Button(self.window, text="Talk to this Spirit", font=("Arial", 12), command=self.on_spirit_choice)

            # button_human.pack(side=tk.LEFT, padx=40)
            # button_spirit.pack(side=tk.RIGHT, padx=40)
