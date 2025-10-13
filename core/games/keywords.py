import string
import random

class KeywordsGame():
    # static attributes
    __CHARACTERS = string.ascii_letters + string.digits

    def __init__(self, length = 5, n = 3):
        self.__keywords = []
        self.__length = length
        self.__number_of_keywords = n
        self.__current_key_index = 0
        self.__fails = 0

    def start(self):
        self.__current_key_index = 0
        self.__fails = 0
        self.__generate_keywords()
        
    def __generate_keywords(self):
        self.__keywords = []
        for _ in range(self.__number_of_keywords):
            self.__keywords.append("".join(random.choice(self.__CHARACTERS) for _ in range(self.__length)))

    def set_length(self, length):
        self.__length = length

    def set_number_of_keywords(self, n):
        self.__number_of_keywords = n

    def play(self, key):
        if key == self.__keywords[self.__current_key_index]:
            self.__current_key_index += 1
            return True
        else:
            self.__fails += 1
            self.__current_key_index += 1
            return False 
    
    def get_current_keyword(self):
        return self.__keywords[self.__current_key_index]

    def is_over(self):
        return self.__current_key_index == self.__number_of_keywords

    def get_failed_attempts(self):
        return self.__fails
