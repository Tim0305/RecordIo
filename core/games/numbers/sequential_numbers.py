import random

class SequentialNumbersGame():
    def __init__(self, width = 5, height = 5, numbers = 3):
        self.width = width
        self.height = height
        self.__numbers = numbers
        self.__board = []
        self.__sequency = []
        self.__current_number = 0
        self.__fails = 0

    def start(self):
        self.__current_number = 0
        self.__fails = 0
        self.__sequency = []
        self.__init_board()
        self.__place_numbers()

    def __init_board(self):
        self.__board = []
        for _ in range(self.height):
            self.__board.append([0] * self.width)

    def __place_numbers(self):
        for i in range (self.__numbers):
            x, y = self.__get_random_position()
            while self.__board[y][x] != 0:
                x, y = self.__get_random_position()
            self.__board[y][x] = i + 1
            self.__sequency.append((x, y))

    def __get_random_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)

    def play(self, x, y):
        if (0 <= x < self.width and 0 <= y < self.height):
            if ((x, y) == self.__sequency[self.__current_number]):
                self.__current_number += 1
                return True
            else:
                self.__fails += 1
                return False
    
    def is_over(self):
        return self.__current_number == len(self.__sequency)

    def get_failed_attempts(self):
        return self.__fails

    def print_board(self):
        for i in range(self.height):
            print(self.__board[i])
