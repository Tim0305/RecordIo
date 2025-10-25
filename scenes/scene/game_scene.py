# Importar las librerías necesarias para el manejo de gráficos y escenas
import pygame
from typing import override
from player.player import Player
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager

'''
Clase base que representa una escena jugable. 
Incluye un fondo, un botón de salida, manejo del jugador, 
y métodos para mostrar mensajes de victoria o derrota. Hereda de Scene.
'''
class GameScene(Scene):
    '''
    Nombre: __init__
    Parámetros: player (Player), screen, manager (SceneManager | None), background_img (str)
    Descripción: Inicializa la escena con el jugador, la pantalla, 
    el administrador de escenas y el fondo. También carga el botón de salida y los sonidos.
    '''
    def __init__(
        self, player: Player, screen, manager: SceneManager | None, background_img: str
    ) -> None:
        # Inicializa la escena
        super().__init__(screen, manager)
        
        # Jugador
        self._player = player

        # Fondo: se convierte al formato de la pantalla y se ajusta al tamaño
        self._background = pygame.image.load(background_img).convert()
        self._background = pygame.transform.scale(
            self._background, self.screen.get_size()
        )

        # Fuentes
        self.__pixel_font_name = "assets/fonts/Jersey15-Regular.ttf"
        self.__arcade_font_name = "assets/fonts/ka1.ttf"

        # Tiempo para mostrar el mensaje de Victoria o Game Over
        self.__show_message_time = 3000  # ms

        # Efecto de sonido
        self.__sound_effect = pygame.mixer.Sound("assets/sounds/click_sound.mp3")

        # Botón de salida sin seleccionar
        self.__exit_button_unselected_img = pygame.image.load(
            "assets/images/exit.png"
        ).convert_alpha()
        self.__exit_button_unselected_img = pygame.transform.scale(
            self.__exit_button_unselected_img, (100, 100)
        )

        # Boton de salida seleccionado (Hover)
        self.__exit_button_hover_img = pygame.image.load(
            "assets/images/exit_hover.png"
        ).convert_alpha()
        self.__exit_button_hover_img = pygame.transform.scale(
            self.__exit_button_hover_img, (100, 100)
        )

        # Boton de salida actual
        self.__exit_button = self.__exit_button_unselected_img
        self.__exit_button_rect = self.__exit_button.get_rect(topleft=(50, 50))

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Detecta si el usuario hace clic en el botón de salida 
    y regresa a la escena anterior si hay un administrador activo.
    '''
    @override
    def handle_events(self, events) -> None:
        super().handle_events(events)
        for event in events:
            # Detecta clics sobre el botón de salida
            if (
                event.type == pygame.MOUSEBUTTONDOWN
                and event.button == 1
                and self.__exit_button_rect.collidepoint(event.pos)
            ):
                if self.manager is not None:
                    # Reproducir el sonido de click
                    self.__sound_effect.play()
                    # Regresar al menú principal
                    self.manager.go_back()

    '''
    Nombre: draw
    Descripción: Dibuja el fondo, el botón de salida (con hover) 
    y el texto que muestra las vidas del jugador.
    '''
    @override
    def draw(self) -> None:
        super().draw()
        # Dibujar la imagen de fondo
        self.screen.blit(self._background, (0, 0))

        # Cambiar el botón de salida al pasar el ratón (hover)
        mouse_pos = pygame.mouse.get_pos()
        if self.__exit_button_rect.collidepoint(mouse_pos):
            self.__exit_button = self.__exit_button_hover_img
        else:
            self.__exit_button = self.__exit_button_unselected_img

        # Dibujar el botón de salida
        self.screen.blit(self.__exit_button, self.__exit_button_rect.topleft)

        # Mostrar vidas
        self.__draw_life_text()

    '''
    Nombre: __draw_life_text
    Descripción: Dibuja en la esquina superior derecha el texto con las vidas del jugador.
    '''
    def __draw_life_text(self) -> None:
        # Texto que se muestra
        text = "Lifes: " + str(self._player.get_life())

        # Renderizar el texto con una fuente específica, tamaño de 80, y color blanco
        font = pygame.font.Font(self.__pixel_font_name, 80)
        life_text = font.render(text, True, (255, 255, 255))

        # Posición del texto
        screen_width, _ = self.screen.get_size()
        x = screen_width - (life_text.get_size()[0] / 2) - 50
        y = 50

        # Dibujar el texto en la pantalla
        self.screen.blit(life_text, life_text.get_rect(center=(x, y)))

    '''
    Nombre: show_win
    Descripción: Muestra un mensaje temporal en la pantalla indicando que el jugador ganó.
    '''
    def show_win(self) -> None:
        self.__show_message("You Won", (0, 0, 0), (217, 219, 145))

    '''
    Nombre: show_game_over
    Descripción: Muestra un mensaje temporal en la pantalla indicando que el jugador perdió.
    '''
    def show_game_over(self) -> None:
        self.__show_message("Game Over", (218, 223, 242), (46, 75, 179))

    '''
    Nombre: __show_message
    Parámetros: message (str), font_color (tuple[int, int, int]), bg_color (tuple[int, int, int])
    Descripción: Muestra un mensaje centrado en la pantalla con un fondo transparente 
    durante un tiempo determinado.
    '''
    def __show_message(
        self,
        message: str,
        font_color: tuple[int, int, int],
        bg_color: tuple[int, int, int],
    ) -> None:
        # Renderizar el texto enviado por parámetros usando una fuente específica, un tamaño de 120
        # y el color enviado por parámetros
        font = pygame.font.Font(self.__arcade_font_name, 120)
        game_over_text = font.render(message, True, font_color)

        # Obtener las dimensiones de la pantalla
        screen_width, screen_height = self.screen.get_size()

        # Crear el rectángulo que contiene el texto
        text_width, text_height = game_over_text.get_size() # Obtener las dimensiones del texto
        rect = pygame.Rect(0, 0, text_width, text_height)
        rect.center = (screen_width / 2, screen_height / 2) # Posicionar el rectángulo al centro
        rect.inflate_ip(60, 60) # Aplicar un padding de 60

        # Crear una superficie para que el rectángulo sea transparente
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        # Dibujar el rectángulo usando el color de fondo enviado por parámetros con un redondeo en las esquinas de 50
        pygame.draw.rect(
            s, (bg_color[0], bg_color[1], bg_color[2], 180), s.get_rect(), border_radius=50
        )

        # Mostrar el rectángulo transparente en la pantalla
        self.screen.blit(s, (rect.x, rect.y))
        # Mostrar el texto centrado en la pantalla
        self.screen.blit(
            game_over_text,
            game_over_text.get_rect(center=(screen_width / 2, screen_height / 2)),
        )

        # Actualizar el contenido de la pantalla
        pygame.display.flip()
        # Crear un tiempo de espera para mostrar el mensaje
        pygame.time.delay(self.__show_message_time)
