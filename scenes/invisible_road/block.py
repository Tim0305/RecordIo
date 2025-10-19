import pygame

class Block:
    def __init__(self, width: int, height: int, position: tuple[int, int]) -> None:
        self.__selected_color = (66, 135, 245)
        self.__unselected_color = (200, 200, 200)
        self.__hover_color = (21, 102, 232)
        self.__position = position
        self.__width = width
        self.__height = height
        self.__border_radius = 50
        self.__is_selected = False
        self.__enabled = True
        # El bloque usa el centro para posicionarse
        self.__rect = pygame.Rect(0, 0, width, height)
        self.__rect.center = position

    def draw(self, surface) -> None:
        # Hover
        mouse_pos = pygame.mouse.get_pos()

        color = self.__unselected_color

        if self.__is_selected:
            color = self.__selected_color
        elif self.__enabled and self.__rect.collidepoint(mouse_pos):
            color = self.__hover_color

        # Dibujar el bloque
        pygame.draw.rect(surface, color, self.__rect, border_radius=self.__border_radius)

    def is_clicked(self, event) -> bool:
        return self.__enabled and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.__rect.collidepoint(event.pos)

    def set_selected(self, selected: bool) -> None:
        self.__is_selected = selected

    def enable(self) -> None:
        self.__enabled = True

    def disable(self) -> None:
        self.__enabled = False
