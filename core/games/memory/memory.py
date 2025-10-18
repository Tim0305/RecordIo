from core.games.game.game import BoardGame
from core.games.memory.card import Card 

class MemoryGame(BoardGame):
    def __init__(self, width = 3, height = 2):
        if (width * height) % 2 == 0:
            super().__init__(width, height)
            self.__cards = []
        else:
            raise ValueError("width x height has to be even")

    def start(self) -> None:
        super().start()
        self.__init_cards()
        self.__place_cards()

    def __init_cards(self) -> None:
        self.__cards.clear()
        if len(self.__cards) == 0:
            number_of_cards = (self.width * self.height) // 2

            for i in range(BoardGame.EMPTY_CELL, BoardGame.EMPTY_CELL + number_of_cards):
                # + 1 to not be the same as EMPTY_CELL
                self.__cards.append(Card(i + 1))

    def __place_cards(self) -> None:
        # Place the cards in the board
        for i in range(len(self.__cards)):
            # 2 cards
            for _ in range(2):
                x, y = self._get_random_position()
                while self._board[y][x] != BoardGame.EMPTY_CELL:
                    x, y = self._get_random_position()
                self._board[y][x] = self.__cards[i].id


    def play(self, x1, y1, x2, y2) -> bool:
        # Check if coordinates are valid
        if not (0 <= x1 < self.width and 0 <= x2 < self.width and 0 <= y1 < self.height and 0 <= y2 < self.height):
            print(f"Coordinates out of range: ({x1}, {y1}) - ({x2}, {y2})")
            self._fails += 1
            return False

        if ((x1 != x2 or y1 != y2) and self._board[y1][x1] == self._board[y2][x2] and self._board[y1][x1] != -1):
            # Remove the card from the list
            self.__cards = [c for c in self.__cards if c.id != self._board[y1][x1]]
            self._board[y1][x1] = BoardGame.EMPTY_CELL
            self._board[y2][x2] = BoardGame.EMPTY_CELL
            return True
        else:
            self._fails += 1
            return False

    def is_over(self) -> bool:
        return len(self.__cards) == 0

    def set_cards(self, cards) -> None:
        if len(cards) == (self.width * self.height):
            self.__cards = cards
        else:
            raise ValueError("The number of cards has to be even")
