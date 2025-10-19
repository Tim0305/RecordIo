import pygame

class Button:
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        self.__button_color = (215, 121, 10)
        self.__hover_color = (138, 77, 6)
        self.__border_color = (74, 35, 25)
        self.__font_color = (72, 31, 21)
        self.__font_size = 40
        self.__font_name = "assets/fonts/Jersey15-Regular.ttf"
        self.__sound_effect = pygame.mixer.Sound("assets/sounds/click_sound.mp3")
        self.__font = None
        self.__border_radius = 8
        self.__padding = 30
        self.__position = position
        self.__text = text
        self.__rect = pygame.Rect(0, 0, 0, 0)

        self.__load_font()
        self.__render()

    def draw(self, surface) -> None:
        # Hover
        mouse_pos = pygame.mouse.get_pos()
        color = self.__hover_color if self.__rect.collidepoint(mouse_pos) else self.__button_color

        # Dibujar el rectangulo del boton
        # Relleno
        pygame.draw.rect(surface, color, self.__rect, border_radius=self.__border_radius)
        # Borde
        pygame.draw.rect(surface, self.__border_color, self.__rect, width=5, border_radius=self.__border_radius)

        # Agregar y centrar el texto al centro del rectangulo del boton
        surface.blit(self.__render_text, self.__render_text.get_rect(center=self.__rect.center))

    def is_clicked(self, event) -> bool:
        # button == 1 (click izquierdo)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.__rect.collidepoint(event.pos):
            self.__sound_effect.play()
            return True
        else:
            return False


    def get_size(self) -> tuple[int, int]:
        return self.__rect.size

    def get_text(self) -> str:
        return self.__text

    def set_text(self, text: str) -> None:
        self.__text = text
        self.__render()

    # Posiciona el boton en el centro de position
    def set_position(self, position: tuple[int, int]) -> None:
        self.__position = position
        self.__render()

    def set_font_name(self, font: str) -> None:
        self.__font_name = font
        self.__load_font()
        self.__render()

    def set_font_size(self, size: int) -> None:
        self.__font_size = size
        self.__load_font()
        self.__render()

    def __load_font(self) -> None:
        self.__font = pygame.font.Font(self.__font_name, self.__font_size)
        
    def __render(self) -> None:
        # Render text
        self.__render_text = self.__font.render(self.__text, True, self.__font_color)

        # Render rect
        self.__rect = self.__render_text.get_rect(center=self.__position)
        self.__rect.inflate_ip(self.__padding, self.__padding) # Agranda el area clickable

