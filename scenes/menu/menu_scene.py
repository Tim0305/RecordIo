from typing import override
import pygame
from player.player import Player
from scenes.components.button.button import Button
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager

class MenuScene(Scene):
    __OPTIONS = ["Invisible Road", "Keywords", "Memory", "Sequential Numbers"]

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

    @override
    def handle_events(self, events) -> None:
        for event in events:
            for button in self.__buttons:
                if (button.is_clicked(event)):
                    option = button.get_text()

                    if option == "Invisible Road" and self.manager != None:
                        # Reiniciar vidas del jugador
                        self.__player.reset()
                        self.manager.go_to(InvisibleRoadScene(self.__player, 5, 5, self.screen, self.manager))                    
    
    @override
    def draw(self) -> None:
        self.screen.blit(self.__background, (0, 0))

        for button in self.__buttons:
            button.draw(self.screen)

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
            
