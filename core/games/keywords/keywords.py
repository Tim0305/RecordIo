# Importar las librerias
import string
import random
from typing import override
from core.games.game.game import Game

# Clase que representa un juego de palabras clave generadas aleatoriamente. Hereda de Game
class KeywordsGame(Game):
    # Atributos estaticos
    # String con todos los caracteres alfanuméricos usando la librería string
    __CHARACTERS = string.ascii_letters + string.digits

    '''
    Nombre: __init__
    Parámetros: keyword_length (int, opcional), n (int, opcional)
    Descripción: Inicializa los atributos del juego y define la longitud y cantidad de palabras clave.
    '''
    def __init__(self, keyword_length: int = 5, n: int = 3) -> None:
        super().__init__()
        self.__keywords = []
        self.__keyword_length = keyword_length
        self.__number_of_keywords = n
        self.__current_key_index = 0

    '''
    Nombre: start
    Descripción: Inicia o reinicia el juego y genera las palabras clave aleatorias.
    '''
    @override
    def start(self) -> None:
        # Reinicia los intentos fallidos y el índice actual
        super().start()
        self.__current_key_index = 0
        # Genera nuevas palabras clave
        self.__generate_keywords()
        
    '''
    Nombre: __generate_keywords
    Descripción: Genera una lista de palabras clave aleatorias sin repetición.
    '''
    def __generate_keywords(self) -> None:
        # Limpia cualquier lista previa
        self.__keywords.clear()
        # Crea nuevas palabras clave
        while len(self.__keywords) < self.__number_of_keywords:
            # Selecciona n caracteres aleatorios de __CHARACTERS y los une en un solo string
            key = "".join(random.choice(self.__CHARACTERS) for _ in range(self.__keyword_length))
            # Evita duplicados
            if key not in self.__keywords:
                self.__keywords.append(key)

    '''
    Nombre: set_keyword_length
    Parámetros: keyword_length (int)
    Descripción: Define la cantidad de caracteres de la clave
    '''
    def set_keyword_length(self, keyword_length: int) -> None:
        self.__keyword_length = keyword_length

    '''
    Nombre: get_keyword_length
    Descripción: Retorna el valor de la cantidad de caracteres de la clave
    '''
    def get_keyword_length(self) -> int:
        return self.__keyword_length

    '''
    Nombre: set_number_of_keywords
    Parámetros: n (int)
    Descripción: Define el número total de palabras clave que se generarán.
    '''
    def set_number_of_keywords(self, n) -> None:
        self.__number_of_keywords = n

    '''
    Nombre: play
    Parámetros: key (str)
    Descripción: Evalúa si la palabra ingresada coincide con la palabra clave actual, y retorna True o False.
    '''
    def play(self, key: str) -> bool:
        # Si ya no hay palabras disponibles
        if self.__current_key_index >= len(self.__keywords):
            return False

        # Compara la palabra ingresada con la esperada
        if key == self.__keywords[self.__current_key_index]:
            #  Avanza a la siguiente palabra
            self.__current_key_index += 1
            return True
        else:
            # Incrementa los fallos y avanza a la siguiente palabra
            self._fails += 1
            self.__current_key_index += 1
            return False 
    
    '''
    Nombre: get_current_keyword
    Descripción: Retorna la palabra clave actual que el jugador debe ingresar.
    '''
    def get_current_keyword(self) -> str:
        # Si aún hay palabras por jugar, devuelve la actual
        if self.__current_key_index < len(self.__keywords):
            return self.__keywords[self.__current_key_index]
        # Si no hay más, devuelve una cadena vacía
        return "" 

    '''
    Nombre: is_over
    Descripción: Indica si el juego ha finalizado.
    '''
    @override
    def is_over(self) -> bool:
        # Determina si ya se jugaron todas las palabras
        return self.__current_key_index == self.__number_of_keywords
