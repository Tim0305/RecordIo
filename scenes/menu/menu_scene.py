import pygame
from scenes.components.button.button import Button
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.scene.scene import Scene

class MenuScene(Scene):
    __OPTIONS = ["Invisible Road", "Keywords", "Memory", "Sequential Numbers"]

    def __init__(self, player, screen, manager = None):
        super().__init__(screen, manager)
        self.__buttons = []
        self.player = player

        # Background
        # Convierte la imagen al mismo formato de la pantalla
        background = pygame.image.load("assets/images/background_wood.png").convert()
        background = pygame.transform.scale(background, self.screen.get_size())
        self.screen.blit(background, (0, 0))

        # Buttons
        self.__draw_buttons()

    def handle_events(self, events):
        for event in events:
            for button in self.__buttons:
                if (button.is_clicked(event)):
                    option = button.get_text()

                    if option == "Invisible Road":
                        self.manager.go_to(InvisibleRoadScene(self.player, 3, 2, self.screen, self.manager))                    
    
    def draw(self):
        for button in self.__buttons:
            button.draw(self.screen)

    def __draw_buttons(self):
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
        y = screen_height // 2

        # Posicionar los botones
        for button in self.__buttons:
            w, _ = button.get_size()
            button.set_position((x + w // 2, y))
            x += w + spacing
            
