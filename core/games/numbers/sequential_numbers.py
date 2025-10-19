from typing import override
from core.games.game.game import BoardGame

class SequentialNumbersGame(BoardGame):
    def __init__(self, board_width: int = 5, board_height: int = 5, numbers: int = 3) -> None:
        super().__init__(board_width, board_height)
        self.__numbers = numbers
        self.__sequency = []
        self.__current_number = 0

    @override
    def start(self) -> None:
        super().start()
        self.__current_number = 0
        self._fails = 0
        self.__place_numbers()

    def __place_numbers(self) -> None:
        self.__sequency.clear()
        for i in range (self.__numbers):
            x, y = self._get_random_position()
            while self._board[y][x] != 0:
                x, y = self._get_random_position()
            self._board[y][x] = i + 1
            self.__sequency.append((x, y))

    def play(self, x, y) -> bool:
        if self.is_over():
            return False

        # Check if coordinates are valid
        if not (0 <= x < self._board_width and 0 <= y < self._board_height):
            print(f"Coordinates out of range: ({x}, {y})")
            self._fails += 1
            return False

        if ((x, y) == self.__sequency[self.__current_number]):
            self.__current_number += 1
            return True
        else:
            self._fails += 1
            return False
    
    @override
    def is_over(self) -> bool:
        return self.__current_number == len(self.__sequency)
