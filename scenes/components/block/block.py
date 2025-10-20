import pygame


class Block:
    def __init__(
        self,
        width: int,
        height: int,
        position: tuple[int, int],
        text: str = "",
        border_radius: int = 50,
        selected_color: tuple[int, int, int] = (66, 135, 245),
        unselected_color: tuple[int, int, int] = (200, 200, 200),
        hover_color: tuple[int, int, int] = (21, 102, 232),
    ) -> None:
        self.__selected_color = selected_color
        self.__unselected_color = unselected_color
        self.__hover_color = hover_color
        self.__border_radius = border_radius
        self.__is_selected = False
        self.__enabled = True

        # El bloque usa el centro para posicionarse
        self.__rect = pygame.rect.Rect(0, 0, 0, 0)
        self.__init_rect(width, height, position)

        # Texto
        self.__font = pygame.font.Font(
            "assets/fonts/Jersey15-Regular.ttf", int(height * 0.6)
        )  # Tamano al 60% de la altura
        self.__render_text = None
        self.__init_text(text)

    def draw(self, surface) -> None:
        # Hover
        mouse_pos = pygame.mouse.get_pos()

        color = self.__unselected_color

        if self.__is_selected:
            color = self.__selected_color
        elif self.__enabled and self.__rect.collidepoint(mouse_pos):
            color = self.__hover_color

        # Dibujar el bloque
        pygame.draw.rect(
            surface, color, self.__rect, border_radius=self.__border_radius
        )

        # Dibujar el texto
        surface.blit(
            self.__render_text, self.__render_text.get_rect(center=self.__rect.center)
        )

    def is_clicked(self, event) -> bool:
        return (
            self.__enabled
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.__rect.collidepoint(event.pos)
        )

    def set_selected(self, selected: bool) -> None:
        self.__is_selected = selected

    def enable(self) -> None:
        self.__enabled = True

    def disable(self) -> None:
        self.__enabled = False

    def __init_rect(self, width: int, height: int, position: tuple[int, int]) -> None:
        self.__rect = pygame.Rect(0, 0, width, height)
        self.__rect.center = position

    def __init_text(self, text) -> None:
        self.__render_text = self.__font.render(text, True, (255, 255, 255))
        self.__render_text

    def set_text(self, text: str) -> None:
        self.__init_text(text)
