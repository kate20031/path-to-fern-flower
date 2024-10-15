# Питає, чи хочеш дізн. про іст. смерті, якщо ні - кікаєш персонажа,
# так - розповідь і пропуск ходу.
class Undead(Silent):
 def __init__(self, name):
        self.name = name
        self.speech = self.load_speech('assets/texts/undead_speech.txt')

    def load_speech(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()  
        except FileNotFoundError:
            print(f"Error: The file {file_path} was not found.")
            return ""
    
    def ask_question(self):
        question = "Do you want to know, how I died?"
        print(question)

    def tell_story(self):
        print(self.speech)
    
    def process_answer(self, answer, life_count):
        if answer == true:
            tell_story()
        else:     
            life_count -= 1
        return life_count
        
    def do_action(self):
        printf("")
        
