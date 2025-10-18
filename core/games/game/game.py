# Note: __ private; _ protected

import random

class Game:
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

    def __init__(self, board_width, board_height):
        super().__init__()
        self._board_width = board_width
        self._board_height = board_height
        self._board = []

    def _init_board(self) -> None:
        self._board.clear()
        for _ in range(self._board_height):
            self._board.append([BoardGame.EMPTY_CELL] * self._board_width)

    def set_board_width(self, board_width) -> None:
        self._board_width = board_width

    def get_board_width(self) -> int:
        return self._board_width

    def set_board_height(self, board_height) -> None:
        self._board_height = board_height 
    
    def get_board_height(self) -> int:
        return self._board_height
    
    def start(self) -> None:
        super().start()
        self._init_board()

    def print_board(self) -> None:
        for row in self._board:
            print(row)
    
    def get_board(self) -> list[list[int]]:
        # return a copy of the board
        return [row[:] for row in self._board]

    def _get_random_position(self):
        x = random.randint(0, self._board_width - 1)
        y = random.randint(0, self._board_height - 1)
        return (x, y)
