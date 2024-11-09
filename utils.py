import random

def load_speech(self, file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""

def rem_life(player):
    if player.lives >= 1:
        player.lives -= 1
        print("You have lost 1 life")
    else:
        print("Game over")

def create_new_character(self, first_encountered_undead, rejection_flag) -> None:
    from src.characters.human import Merchant, Peasant, Man, Bandit
    from src.characters.spirit import Perelisnyk, ForestGuardian, Mavka, Demon
    from src.characters.silent import Nurse, Robber, Traveler, Witch, Undead

    # Список персонажів (без Undead на старті)
    character_classes = [Man, Peasant, Merchant, Bandit, Mavka, Perelisnyk, ForestGuardian, Demon, Witch, Nurse, Robber, Traveler]
    
    # Визначаємо кількість Undead для зустрічі (1 або 2)
    undead_count = random.randint(1, 2)  # Decide whether we encounter 1 or 2 Undead characters
    
    # Списки для відслідковування зустрічей з Undead
    undead_encounters = []
    
    # Додаємо Undead до списку персонажів
    for _ in range(undead_count):
        undead_encounters.append(Undead)
    
    # Розширюємо список персонажів, додаючи Undead
    character_classes.extend(undead_encounters)

    # Вибираємо випадковий персонаж зі списку (але без Undead, якщо це не перша зустріч)
    chosen_class = random.choice(character_classes)

    # Якщо це Undead, передаємо правильні параметри для зустрічей
    if chosen_class == Undead:
        # Якщо це перша зустріч з Undead, передаємо "no" та None
        if not self.first_encountered_undead:
            already_met = "no"
            rejection_flag = None
        else:
            # Якщо Undead вже був зустрічений, передаємо останні оновлені значення
            already_met = "yes"
            rejection_flag = self.rejection_flag
        
        # Створюємо Undead і передаємо ці параметри в конструктор
        new_character = Undead(self.player, already_met, rejection_flag)
        
        # Якщо це перша зустріч з Undead, оновлюємо статус першої зустрічі
        if not self.first_encountered_undead:
            self.first_encountered_undead = True
    
    # Якщо це ForestGuardian, передаємо параметри
    elif chosen_class == ForestGuardian:
        # Параметри для ForestGuardian
        undead_met = "yes" if self.first_encountered_undead else "no"
        rejection_flag = self.rejection_flag
        
        # Створюємо ForestGuardian і передаємо ці параметри в конструктор
        new_character = ForestGuardian(self.player, undead_met, rejection_flag)

    # Для інших персонажів просто створюємо їх без додаткових параметрів
    else:
        new_character = chosen_class(self)

    return new_character
