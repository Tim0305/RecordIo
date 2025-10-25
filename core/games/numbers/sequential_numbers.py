# Importar las librerías
from typing import override
from core.games.game.game import BoardGame


'''
Clase que representa un juego donde el jugador debe seleccionar números en orden secuencial
dentro de un tablero generado aleatoriamente.
Hereda de BoardGame
'''
class SequentialNumbersGame(BoardGame):
    '''
    Nombre: __init__
    Parámetros: board_width (int, opcional), board_height (int, opcional), numbers (int, opcional)
    Descripción: Inicializa el tablero, la cantidad de números y las variables de control del juego.
    '''
    def __init__(self, board_width: int = 5, board_height: int = 5, numbers: int = 3) -> None:
        super().__init__(board_width, board_height)
        self.__numbers = numbers
        self.__sequency = []
        self.__current_number = 0

    '''
    Nombre: start
    Descripción: Inicia o reinicia el juego y coloca los números en posiciones aleatorias del tablero.
    '''
    @override
    def start(self) -> None:
        # Reinicia los valores base del juego
        super().start()
        self.__current_number = 0
        self._fails = 0
        # Coloca los números aleatoriamente en el tablero
        self.__place_numbers()

    '''
    Nombre: __place_numbers
    Descripción: Coloca los números en posiciones aleatorias sin repetir dentro del tablero.
    '''
    def __place_numbers(self) -> None:
        # Limpia cualquier secuencia anterior
        self.__sequency.clear()

        # Asigna números del 1 al definido en __numbers
        for i in range(self.__numbers):
            x, y = self._get_random_position()
            # Asegura que no se sobreescriba una celda ya ocupada
            while self._board[y][x] != 0:
                x, y = self._get_random_position()
            self._board[y][x] = i + 1
            self.__sequency.append((x, y))

    '''
    Nombre: play
    Parámetros: x (int), y (int)
    Descripción: Evalúa si la posición seleccionada corresponde al número correcto en secuencia, y retorna True o False.
    '''
    def play(self, x, y) -> bool:
        # Si el juego ya terminó, no permite más jugadas
        if self.is_over():
            return False

        # Verifica que las coordenadas estén dentro del rango permitido
        if not (0 <= x < self._board_width and 0 <= y < self._board_height):
            print(f"Coordinates out of range: ({x}, {y})")
            self._fails += 1
            return False

        # Comprueba si la celda seleccionada es la correcta en la secuencia
        if (x, y) == self.__sequency[self.__current_number]:
            # Avanza al siguiente numero
            self.__current_number += 1
            return True
        else:
            # Si no es correcta, incrementa el contador de fallos
            self._fails += 1
            return False
    
    '''
    Nombre: is_over
    Descripción: Indica si el jugador ya completó la secuencia de números.
    '''
    @override
    def is_over(self) -> bool:
        # Retorna True si se alcanzó el final de la secuencia
        return self.__current_number == len(self.__sequency)

    '''
    Nombre: get_sequency
    Descripción: Retorna una copia de la secuencia de posiciones numéricas del tablero.
    '''
    def get_sequency(self) -> list[tuple[int, int]]:
        # Devuelve la secuencia completa (lista de tuplas)
        return self.__sequency.copy()

    '''
    Nombre: get_current_number
    Descripción: Retorna el índice actual del número que debe seleccionarse.
    '''
    def get_current_number(self) -> int:
        # Devuelve el número actual que el jugador debe encontrar
        return self.__current_number
