from typing import override
import pygame
from player.player import Player
from scenes.components.button.button import Button
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.misc.misc_scene import MiscScene
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager
from scenes.sequential_numbers.sequential_numbers_scene import SequentialNumbersScene

class MenuScene(Scene):
    __OPTIONS = ["Invisible Road", "Keywords", "Sequential Numbers", "Misc"]

    def __init__(self, player: Player, screen, manager: SceneManager | None = None) -> None:
        super().__init__(screen, manager)
        self.__buttons = []
        self.__player = player

        # Background
        # Convierte la imagen al mismo formato de la pantalla
        self.__background = pygame.image.load("assets/images/RecordIo.png").convert()
        self.__background = pygame.transform.scale(self.__background, self.screen.get_size())

        # Buttons
        self.__draw_buttons()

        # Statistics
        self.__font = pygame.font.Font("assets/fonts/Jersey15-Regular.ttf", 50)
        self.__font_color = (231, 153, 15)

    @override
    def handle_events(self, events) -> None:
        super().handle_events(events)
        for event in events:
            for button in self.__buttons:
                if (button.is_clicked(event)):
                    option = button.get_text()
                    
                    # Scenes
                    if self.manager != None:
                        if option == "Invisible Road": 
                            # Reiniciar vidas del jugador
                            self.__player.reset()
                            self.manager.go_to(InvisibleRoadScene(self.__player, 5, 5, self.screen, self.manager))              
                        elif option == "Keywords":
                            # Reiniciar vidas del jugador
                            self.__player.reset()
                            self.manager.go_to(KeywordsScene(self.__player, 6, 3, self.screen, self.manager))                    
                        elif option == "Sequential Numbers":
                            # Reiniciar vidas del jugador
                            self.__player.reset()
                            self.manager.go_to(SequentialNumbersScene(self.__player, 5, 5, 8, self.screen, self.manager))
                        elif option == "Misc":
                            # Reiniciar vidas del jugador
                            self.__player.reset()
                            self.manager.go_to(MiscScene(self.__player, self.screen, self.manager))
    
    @override
    def draw(self) -> None:
        super().draw()
        self.screen.blit(self.__background, (0, 0))
        for button in self.__buttons:
            button.draw(self.screen)

        # Statistics
        self.__draw_statistics()

    def __draw_buttons(self) -> None:
        # Espaciado entre botones
        spacing = 40
        screen_width, screen_height = self.screen.get_size()
        
        # Obtener el ancho que abarcan todos los botones
        total_width = 0
        for option in self.__OPTIONS:
            button = Button(option, (0, 0))
            self.__buttons.append(button)
            total_width += button.get_size()[0] + spacing
        # Eliminar el ultimo espaciado
        total_width -= spacing
        
        x = (screen_width - total_width) // 2
        y = screen_height * 0.8

        # Posicionar los botones
        for button in self.__buttons:
            w, _ = button.get_size()
            button.set_position((x + w // 2, y))
            x += w + spacing
    
    def __draw_statistics(self) -> None:
        # Obtener datos del jugador
        total_games = self.__player.get_wins() + self.__player.get_fails()
        wins = self.__player.get_wins()
        fails = self.__player.get_fails()

        # Líneas de texto
        lines = [
            f"Total Games: {total_games}",
            f"Wins: {wins}",
            f"Fails: {fails}"
        ]

        line_spacing = 5  # separación entre líneas

        # Calcular tamaño del rectángulo según el texto
        ancho = max(self.__font.size(linea)[0] for linea in lines)
        alto = len(lines) * self.__font.get_height() + (len(lines) - 1) * line_spacing

        # Posición del rectángulo
        screen_width, screen_height = self.screen.get_size()
        x = screen_width - ancho - 80
        y = (screen_height - alto) // 2
        rect = pygame.Rect(x, y, ancho, alto)
        rect.inflate_ip(60, 60)  # agranda rectángulo; puede cambiar width/height

        # Dibujar rectángulo
        pygame.draw.rect(self.screen, (133, 53, 22), rect, border_radius=50)  # relleno
        pygame.draw.rect(self.screen, (56, 22, 9), rect, width=12, border_radius=50)  # borde

        # Calcular posición vertical del bloque de texto centrado dentro del rect
        total_text_height = len(lines) * self.__font.get_height() + (len(lines) - 1) * line_spacing
        start_y = rect.top + (rect.height - total_text_height) // 2

        # Dibujar las líneas
        for i, linea in enumerate(lines):
            render = self.__font.render(linea, True, self.__font_color)
            text_rect = render.get_rect()
            text_rect.left = rect.left + 25  # margen horizontal opcional
            text_rect.top = start_y + i * (self.__font.get_height() + line_spacing)
            self.screen.blit(render, text_rect)
