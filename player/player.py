class Player():
    def __init__(self) -> None:
        self.__life = 3

    def decrement_life(self) -> None:
        self.__life -= 1

    def reset(self) -> None:
        self.__life = 3

    def get_life(self) -> int:
        return self.__life
