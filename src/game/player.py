class Player:
    def __init__(self, nickname):
        self._nickname = nickname
        self._score = 0
        self._coins = 0
        self._lives = 3
        self._items = [None, None, None] #trade_item, spirit_defense, human_defence 

    def bribe(self):
        pass

    def buy_item(self):
        pass

    def guess(self):
        pass

    def defend(self):
        pass

    def listen_undead(self):
        pass

    # Getter for nickname
    @property
    def nickname(self):
        return self._nickname

    # Setter for nickname
    @nickname.setter
    def nickname(self, value):
        if not value:
            raise ValueError("Nickname cannot be empty")
        self._nickname = value

    # Getter for score
    @property
    def score(self):
        return self._score

    # Setter for score
    @score.setter
    def score(self, value):
        if value < 0:
            raise ValueError("Score cannot be negative")
        self._score = value

    # Getter for coins
    @property
    def coins(self):
        return self._coins

    # Setter for coins
    @coins.setter
    def coins(self, value):
        if value < 0:
            raise ValueError("Coins cannot be negative")
        self._coins = value

    # Getter for lives
    @property
    def lives(self):
        return self._lives

    # Setter for lives
    @lives.setter
    def lives(self, value):
        if value < 0:
            raise ValueError("Lives cannot be negative")
        self._lives = value

    # Getter for items
    @property
    def items(self):
        return self._items

    def add_item(self, value):
        for i in range(len(self._items)):
            if self._items[i] is None:  # Додаємо, якщо місце порожнє
                self._items[i] = value
                return
        print("No space to add more items.")  # Якщо немає місця

    def del_item(self, index):
        if 0 <= index < len(self._items):  # Перевірка на допустимість індексу
            removed_item = self._items[index]
            self._items[index] = None  # Позначаємо місце як порожнє
            return removed_item  # Повертаємо видалений предмет
        else:
            raise IndexError("Index out of range")  # Обробка помилки

