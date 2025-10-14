# Note: __ private; _ protected

import random

class Game():
    def __init__(self):
        self._fails = 0

    def start(self) -> None:
        self._fails = 0
    
    def is_over(self) -> bool:
        return False

    def get_failed_attempts(self) -> int:
        return self._fails

class BoardGame(Game):
    EMPTY_CELL = 0

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self._board = []

    def _init_board(self) -> None:
        for _ in range(self.height):
            self._board.append([BoardGame.EMPTY_CELL] * self.width)

    def set_width(self, width) -> None:
        self.width = width

    def get_width(self) -> int:
        return self.width

    def set_height(self, height) -> None:
        self.height = height 
    
    def get_height(self) -> int:
        return self.height
    
    def start(self) -> None:
        super().start()
        self._board = []
        self._init_board()

    def print_board(self) -> None:
        for row in self._board:
            print(row)
    
    def get_board(self) -> list[list[int]]:
        # return a copy of the board
        return [row[:] for row in self._board]

    def _get_random_position(self):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        return (x, y)
