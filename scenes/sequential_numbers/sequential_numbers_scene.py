# Importar las librerías necesarias para manejar la escena y el juego
from core.games.numbers.sequential_numbers import SequentialNumbersGame
from typing import override
from player.player import Player
from scenes.components.block.block import Block
from scenes.scene.game_scene import GameScene
from scenes.scene.scene_manager import SceneManager
from util.file import write_game_data
from util.timer import Timer


'''
Clase que representa la escena del minijuego "Sequential Numbers".
El jugador debe recordar y seleccionar los números en el orden correcto.
Hereda de GameScene y gestiona la lógica de juego, el tablero y las interacciones del jugador.
'''
class SequentialNumbersScene(GameScene):
    '''
    Nombre: __init__
    Parámetros: player (Player), board_width (int), board_height (int), numbers (int), screen (pygame.Surface),
    manager (SceneManager | None)
    Descripción:
        Inicializa la escena creando el tablero de bloques,
        configura los tiempos de visualización de la secuencia
        y prepara el juego para iniciar.
    '''
    def __init__(
        self,
        player: Player,
        board_width: int,
        board_height: int,
        numbers: int,
        screen,
        manager: SceneManager | None = None,
    ) -> None:
        # Inicializa la escena con una imagen de fondo
        super().__init__(player, screen, manager, "assets/images/background_1.png")

        # Lógica de juego
        self.game = SequentialNumbersGame(board_width, board_height, numbers)
        self.game.start()

        # Configuración de los bloques visuales
        self.__blocks = []
        self.__block_width = 130
        self.__block_height = 130
        self.__spacing = 5

        # Tiempo en milisegundos que la secuencia es visible
        self.__reveal_sequency_time = 5000 # ms  

        # Timer
        self.__timer = Timer()

        # Bandera que controla cuando se debe mostrar la secuencia
        self.__sequency_visible = True

        # Generar y posicionar los bloques del tablero
        self.__draw_blocks()

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Gestiona los eventos del juego. Si el jugador pierde todas sus vidas, muestra "Game Over" y regresa al menú.
    Si completa la secuencia correctamente, muestra "You Win" y regresa al menú. Finalmente, si el jugador hace clic en un 
    bloque, se valida si es el número correcto o no.
    '''
    @override
    def handle_events(self, events) -> None:
        super().handle_events(events)
        if self._player.get_life() == 0:
            # Actualizar el estado del jugador
            self._player.increment_fails()
            # Actualizar la información de data.txt
            write_game_data(self._player)
            # Mostrar la secuencia antes de finalizar
            self.__show_sequency()
            # Actualizar la pantalla
            self.draw()
            # Mostrar el mensaje de derrota
            self.show_game_over()
            if self.manager != None:
                # Regresar al menú principal
                self.manager.go_back()

        elif self.game.is_over():
            # Actualizar el estado del jugador
            self._player.increment_wins()
            # Actualizar la información de data.txt
            write_game_data(self._player)
            # Mostrar el mensaje de victoria
            self.show_win()
            if self.manager != None:
                # Regresar al menú principal
                self.manager.go_back()

        else:
            # Validar los clics del jugador sobre los bloques
            for event in events:
                for i in range(len(self.__blocks)):
                    for j in range(len(self.__blocks[i])):
                        if self.__blocks[i][j].is_clicked(event):
                            # Validar si es la opción correcta
                            if self.game.play(j, i):
                                self.__blocks[i][j].set_selected(True)
                                self.__blocks[i][j].set_text(str(self.game.get_current_number()))
                            else:
                                self._player.decrement_life() # Decrementar vidas si no es correcto

    '''
    Nombre: draw
    Descripción: Dibuja el fondo y todos los bloques del tablero en la pantalla.
    '''
    @override
    def draw(self) -> None:
        super().draw()
        for fila in self.__blocks:
            for bloque in fila:
                bloque.draw(self.screen)

    '''
    Nombre: update
    Parámetros: events (list[pygame.Event])
    Descripción: Actualiza la escena cada frame. Controla el tiempo de visualización de la secuencia
    y permite que el jugador empiece a jugar cuando esta se oculta.
    '''
    @override
    def update(self, events) -> None:
        super().update(events)
        if self.__sequency_visible:
            self.__reveal_sequency()

    '''
    Nombre: __draw_blocks
    Descripción: Genera el tablero de bloques del juego. Calcula el centrado de los bloques en pantalla y su espaciado.
    '''
    def __draw_blocks(self) -> None:
        # Limpia la matriz de bloques
        self.__blocks.clear()

        # Calcular la dimensión total que abarcan los bloques en la pantalla
        total_blocks_width = (
            self.game.get_board_width() * (self.__block_width + self.__spacing)
            - self.__spacing
        )
        total_blocks_height = (
            self.game.get_board_height() * (self.__block_height + self.__spacing)
            - self.__spacing
        )

        # Obtener las dimensiones de la pantalla
        screen_width, screen_height = self.screen.get_size()

        # Posición incial de los bloques
        x_start = (screen_width - total_blocks_width + self.__block_width) // 2
        y_start = (screen_height - total_blocks_height + self.__block_height) // 2

        for i in range(self.game.get_board_height()):
            self.__blocks.append([])

            # Reiniciar los valores conforme a cada fila de la matriz de bloques
            x = x_start
            y = y_start + i * (self.__block_height + self.__spacing)

            for _ in range(self.game.get_board_width()):
                # Crear un nuevo bloque
                block = Block(self.__block_width, self.__block_height, (x, y))
                # Actualizar su posicion en X
                x += self.__block_width + self.__spacing
                # Agregarlo a la matriz
                self.__blocks[i].append(block)

    '''
    Nombre: __reveal_sequency
    Descripción: Controla el tiempo en que la secuencia de números está visible.
    Al finalizar el tiempo, se oculta la secuencia y se habilita el tablero.
    '''
    def __reveal_sequency(self) -> None:
        if self.__timer.is_active():
            if self.__timer.is_finished():
                # Ocultar la secuencia y habilitar los bloques
                self.__sequency_visible = False
                self.__enable_blocks()
                self.__hide_sequency()
            else:
                # Mostrar la secuencia y deshabilitar los bloques
                self.__sequency_visible = True
                self.__disable_blocks()
                self.__show_sequency()
        else:
            # Iniciar el timer
            self.__timer.start(self.__reveal_sequency_time)

    '''
    Nombre: __show_sequency
    Descripción: Muestra la secuencia correcta de números al jugador.
    '''
    def __show_sequency(self) -> None:
        sequency = self.game.get_sequency() # Obtener la secuencia
        for i, (x, y) in enumerate(sequency):
            self.__blocks[y][x].set_selected(True) # Seleccionar el bloque
            self.__blocks[y][x].set_text(str(i + 1))# Agregar texto al bloque para indicar el orden de la secuencia

    '''
    Nombre: __hide_sequency
    Descripción: Oculta la secuencia correcta de números.
    '''
    def __hide_sequency(self) -> None:
        sequency = self.game.get_sequency() # Obtener la secuencia
        for x, y in sequency:
            self.__blocks[y][x].set_selected(False) # Deseleccionar el bloque
            self.__blocks[y][x].set_text("") # Quitar el texto del bloque

    '''
    Nombre: __enable_blocks
    Descripción: Habilita todos los bloques del tablero para que el jugador pueda interactuar.
    '''
    def __enable_blocks(self) -> None:
        for fila in self.__blocks:
            for bloque in fila:
                bloque.enable()

    '''
    Nombre: __disable_blocks
    Descripción: Deshabilita todos los bloques del tablero para que el jugador no pueda interactuar.
    '''
    def __disable_blocks(self) -> None:
        for fila in self.__blocks:
            for bloque in fila:
                bloque.disable()
