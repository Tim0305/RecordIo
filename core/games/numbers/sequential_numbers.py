import random

from core.games.game.game import BoardGame

class SequentialNumbersGame(BoardGame):
    def __init__(self, width = 5, height = 5, numbers = 3):
        super().__init__(width, height)
        self.__numbers = numbers
        self.__sequency = []
        self.__current_number = 0

    def start(self):
        super().start()
        self.__current_number = 0
        self._fails = 0
        self.__sequency = []
        self.__place_numbers()

    def __place_numbers(self):
        for i in range (self.__numbers):
            x, y = self._get_random_position()
            while self._board[y][x] != 0:
                x, y = self._get_random_position()
            self._board[y][x] = i + 1
            self.__sequency.append((x, y))

    def play(self, x, y):
        if self.is_over():
            return False

        # Check if coordinates are valid
        if not (0 <= x < self.width and 0 <= y < self.height):
            print(f"Coordinates out of range: ({x}, {y})")
            self._fails += 1
            return False

        if ((x, y) == self.__sequency[self.__current_number]):
            self.__current_number += 1
            return True
        else:
            self._fails += 1
            return False
    
    def is_over(self):
        return self.__current_number == len(self.__sequency)
