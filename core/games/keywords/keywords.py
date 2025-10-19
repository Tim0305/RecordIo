import string
import random
from typing import override

from core.games.game.game import Game

class KeywordsGame(Game):
    # static attributes
    __CHARACTERS = string.ascii_letters + string.digits

    def __init__(self, length: int = 5, n: int = 3) -> None:
        super().__init__()
        self.__keywords = []
        self.__length = length
        self.__number_of_keywords = n
        self.__current_key_index = 0

    @override
    def start(self) -> None:
        super().start()
        self.__current_key_index = 0
        self.__generate_keywords()
        
    def __generate_keywords(self) -> None:
        self.__keywords.clear()
        while len(self.__keywords) < self.__number_of_keywords:
            key = "".join(random.choice(self.__CHARACTERS) for _ in range(self.__length))
            if key not in self.__keywords:
                self.__keywords.append(key)

    def set_length(self, length) -> None:
        self.__length = length

    def get_length(self) -> int:
        return self.__length

    def set_number_of_keywords(self, n) -> None:
        self.__number_of_keywords = n

    def play(self, key: str) -> bool:
        # ya no hay keywords
        if self.__current_key_index >= len(self.__keywords):
            return False

        if key == self.__keywords[self.__current_key_index]:
            self.__current_key_index += 1
            return True
        else:
            self._fails += 1
            self.__current_key_index += 1
            return False 
    
    def get_current_keyword(self) -> str | None:
        if self.__current_key_index < len(self.__keywords):
                return self.__keywords[self.__current_key_index]
        return None

    @override
    def is_over(self) -> bool:
        return self.__current_key_index == self.__number_of_keywords
