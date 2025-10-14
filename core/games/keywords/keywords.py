import string
import random

from core.games.game.game import Game

class KeywordsGame(Game):
    # static attributes
    __CHARACTERS = string.ascii_letters + string.digits

    def __init__(self, length = 5, n = 3):
        super().__init__()
        self.__keywords = []
        self.__length = length
        self.__number_of_keywords = n
        self.__current_key_index = 0

    def start(self) -> None:
        super().start()
        self.__current_key_index = 0
        self.__generate_keywords()
        
    def __generate_keywords(self) -> None:
        self.__keywords = []
        for _ in range(self.__number_of_keywords):
            self.__keywords.append("".join(random.choice(self.__CHARACTERS) for _ in range(self.__length)))

    def set_length(self, length) -> None:
        self.__length = length

    def get_length(self) -> int:
        return self.__length

    def set_number_of_keywords(self, n) -> None:
        self.__number_of_keywords = n

    def play(self, key) -> bool:
        if key == self.__keywords[self.__current_key_index]:
            self.__current_key_index += 1
            return True
        else:
            self._fails += 1
            self.__current_key_index += 1
            return False 
    
    def get_current_keyword(self) -> str:
        return self.__keywords[self.__current_key_index]

    def is_over(self) -> bool:
        return self.__current_key_index == self.__number_of_keywords
