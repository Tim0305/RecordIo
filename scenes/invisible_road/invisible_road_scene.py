# Importar las librerías necesarias para el manejo de gráficos, escenas y lógica del juego
import pygame
from typing import override
from core.games.invisible_road.invisible_road import InvisibleRoadGame
from player.player import Player
from scenes.components.block.block import Block
from scenes.scene.game_scene import GameScene
from scenes.scene.scene_manager import SceneManager
from util.file import write_game_data
from util.timer import Timer


'''
Clase que representa la escena principal del juego "Invisible Road".
Controla la lógica de interacción entre el jugador, los bloques visuales del tablero
y el flujo general del juego (inicio, fin, victoria o derrota). Hereda de GameScene.
'''
class InvisibleRoadScene(GameScene):
    '''
    Nombre: __init__
    Parámetros: player (Player), board_width (int), board_height (int), screen (pygame.Surface), manager (SceneManager | None)
    Descripción: Inicializa la escena del juego, configura el tablero, los bloques, 
    el temporizador y los parámetros visuales.
    '''
    def __init__(
        self,
        player: Player,
        board_width: int,
        board_height: int,
        screen,
        manager: SceneManager | None = None,
    ) -> None:
        # Inicializar la escena base con la imagen de fondo
        super().__init__(player, screen, manager, "assets/images/background_5.png")
        
        # Lógica del juego
        self.game = InvisibleRoadGame(board_width, board_height)
        self.game.start()
        
        # Matriz (lista de listas) de objetos tipo block
        self.__blocks = []

        # Configuraciones visuales de los bloques
        self.__block_width = 130
        self.__block_height = 130
        self.__spacing = 5

        # Tiempo en ms que se tarda en mostrar el camino invisible
        self.__reveal_road_time = 5000  # ms

        # Temporizador
        self.__timer = Timer()

        # Bandera que permite controlar cuando mostrar el camino invisible
        self.__road_visible = True
        self.__draw_blocks()

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Gestiona los eventos del juego, incluyendo los clics del jugador. 
    Determina si el jugador gana, pierde o continúa jugando según sus acciones.
    '''
    @override
    def handle_events(self, events) -> None:
        super().handle_events(events)
        if self._player.get_life() == 0:
            # Si el jugador se queda sin vidas
            self._player.increment_fails()
            # Actualizar el archivo data.txt
            write_game_data(self._player)
            # Mostrar el caminuo oculto
            self.__show_road()
            self.draw()  # Actualizar pantalla para mostrar el camino
            # Mostrar un mensaje de Game Over
            self.show_game_over()
            if self.manager != None:
                # Regresar al menu principal
                self.manager.go_back()
        elif self.game.is_over():
            # Si el jugador completa correctamente el camino
            self._player.increment_wins()
            # Actualizar el archivo data.txt
            write_game_data(self._player)
            # Mostrar un mensaje de victoria
            self.show_win()
            if self.manager != None:
                # Regresar al menu principal
                self.manager.go_back()
        else:
            # Verifica los clics en los bloques del tablero
            for event in events:
                for i in range(len(self.__blocks)):
                    for j in range(len(self.__blocks[i])):
                        if self.__blocks[i][j].is_clicked(event):
                            if self.game.play(j, i):
                                self.__blocks[i][j].set_selected(True)
                            else:
                                self._player.decrement_life()

    '''
    Nombre: draw
    Descripción: Dibuja los elementos visuales del juego en la pantalla, 
    incluyendo el fondo y los bloques del tablero.
    '''
    @override
    def draw(self) -> None:
        super().draw()
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                self.__blocks[i][j].draw(self.screen)

    '''
    Nombre: update
    Parámetros: events (list[pygame.Event])
    Descripción: Actualiza el estado del juego y se encarga de mostrar al inicio el camino oculto
    '''
    @override
    def update(self, events) -> None:
        super().update(events)
        if self.__road_visible:
            self.__reveal_road()

    '''
    Nombre: __draw_blocks
    Descripción: Crea y posiciona los bloques del tablero en la pantalla, 
    centrando el conjunto visual en función del tamaño del tablero.
    '''
    def __draw_blocks(self) -> None:
        # Limpia la matriz de bloques
        self.__blocks.clear()

        # Calcular el tamaño total del tablero
        total_blocks_width = (
            self.game.get_board_width() * (self.__block_width + self.__spacing)
            - self.__spacing
        )
        total_blocks_height = (
            self.game.get_board_height() * (self.__block_height + self.__spacing)
            - self.__spacing
        )
        screen_width, screen_height = self.screen.get_size()

        # Calcular la posición inicial para centrar el tablero
        x_start = (screen_width - total_blocks_width + self.__block_width) // 2
        y_start = (screen_height - total_blocks_height + self.__block_height) // 2

        # Crear los bloques y agregarlos al tablero
        for i in range(self.game.get_board_height()):
            self.__blocks.append([])

            # Reiniciar los valores conforme a cada fila de la matriz de bloques
            x = x_start
            y = y_start + i * (self.__block_height + self.__spacing)

            for _ in range(self.game.get_board_width()):
                block = Block(self.__block_width, self.__block_height, (x, y))
                x += self.__block_width + self.__spacing
                self.__blocks[i].append(block)

    '''
    Nombre: __reveal_road
    Descripción: Controla el tiempo durante el cual el camino es visible al jugador. 
    Cuando el temporizador finaliza, el camino se oculta y los bloques se activan.
    '''
    def __reveal_road(self) -> None:
        if self.__timer.is_active():
            if self.__timer.is_finished():
                # Ocultar el camino y habilitar los bloques
                self.__road_visible = False
                self.__enable_blocks()
                self.__hide_road()
            else:
                # Deshabilitar los bloques y mostrar el camino
                self.__road_visible = True
                self.__disable_blocks()
                self.__show_road()
        else:
            # Iniciar el timer
            self.__timer.start(self.__reveal_road_time)

    '''
    Nombre: __show_road
    Descripción: Muestra visualmente el camino correcto que debe memorizar el usuario en el tablero
    '''
    def __show_road(self) -> None:
        road = self.game.get_road() # Obtener el camino
        for i in range(len(road)):
            x, y = road[i]
            self.__blocks[y][x].set_selected(True) # Seleccionar el bloque
            self.__blocks[y][x].set_text(str(i + 1)) # Agregar texto al bloque para indicar el orden en que se recorre el camino

    '''
    Nombre: __hide_road
    Descripción: Oculta el camino del tablero, removiendo los números 
    y desactivando la selección de los bloques.
    '''
    def __hide_road(self) -> None:
        road = self.game.get_road() # Obtener el camino
        for i in range(len(road)):
            x, y = road[i]
            self.__blocks[y][x].set_selected(False) # Deseleccionar el bloque
            self.__blocks[y][x].set_text("") # Quitar el texto del bloque

    '''
    Nombre: __enable_blocks
    Descripción: Habilita la interacción del jugador con todos los bloques del tablero.
    '''
    def __enable_blocks(self) -> None:
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                self.__blocks[i][j].enable()

    '''
    Nombre: __disable_blocks
    Descripción: Deshabilita la interacción del jugador con todos los bloques del tablero.
    '''
    def __disable_blocks(self) -> None:
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                self.__blocks[i][j].disable()
