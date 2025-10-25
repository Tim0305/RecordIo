# Importar las librerías necesarias para el manejo de gráficos, escenas y lógica del juego
import pygame
from typing import override
from core.games.keywords.keywords import KeywordsGame
from player.player import Player
from scenes.scene.game_scene import GameScene
from scenes.scene.scene_manager import SceneManager
from util.file import write_game_data
from util.timer import Timer

'''
Clase que representa la escena del juego de palabras clave (KeywordsGame),
donde el jugador debe memorizar una palabra mostrada brevemente y luego escribirla.
Se encarga de controlar el flujo visual, los eventos del teclado y las condiciones de victoria o derrota. Hereda de GameScene.
'''
class KeywordsScene(GameScene):
    '''
    Nombre: __init__
    Parámetros: player (Player), length (int), n (int), screen (pygame.Surface), manager (SceneManager | None)
    Descripción: Inicializa la escena del juego Keywords. Configura el entorno gráfico,
    inicializa el juego principal, el temporizador y las variables de estado necesarias.
    '''
    def __init__(self, player: Player, length: int, n: int, screen, manager: SceneManager | None = None) -> None:
        # Inicializar la escena base con la imagen de fondo
        super().__init__(player, screen, manager, "assets/images/background_4.png")
        
        # Lógica del juego
        self.game = KeywordsGame(length, n)
        self.game.start()
        
        # Numero de palabras
        self.__number_of_keywords = n

        # Tiempo (en milisegundos) que cada palabra se muestra
        self.__show_keyword_time = 3000
        
        self.__is_writing = False  # Indica si el jugador está escribiendo la palabra
        self.__user_input_text = ""  # Texto que el jugador escribe durante el turno
        self.__font_name = "assets/fonts/Jersey15-Regular.ttf" # Fuente
        
        # Temporizador que controla el tiempo de visualización de las palabras
        self.__timer = Timer()

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Gestiona los eventos del teclado. Permite escribir y borrar texto. Evalúa las palabras escritas por el jugador.
    Determina si el jugador ha ganado o perdido.
    '''
    @override
    def handle_events(self, events):
        super().handle_events(events)

        # Si el jugador perdió todas sus vidas
        if self._player.get_life() == 0:
            self._player.increment_fails()
            # Guardar la información en data.txt
            write_game_data(self._player)
            # Mostrar pantalla de "Game Over"
            self.show_game_over()
            if self.manager is not None:
                # Regresar al menu principal
                self.manager.go_back()

        # Si el jugador completó correctamente todas las palabras
        elif self.game.is_over():
            self._player.increment_wins()
            # Guardar la información en data.txt
            write_game_data(self._player)
            # Mostrar pantalla de victoria
            self.show_win()
            if self.manager is not None:
                # Regresar al menu principal
                self.manager.go_back()

        else:
            # Recorrer todos los eventos
            for event in events:
                if event.type == pygame.KEYDOWN:
                    # Si se presiona la tecla de borrar
                    if event.key == pygame.K_BACKSPACE:
                        # Borrar el último carácter del texto ingresado
                        self.__user_input_text = self.__user_input_text[:-1]

                    # Si se presiona la tecla Enter
                    elif event.key == pygame.K_RETURN:
                        # Solo procesar si el jugador escribió algo
                        if len(self.__user_input_text) != 0:
                            # Verificar si la palabra ingresada es correcta
                            if not self.game.play(self.__user_input_text):
                                self._player.decrement_life()

                            # Limpiar el texto ingresado
                            self.__user_input_text = ""
                            # Cambiar el estado a “no escribiendo”
                            self.__is_writing = False

                    # Si se presiona cualquier otra tecla
                    else:
                        # Solo aceptar texto si el jugador está en modo escritura
                        if self.__is_writing and len(self.__user_input_text) < self.game.get_keyword_length():
                            # Aceptar únicamente caracteres alfanuméricos
                            if event.unicode.isalnum():
                                self.__user_input_text += event.unicode

    '''
    Nombre: draw
    Descripción: Dibuja los elementos visuales del juego.
    Muestra la palabra clave cuando el jugador debe memorizarla,
    y el área de texto cuando el jugador debe escribirla.
    '''
    @override
    def draw(self) -> None:
        super().draw()

        # Solo dibujar si el juego no ha terminado
        if not self.game.is_over():
            # Si el jugador aún no está escribiendo, mostrar la palabra
            if not self.__is_writing:
                # Mostrar la palabra actual generada por el juego
                self.__draw_keyword(self.game.get_current_keyword())

                # Si el temporizador aún no ha comenzado, iniciarlo
                if not self.__timer.is_active():
                    self.__timer.start(self.__show_keyword_time)

                # Una vez terminado el tiempo, cambiar al modo escritura
                if self.__timer.is_finished():
                    self.__is_writing = True
            else:
                # Dibujar el área donde el jugador escribe la palabra
                self.__draw_text_area(self.__user_input_text)

    '''
    Nombre: __draw_keyword
    Parámetros: keyword (str)
    Descripción: Muestra en pantalla la palabra clave que el jugador debe memorizar.
    Aparece centrada en la parte superior de la ventana con un fondo gris y texto blanco.
    '''
    def __draw_keyword(self, keyword: str) -> None:
        # Cargar la fuente y renderizar el texto
        font = pygame.font.Font(self.__font_name, 120)
        render_text = font.render(keyword, True, (255, 255, 255))
        
        # Obtener las dimensiones de la pantalla y el texto
        screen_width, screen_height = self.screen.get_size()
        text_width, text_height = render_text.get_size()

        # Crear un rectángulo ajustado al texto y centrarlo en la parte superior
        rect = pygame.Rect(0, 0, text_width, text_height)
        rect.center = (screen_width / 2, screen_height * 0.2)
        rect.inflate_ip(100, 60)  # Añadir espacio interno (padding)
        
        # Dibujar el rectángulo y texto en pantalla
        pygame.draw.rect(self.screen, (100, 100, 100), rect, border_radius=50)
        self.screen.blit(render_text, render_text.get_rect(center=rect.center))

    '''
    Nombre: __draw_text_area
    Parámetros: text (str)
    Descripción: Dibuja el área de texto donde el jugador escribe.
    '''
    def __draw_text_area(self, text: str):
        # Cargar fuente y renderizar el texto actual
        font = pygame.font.Font(self.__font_name, 100)
        text_area = font.render(text, True, (255, 255, 255))
        
        # Obtener tamaño de la pantalla
        screen_width, screen_height = self.screen.get_size()
        text_area_width, _ = text_area.get_size()

        # Crear un rectángulo centrado debajo de la palabra clave
        rect = pygame.Rect(0, 0, text_area_width + 50, 10)
        rect.center = (screen_width / 2, (screen_height / 2) + 150)
        
        # Dibujar el rectángulo debajo del texto y luego el texto mismo
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        self.screen.blit(text_area, text_area.get_rect(center=(screen_width / 2, (screen_height / 2) + 70)))
