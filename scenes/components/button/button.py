import pygame

class Button:
    def __init__(self, text, position):
        self.__button_color = (60, 60, 60)
        self.__hover_color = (100, 100, 100)
        self.__text_color = (255, 255, 255)
        self.__font_size = 40
        self.__text_font = "assets/fonts/Jersey15-Regular.ttf"
        self.__font = None
        self.__border_radius = 8
        self.__padding = 30
        self.__position = position
        self.__text = text
        self.__rect = pygame.Rect(0, 0, 0, 0)

        self.__load_font()
        self.__render()

    def draw(self, surface):
        # Hover
        mouse_pos = pygame.mouse.get_pos()
        color = self.__hover_color if self.__rect.collidepoint(mouse_pos) else self.__button_color

        # Dibujar el rectangulo del boton
        pygame.draw.rect(surface, color, self.__rect, border_radius=self.__border_radius)

        # Agregar y centrar el texto al centro del rectangulo del boton
        surface.blit(self.__render_text, self.__render_text.get_rect(center=self.__rect.center))

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.__rect.collidepoint(event.pos)

    def get_size(self):
        return self.__rect.size

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text
        self.__render()

    # Posiciona el boton en el centro de position
    def set_position(self, position):
        self.__position = position
        self.__render()

    def set_text_font(self, font):
        self.__text_font = font
        self.__load_font()
        self.__render()

    def set_font_size(self, size):
        self.__font_size = size
        self.__load_font()
        self.__render()

    def __load_font(self):
        self.__font = pygame.font.Font(self.__text_font, self.__font_size)
        
    def __render(self):
        # Render text
        self.__render_text = self.__font.render(self.__text, True, self.__text_color)

        # Render rect
        self.__rect = self.__render_text.get_rect(center=self.__position)
        self.__rect.inflate_ip(self.__padding, self.__padding) # Agranda el area clickable

