def load_speech(self, file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return ""

def rem_life(self):
    if self.player.lives >= 1:
        self.player.lives -= 1  # Забирає життя, якщо більше =
        print("You have lost 1 life")
    else:
        print("Game over")