# Importar las librerías necesarias para el manejo de gráficos y escenas
import pygame
from typing import override
from player.player import Player
from scenes.components.button.button import Button
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.misc.misc_scene import MiscScene
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager
from scenes.sequential_numbers.sequential_numbers_scene import SequentialNumbersScene


'''
Clase que representa el menú principal del juego.
Muestra las distintas opciones disponibles (minijuegos) y las estadísticas del jugador.
Permite cambiar entre escenas de forma interactiva mediante botones. Hereda de Scene.
'''
class MenuScene(Scene):
    # Constante que contiene las opciones del menú
    __OPTIONS = ["Invisible Road", "Keywords", "Sequential Numbers", "Misc"]

    '''
    Nombre: __init__
    Parámetros: player (Player), screen (pygame.Surface), manager (SceneManager | None)
    Descripción: Inicializa la escena del menú, configurando los botones,
    el fondo, la fuente del texto y las estadísticas del jugador.
    '''
    def __init__(self, player: Player, screen, manager: SceneManager | None = None) -> None:
        # Inicializar la escena
        super().__init__(screen, manager)
        
        # Jugador
        self.__player = player        

        # Imagen de fondo principal
        self.__background = pygame.image.load("assets/images/RecordIo.png").convert()
        self.__background = pygame.transform.scale(self.__background, self.screen.get_size())

        # Lista de los botones que se muestran en el menú
        self.__buttons = []
        # Dibujar los botones del menú
        self.__draw_buttons()

        # Fuente y color para las estadísticas
        self.__font = pygame.font.Font("assets/fonts/Jersey15-Regular.ttf", 50)
        self.__font_color = (231, 153, 15)

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Gestiona los eventos del menú principal.
    Detecta los clics sobre los botones y redirige al jugador a la escena correspondiente usando el SceneManager.
    '''
    @override
    def handle_events(self, events) -> None:
        super().handle_events(events)
        for event in events:
            for button in self.__buttons:
                if (button.is_clicked(event)):
                    option = button.get_text()
                    
                    # Cambiar de escena según la opción seleccionada
                    if self.manager != None:
                        if option == "Invisible Road": 
                            self.__player.reset()
                            self.manager.go_to(InvisibleRoadScene(self.__player, 5, 5, self.screen, self.manager))              
                        elif option == "Keywords":
                            self.__player.reset()
                            self.manager.go_to(KeywordsScene(self.__player, 6, 3, self.screen, self.manager))                    
                        elif option == "Sequential Numbers":
                            self.__player.reset()
                            self.manager.go_to(SequentialNumbersScene(self.__player, 5, 5, 8, self.screen, self.manager))
                        elif option == "Misc":
                            self.__player.reset()
                            self.manager.go_to(MiscScene(self.__player, self.screen, self.manager))
    
    '''
    Nombre: draw
    Descripción: Dibuja los elementos del menú principal en pantalla.
    Incluye el fondo, los botones y las estadísticas del jugador.
    '''
    @override
    def draw(self) -> None:
        super().draw()
        self.screen.blit(self.__background, (0, 0))

        # Dibujar los botones del menú
        for button in self.__buttons:
            button.draw(self.screen)

        # Dibujar las estadísticas del jugador
        self.__draw_statistics()

    '''
    Nombre: __draw_buttons
    Descripción: Crea y posiciona los botones del menú en la parte inferior de la pantalla.
    Calcula automáticamente el espaciado y centra los botones horizontalmente.
    '''
    def __draw_buttons(self) -> None:
        spacing = 40
        screen_width, screen_height = self.screen.get_size()
        
        # Calcular el ancho total de los botones (para centrarlos)
        total_width = 0
        for option in self.__OPTIONS:
            button = Button(option, (0, 0))
            self.__buttons.append(button)
            total_width += button.get_size()[0] + spacing
        total_width -= spacing  # Quitar el último espacio adicional
        
        # Posicionar los botones centrados en la parte inferior
        x = (screen_width - total_width) // 2
        y = screen_height * 0.8

        for button in self.__buttons:
            w, _ = button.get_size()
            button.set_position((x + w // 2, y))
            x += w + spacing
    
    '''
    Nombre: __draw_statistics
    Descripción: Muestra las estadísticas del jugador (partidas jugadas, ganadas y perdidas)
    en un recuadro decorativo en la parte derecha de la pantalla.
    '''
    def __draw_statistics(self) -> None:
        # Obtener las estadísticas del jugador
        total_games = self.__player.get_wins() + self.__player.get_fails()
        wins = self.__player.get_wins()
        fails = self.__player.get_fails()

        # Líneas de texto a mostrar
        lines = [
            f"Total Games: {total_games}",
            f"Wins: {wins}",
            f"Fails: {fails}"
        ]

        line_spacing = 5

        # Calcular el tamaño del recuadro en función del texto
        ancho = max(self.__font.size(linea)[0] for linea in lines)
        alto = len(lines) * self.__font.get_height() + (len(lines) - 1) * line_spacing

        # Posición del recuadro en la pantalla
        screen_width, screen_height = self.screen.get_size()
        x = screen_width - ancho - 80
        y = (screen_height - alto) // 2
        rect = pygame.Rect(x, y, ancho, alto)
        rect.inflate_ip(60, 60)

        # Dibujar fondo y borde del recuadro
        pygame.draw.rect(self.screen, (133, 53, 22), rect, border_radius=50)
        pygame.draw.rect(self.screen, (56, 22, 9), rect, width=12, border_radius=50)

        # Calcular posición del texto centrado dentro del recuadro
        total_text_height = len(lines) * self.__font.get_height() + (len(lines) - 1) * line_spacing
        start_y = rect.top + (rect.height - total_text_height) // 2

        # Dibujar las líneas de texto
        for i, linea in enumerate(lines):
            render = self.__font.render(linea, True, self.__font_color)
            text_rect = render.get_rect()
            text_rect.left = rect.left + 25
            text_rect.top = start_y + i * (self.__font.get_height() + line_spacing)
            self.screen.blit(render, text_rect)
