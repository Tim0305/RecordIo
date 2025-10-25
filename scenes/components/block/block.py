# Importar pygame para manejar gráficos 2D y eventos
import pygame

'''
Clase que representa un bloque visual interactivo en Pygame,
el cual puede mostrar texto, detectar clics y cambiar de color
dependiendo de su estado (seleccionado, deshabilitado o en hover).
'''
class Block:
    '''
    Nombre: __init__
    Parámetros: 
        width (int), height (int), position (tuple[int, int]), 
        text (str, opcional), border_radius (int, opcional),
        selected_color (tuple[int, int, int], opcional),
        unselected_color (tuple[int, int, int], opcional),
        hover_color (tuple[int, int, int], opcional)
    Descripción: Inicializa el bloque con sus propiedades visuales y de interacción.
    '''
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
        # Colores
        self.__selected_color = selected_color
        self.__unselected_color = unselected_color
        self.__hover_color = hover_color
        
        # Borde redondeado
        self.__border_radius = border_radius
        
        # Banderas que indican si el bloque esta selccionado o no, y si está habilitado o no
        self.__is_selected = False
        self.__enabled = True

        # Se inicializa el rectángulo que define la posición y tamaño del bloque
        self.__rect = pygame.rect.Rect(0, 0, 0, 0)
        self.__init_rect(width, height, position)

        # Configuración del texto a mostrar dentro del bloque
        self.__font = pygame.font.Font(
            "assets/fonts/Jersey15-Regular.ttf", int(height * 0.6)
        )  # Tamaño del texto: 60% de la altura del bloque
        self.__render_text = None
        self.__init_text(text)

    '''
    Nombre: draw
    Parámetros: surface (pygame.Surface)
    Descripción: Dibuja el bloque en pantalla con el color y texto correspondientes.
    '''
    def draw(self, surface) -> None:
        # Obtiene la posición actual del mouse
        mouse_pos = pygame.mouse.get_pos()
        color = self.__unselected_color

        # Determina el color según el estado actual del bloque
        if self.__is_selected:
            color = self.__selected_color
        elif self.__enabled and self.__rect.collidepoint(mouse_pos):
            # Color cuando el mouse hace hover
            color = self.__hover_color

        # Dibuja el rectángulo del bloque
        pygame.draw.rect(surface, color, self.__rect, border_radius=self.__border_radius)

        # Dibuja el texto centrado dentro del bloque
        surface.blit(
            self.__render_text, self.__render_text.get_rect(center=self.__rect.center)
        )

    '''
    Nombre: is_clicked
    Parámetros: event (pygame.Event)
    Descripción: Verifica si el bloque fue clicado con el botón izquierdo del mouse.
    '''
    def is_clicked(self, event) -> bool:
        # Retorna True si el bloque está habilitado y fue clicado
        return (
            self.__enabled
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.__rect.collidepoint(event.pos)
        )

    '''
    Nombre: set_selected
    Parámetros: selected (bool)
    Descripción: Cambia el estado del bloque a seleccionado o no seleccionado.
    '''
    def set_selected(self, selected: bool) -> None:
        self.__is_selected = selected

    '''
    Nombre: enable
    Descripción: Habilita la interacción con el bloque.
    '''
    def enable(self) -> None:
        # Permite que el bloque responda a eventos de usuario
        self.__enabled = True

    '''
    Nombre: disable
    Descripción: Deshabilita la interacción con el bloque.
    '''
    def disable(self) -> None:
        # Desactiva la interacción del bloque
        self.__enabled = False

    '''
    Nombre: __init_rect
    Parámetros: width (int), height (int), position (tuple[int, int])
    Descripción: Inicializa el rectángulo del bloque y lo posiciona en el centro indicado.
    '''
    def __init_rect(self, width: int, height: int, position: tuple[int, int]) -> None:
        # Crea el rectángulo del bloque y lo centra en la posición dada
        self.__rect = pygame.Rect(0, 0, width, height)
        self.__rect.center = position

    '''
    Nombre: __init_text
    Parámetros: text (str)
    Descripción: Genera el texto renderizado que se mostrará en el bloque.
    '''
    def __init_text(self, text) -> None:
        # Renderiza el texto con color blanco
        self.__render_text = self.__font.render(text, True, (255, 255, 255))

    '''
    Nombre: set_text
    Parámetros: text (str)
    Descripción: Actualiza el texto que se muestra dentro del bloque.
    '''
    def set_text(self, text: str) -> None:
        # Redibuja el texto con el nuevo valor
        self.__init_text(text)
