import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from characters.human import Merchant, Peasant, Man, Bandit
from characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
from characters.silent import Nurse, Robber, Traveler, Witch, Undead
from game.player import Player
from utils import *

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

        # Load and display image
        image_path = "..\\path-to-fern-flower\\media\\images\\img.png"
        img = Image.open(image_path)
        img = img.resize((400, 400))  # Resize image to fit the window
        img_tk = ImageTk.PhotoImage(img)

        label_image = tk.Label(self.window, image=img_tk)
        label_image.image = img_tk
        label_image.pack(pady=20)

        # Player information display
        player_info = f"Nickname: {self.player.nickname}\nCoins: {self.player.coins}\nLives: {self.player.lives}\nItems: {self.player.items}"
        label_info = tk.Label(self.window, text=player_info, font=("Arial", 14))
        label_info.pack(pady=10)

        # Buttons for Human and Spirit choices
        button_human = tk.Button(self.window, text="Human", font=("Arial", 12), command=self.on_human_choice)
        button_spirit = tk.Button(self.window, text="Spirit", font=("Arial", 12), command=self.on_spirit_choice)

        button_human.pack(side=tk.LEFT, padx=40)
        button_spirit.pack(side=tk.RIGHT, padx=40)

        self.window.mainloop()

    def on_human_choice(self):
        messagebox.showinfo("Human", "You chose Human!")
        self.run_game_loop("human")

    def on_spirit_choice(self):
        messagebox.showinfo("Spirit", "You chose Spirit!")
        self.run_game_loop("spirit")

    def run_game_loop(self, choice):
        global met_people, met_spirits, met_silent

    def run(self):
        global met_people, met_spirits, met_silent

        for character in self.characters:
            # Якщо персонаж не є ForestGuardian або Undead, просто виконуємо його дію
            if not isinstance(character, (ForestGuardian, Undead)):
                character.do_action()

            # Якщо гравець помер, виводимо повідомлення і завершуємо гру
            if not self.player.is_alive:
                print("Game Over. You are dead.")
                self.window.quit()
                break  # Завершуємо гру, якщо гравець мертвий

            # Перевірка, чи є персонаж людиною
            if isinstance(character, tuple(self.people_classes)):
                met_people += 1
                character.guess_character()
            # Перевірка, чи є персонаж духом
            elif isinstance(character, tuple(self.spirit_classes)):
                met_spirits += 1
                character.guess_character()
                if isinstance(character, ForestGuardian):
                    # Передача відповідних параметрів щодо зустрічі з Undead
                    undead_met = "yes" if self.first_encountered_undead else "no"
                    result = character.do_action()
                    
                    # Обробка результату дії ForestGuardian
                    if result == "yes":
                        self.first_encountered_undead = True
                    elif result == "no":
                        self.rejection_flag = "no"

            # Перевірка, чи є персонаж мовчазною істотою (Undead)
            else:
                met_silent += 1
                if isinstance(character, Undead):
                    # Якщо це перша зустріч, передаємо відповідні параметри
                    already_met = "yes" if self.first_encountered_undead else "no"
                    rejection_flag = self.rejection_flag if self.first_encountered_undead else None
                    result = character.do_action()
                    
                    # Оновлюємо інформацію після зустрічі з Undead
                    if result == "yes":
                        self.rejection_flag = "yes"
                        self.first_encountered_undead = True
                    elif result == "no":
                        self.rejection_flag = "no"
                        self.first_encountered_undead = True

        # Оновлюємо лічильники для персонажів
        self.player.set_characters_counters(total_people - met_people, total_spirits - met_spirits)
        self.player.set_characters_list(self.characters)


if __name__ == "__main__":
    player = Player("a")
    game = Game(player)
    game.run()
