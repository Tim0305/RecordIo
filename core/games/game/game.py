# Note: __ private; _ protected

# Importa las librerías
import random
from typing import override

# Clase base que define lo básico que debe tener un juego
class Game:
    '''
    Nombre: __init__
    Descripción: Inicializa la clase Game estableciendo el contador de intentos fallidos (_fails) en 0.
    '''
    def __init__(self) -> None:
        # Atributos de la clase
        self._fails = 0

    '''
    Nombre: start
    Descripción: Reinicia el número de intentos fallidos al iniciar una nueva partida.
    '''
    def start(self) -> None:
        self._fails = 0
    
    '''
    Nombre: is_over
    Descripción: Método que las clases hijas deben implementar.
    Devuelve True si el juego ha terminado, False en caso contrario.
    '''
    def is_over(self) -> bool: ...

    '''
    Nombre: get_failed_attempts
    Descripción: Devuelve el número de intentos fallidos acumulados hasta el momento.
    '''
    def get_failed_attempts(self) -> int:
        return self._fails

# Clase que hereda de la clase Game, y define un juego de tablero
class BoardGame(Game):
    # Constante que define una celda vacía en el tablero
    EMPTY_CELL = 0

    '''
    Nombre: __init__
    Parámetros: board_width (int), board_height (int)
    Descripción: Inicializa la clase BoardGame con el ancho y alto del tablero.
    '''
    def __init__(self, board_width: int, board_height: int) -> None:
        # Ejecuta el constructor padre
        super().__init__()
        
        # Atributos de la clase
        self._board_width = board_width
        self._board_height = board_height
        self._board = []

    '''
    Nombre: _init_board
    Descripción: Limpia e inicializa el tablero llenándolo con celdas vacías (EMPTY_CELL)
    según las dimensiones establecidas (ancho y alto).
    '''
    def _init_board(self) -> None:
        # Limpia los datos de la lista
        self._board.clear()

        # Crea un tablero representado por una lista de listas
        for _ in range(self._board_height):
            self._board.append([BoardGame.EMPTY_CELL] * self._board_width)

    '''
    Nombre: set_board_width
    Parámetros: board_width (int)
    Descripción: Establece el ancho del tablero con el valor recibido.
    '''
    def set_board_width(self, board_width: int) -> None:
        self._board_width = board_width

    '''
    Nombre: get_board_width
    Descripción: Devuelve el ancho actual del tablero.
    '''
    def get_board_width(self) -> int:
        return self._board_width

    '''
    Nombre: set_board_height
    Parámetros: board_height (int)
    Descripción: Establece la altura del tablero con el valor recibido.
    '''
    def set_board_height(self, board_height: int) -> None:
        self._board_height = board_height 
    
    '''
    Nombre: get_board_height
    Descripción: Devuelve la altura actual del tablero.
    '''
    def get_board_height(self) -> int:
        return self._board_height
    
    '''
    Nombre: start
    Descripción: Sobrescribe el método de la clase padre. Reinicia el estado del juego heredado de la clase Game
    y genera un nuevo tablero vacío llamando a _init_board().
    '''
    @override
    def start(self) -> None:
        super().start()
        self._init_board()

    '''
    Nombre: print_board
    Descripción: Imprime en consola el tablero fila por fila.
    '''
    def print_board(self) -> None:
        for row in self._board:
            print(row)
    
    '''
    Nombre: get_board
    Descripción: Retorna una copia independiente del tablero actual como lista de listas.
    Esto evita modificar el tablero original fuera de la clase.
    '''
    def get_board(self) -> list[list[int]]:
        # return a copy of the board
        return [row[:] for row in self._board]

    '''
    Nombre: _get_random_position
    Descripción: Genera y retorna una tupla (x, y) con una posición aleatoria válida dentro del tablero.
    '''
    def _get_random_position(self) -> tuple[int, int]:
        # Generar el valor de X y Y de forma aleatoria usando randint, pasando los
        # límites del tablero
        x = random.randint(0, self._board_width - 1)
        y = random.randint(0, self._board_height - 1)
        return (x, y)
