import random
from core.games.game.game import BoardGame

class InvisibleRoadGame(BoardGame):
    def __init__(self, width=3, height=3):
        super().__init__(width, height)
        self.__road = []
        self.__current_position = 0

    def start(self) -> None:
        # Reset variables
        super().start()
        self.__road = []
        self.__current_position = 0
        self.__init_road()

    def __init_road(self) -> None:
        # Create the road randomly
        # 0 -> up, 1 -> right; 2 -> down (never left)

        # Set the initial position
        x = 0
        y = random.randint(0, self.height - 1)
        position = (x, y)
        self.__road.append(tuple(position))
        self._board[y][x] = 1

        while x < self.width - 1:
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
                if y == self.height - 1:
                    y = self.height - 1
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

    def play(self, x, y) -> bool:
        if self.is_over():
            return False
        if (x, y) == self.__road[self.__current_position]:
            self.__current_position += 1
            return True
        else:
            self._fails += 1
            return False

    def is_over(self) -> bool:
        return self.__current_position == len(self.__road)
