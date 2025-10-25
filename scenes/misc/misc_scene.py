# Importar las librerías necesarias para el manejo de gráficos y escenas
import random
from typing import override
from player.player import Player
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager
from scenes.sequential_numbers.sequential_numbers_scene import SequentialNumbersScene

'''
Clase que representa una escena que selecciona aleatoriamente un minijuego y transfiere el control a esa escena.
Hereda de Scene.
'''
class MiscScene(Scene):
    '''
    Nombre: __init__
    Parámetros: player (Player), screen (pygame.Surface), manager (SceneManager | None)
    Descripción: Inicializa la escena Misc, selecciona aleatoriamente un juego y prepara el estado
    para ejecutar la transición.
    '''
    def __init__(self, player: Player, screen, manager: SceneManager | None = None) -> None:
        # Inicializa la escena
        super().__init__(screen, manager)

        # Jugador
        self.__player = player

        # Opción aleatoria: 0 -> Invisible Road, 1 -> Keywords, 2 -> Sequential Numbers
        self.__opcion = random.randint(0, 2)

        # Estado que asegura que la transición se ejecute solo una vez
        self.__is_playing = True

    '''
    Nombre: update
    Parámetros: events (list[pygame.Event])
    Descripción: Controla la transición hacia la escena seleccionada aleatoriamente. 
    Si ya se realizó la transición, regresa a la escena anterior.
    '''
    @override
    def update(self, events) -> None:
        super().update(events)
        if self.manager != None:
            if self.__is_playing:
                # Establecer la bandera de "jugando" en False para marcar la transición de escenas
                self.__is_playing = False
                # Cambiar a la escena correspondiente según la opción aleatoria
                if self.__opcion == 0:
                    self.manager.go_to(InvisibleRoadScene(self.__player, 5, 5, self.screen, self.manager))
                elif self.__opcion == 1:
                    self.manager.go_to(KeywordsScene(self.__player, 6, 3, self.screen, self.manager))
                elif self.__opcion == 2:
                    self.manager.go_to(SequentialNumbersScene(self.__player, 5, 5, 8, self.screen, self.manager))
            else:
                # Regresar al menu principal si se termina el juego aleatorio
                self.manager.go_back()
