class Player:
    """Represents the player character, including attributes like score, coins, lives, and items."""

    def __init__(self):
        """Initializes the player with a nickname, starting coins, lives, and items."""
        self.characters = []
        self._nickname = ""
        self._score = 0
        self._coins = 10  # Starting capital
        self._lives = 3
        self._items = dict(Varenucha=0, Wormwood=0, Bartka=0)
        self.remaining_people = None
        self.remaining_spirits = None
        self.is_alive = True

    def bribe(self):
        """Defines bribe action for the player, to be implemented."""
        pass

    def buy_item(self):
        """Defines item purchasing logic for the player, to be implemented."""
        pass

    def guess(self):
        """Defines guessing action for the player, to be implemented."""
        pass

    def defend(self):
        """Defines defense action for the player, to be implemented."""
        pass

    def listen_undead(self):
        """Defines interaction with undead characters, to be implemented."""
        pass

    @property
    def nickname(self):
        """Getter for the player's nickname."""
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        """Setter for nickname with validation to prevent empty values."""
        if not value:
            raise ValueError("Nickname cannot be empty")
        self._nickname = value

    @property
    def score(self):
        """Getter for the player's score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score, ensuring it cannot be negative."""
        if value < 0:
            raise ValueError("Score cannot be negative")
        self._score = value

    @property
    def coins(self):
        """Getter for the player's coin count."""
        return self._coins

    @coins.setter
    def coins(self, value):
        """Setter for coins, ensuring it cannot be negative."""
        if value < 0:
            raise ValueError("Coins cannot be negative")
        self._coins = value

    @property
    def lives(self):
        """Getter for the player's remaining lives."""
        return self._lives

    @lives.setter
    def lives(self, value):
        """Setter for lives, ensuring it cannot be negative."""
        if value < 0:
            raise ValueError("Lives cannot be negative")
        self._lives = value

    @property
    def items(self):
        """Getter for the player's items."""
        return self._items

    def add_item(self, value):
        """Adds an item if there is an empty slot; otherwise, displays a message."""
        for i in range(len(self._items)):
            if self._items[i] is None:  # Add if the slot is empty
                self._items[i] = value
                return
        print("No space to add more items.")  # Display message if no space available

    def del_item(self, index):
        if 0 <= index < len(self._items):
            removed_item = self._items.pop(index)
            print(f"Removed item: {removed_item}")
            return removed_item
        else:
            print(f"Invalid index {index}. No item removed.")
            return None

    def set_characters_counters(self, remaining_people, remaining_spirits):
        """Sets the counters for remaining people and spirits encountered by the player."""
        self.remaining_people = remaining_people
        self.remaining_spirits = remaining_spirits

    def set_characters_list(self, characters):
        self.characters = characters

    def add_new_character(self, character):
        self.characters.append(character)
