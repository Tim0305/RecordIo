# Importar las librerías
import random
from typing import override
from core.games.game.game import BoardGame

# Clase que define el juego del camino invisible. Hereda de BoardGame
class InvisibleRoadGame(BoardGame):
    '''
    Nombre: __init__
    Parámetros: board_width (int, opcional), board_height (int, opcional)
    Descripción: Inicializa el juego InvisibleRoadGame con el ancho y alto del tablero.
    '''
    def __init__(self, board_width: int = 3, board_height: int = 3) -> None:
        # Ejecuta el constructor de la clase padre
        super().__init__(board_width, board_height)
        # Atributos privados
        self.__road = [] # Camino
        self.__current_position = 0 # Posición actual del jugador

    '''
    Nombre: start
    Descripción: Reinicia el estado del juego, restablece la posición actual y 
    genera un nuevo camino aleatorio en el tablero llamando a __init_road().
    '''
    @override
    def start(self) -> None:
        # Reset variables
        super().start()
        self.__current_position = 0
        self.__init_road()

    '''
    Nombre: __init_road
    Descripción: Genera un camino aleatorio dentro del tablero. 
    El camino comienza en la primera columna y avanza hacia la derecha, 
    pudiendo moverse hacia arriba, derecha o abajo, sin retroceder a la izquierda.
    '''
    def __init_road(self) -> None:
        self.__road.clear()
        # Crear el camino aleatoriamente
        # 0 -> arriba, 1 -> derecha; 2 -> abajo (nunva izquierda)

        # Obtener la posición inicial
        x = 0
        y = random.randint(0, self._board_height - 1)
        position = (x, y)
        self.__road.append(tuple(position))
        self._board[y][x] = 1

        while x < self._board_width - 1:
            move = random.randint(0, 2)

            if move == 0:
                # Mover Arriba
                if y == 0:
                    y = 0
                else:
                    y -= 1
            elif move == 1:
                # Mover Derecha
                x += 1
            else:
                # Move Abajo
                if y == self._board_height - 1:
                    y = self._board_height - 1
                else:
                    y += 1

            position = (x, y)

            # Verificar si la posición ya existe en el camino
            if position not in self.__road:
                self.__road.append(position)
                self._board[y][x] = 1
            else:
                # Reiniciar el camino
                x = self.__road[-1][0]
                y = self.__road[-1][1]

    '''
    Nombre: play
    Parámetros: x (int), y (int)
    Descripción: Retorna True si la casilla seleccionada es la misma que la casilla en la posición actual,
    y False si es incorrecto o si está fuera de rango.
    '''
    def play(self, x: int, y: int) -> bool:
        if self.is_over():
            return False

        # Posicion repetida
        if (x, y) in self.__road[0 : self.__current_position]:
            return True

        # Validar que las coordenadas sean validas
        if not (0 <= x < self._board_width and 0 <= y < self._board_height):
            print(f"Coordinates out of range: ({x}, {y})")
            self._fails += 1
            return False

        # Si las coordenadas son correctas, aumentar __current_position
        if (x, y) == self.__road[self.__current_position]:
            self.__current_position += 1
            return True
        else:
            self._fails += 1
            return False

    '''
    Nombre: is_over
    Descripción: Retorna True si el juego ha terminado, y False en caso contrario
    '''
    @override
    def is_over(self) -> bool:
        # Si la posición actual es igual al tamaño de la lista del camino, el juego ya terminó
        return self.__current_position == len(self.__road)

    '''
    Nombre: get_road
    Descripción: Devuelve una copia del camino generado en forma de lista de tuplas (x, y).
    '''
    def get_road(self) -> list[tuple[int, int]]:
        return self.__road.copy()

    '''
    Nombre: get_current_position
    Descripción: Devuelve la posición actual del jugador dentro del camino, comenzando en 1.
    '''
    def get_current_position(self) -> int:
        return self.__current_position + 1
