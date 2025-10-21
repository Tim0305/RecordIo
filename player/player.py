class Player():
    def __init__(self, wins: int = 0, fails: int = 0) -> None:
        self.__wins = wins
        self.__fails = fails
        self.__life = 3

    def decrement_life(self) -> None:
        self.__life -= 1

    def reset(self) -> None:
        self.__life = 3

    def get_life(self) -> int:
        return self.__life
    
    def increment_wins(self) -> None:
        self.__wins += 1

    def increment_fails(self) -> None:
        self.__fails += 1

    def get_wins(self) -> int:
        return self.__wins

    def get_fails(self) -> int:
        return self.__fails
