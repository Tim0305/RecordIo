import random
from typing import override
from core.games.game.game import BoardGame

class InvisibleRoadGame(BoardGame):
    def __init__(self, board_width: int = 3, board_height: int = 3) -> None:
        super().__init__(board_width, board_height)
        self.__road = []
        self.__current_position = 0

    @override
    def start(self) -> None:
        # Reset variables
        super().start()
        self.__current_position = 0
        self.__init_road()

    def __init_road(self) -> None:
        self.__road.clear()
        # Create the road randomly
        # 0 -> up, 1 -> right; 2 -> down (never left)

        # Set the initial position
        x = 0
        y = random.randint(0, self._board_height - 1)
        position = (x, y)
        self.__road.append(tuple(position))
        self._board[y][x] = 1

        while x < self._board_width - 1:
            move = random.randint(0, 2)

            if move == 0:
                # Move up
                if y == 0:
                    y = 0
                else:
                    y -= 1
            elif move == 1:
                # Move right
                x += 1
            else:
                # Move down
                if y == self._board_height - 1:
                    y = self._board_height - 1
                else:
                    y += 1

            position = (x, y)
            if position not in self.__road:
                self.__road.append(position)
                self._board[y][x] = 1
            else:
                # Reset the position
                x = self.__road[-1][0]
                y = self.__road[-1][1]

    def play(self, x: int, y: int) -> bool:
        if self.is_over():
            return False

        # Posicion repetida
        if (x, y) in self.__road[0:self.__current_position]:
            return True

        # Validar que las coordenadas sean validas
        if not (0 <= x < self._board_width and 0 <= y < self._board_height):
            print(f"Coordinates out of range: ({x}, {y})")
            self._fails += 1
            return False

        # Si las coordenadas son correctas, aumentar __current_position
        if (x, y) == self.__road[self.__current_position]:
            self.__current_position += 1
            return True
        else:
            self._fails += 1
            return False

    @override
    def is_over(self) -> bool:
        return self.__current_position == len(self.__road)

    def get_road(self) -> list[tuple[int, int]]:
        return self.__road.copy()

    def get_current_position(self) -> int:
        return self.__current_position + 1

    
