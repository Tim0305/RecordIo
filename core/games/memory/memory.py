import random

from core.games.memory.card import Card 

class MemoryGame():
    def __init__(self, width = 3, height = 2):
        if (width * height) % 2 == 0:
            self.width = width
            self.height = height
            self.__board = []
            self.__cards = []
            self.__fails = 0
        else:
            raise ValueError("width x height has to be even")

    def start(self):
        self.__fails = 0
        self.__init_cards()
        self.__init_board()

    def __init_cards(self):
        if len(self.__cards) == 0:
            number_of_cards = (self.width * self.height) // 2

            for i in range(number_of_cards):
                self.__cards.append(Card(i))

    def __init_board(self):
        self.__board = []
        for _ in range(self.height):
            self.__board.append([-1] * self.width)
        
        # Place the cards in the board
        for i in range(len(self.__cards)):
            # 2 cards
            for _ in range(2):
                x, y = self.__get_random_position()
                while self.__board[y][x] != -1:
                    x, y = self.__get_random_position()
                self.__board[y][x] = self.__cards[i].id

    def __get_random_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)

    def play(self, x1, y1, x2, y2):
        # Check if coordinates are valid
        if not (0 <= x1 < self.width and 0 <= x2 < self.width and 0 <= y1 < self.height and 0 <= y2 < self.height):
            print(f"Coordinates out of range: ({x1}, {y1}) - ({x2}, {y2})")
            self.__fails += 1
            return False
            # raise ValueError("Coordinates out of range")

        if ((x1 != x2 or y1 != y2) and self.__board[y1][x1] == self.__board[y2][x2] and self.__board[y1][x1] != -1):
            # Remove the card from the list
            self.__cards = [c for c in self.__cards if c.id != self.__board[y1][x1]]
            self.__board[y1][x1] = -1
            self.__board[y2][x2] = -1
            return True
        else:
            self.__fails += 1
            return False

    def is_over(self):
        return len(self.__cards) == 0

    def get_failed_attempts(self):
        return self.__fails

    def set_cards(self, cards):
        if len(cards) == (self.width * self.height):
            self.__cards = cards
        else:
            raise ValueError("The number of cards has to be even")
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_board(self):
        return self.__board

    def print_board(self):
        for i in range(self.height):
            print(self.__board[i])

