# Питає, чи хочеш дізн. про іст. смерті, якщо ні - кікаєш персонажа,
# так - розповідь і пропуск ходу.
class Undead(Silent):
    def ask_question(self):
        question = "Do you want to know, how I died?"
        print(question)

    def tell_story(self):
        
    
    def process_answer(self, answer, life_count):
        if answer == true:
            tell_story()
        else:     
            life_count -= 1
        return life_count
        
    def do_action(self):
        printf("")
        
