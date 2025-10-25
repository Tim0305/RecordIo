# Importar la librería pygame para manejar gráficos 2D y eventos
import pygame

'''
Clase que representa un botón visual interactivo en Pygame,
el cual puede mostrar texto, detectar clics y cambiar de color.
'''
class Button:
    '''
    Nombre: __init__
    Parámetros: text (str), position (tuple[int, int])
    Descripción: Inicializa un botón con texto, posición, colores, fuente y efectos de sonido. 
    Configura el rectángulo del botón y prepara su renderizado.
    '''
    def __init__(self, text: str, position: tuple[int, int]) -> None:
        # Colores de fondo, hover, borde, y fuente
        self.__button_color = (215, 121, 10)
        self.__hover_color = (138, 77, 6)
        self.__border_color = (74, 35, 25)
        self.__font_color = (72, 31, 21)

        # Nombre y tamaño de fuente
        self.__font_size = 40
        self.__font_name = "assets/fonts/Jersey15-Regular.ttf"
        self.__font = None

        # Efectos de sonido
        self.__sound_effect = pygame.mixer.Sound("assets/sounds/click_sound.mp3")

        # Configuraciones visuales del botón
        self.__border_radius = 8
        self.__padding = 30
        self.__position = position

        # Texto y rectángulo del botón
        self.__text = text
        self.__rect = pygame.Rect(0, 0, 0, 0)

        self.__load_font()
        self.__render()

    '''
    Nombre: draw
    Parámetros: surface (pygame.Surface)
    Descripción: Dibuja el botón en la superficie indicada. 
    Cambia de color si el cursor está sobre el botón y centra el texto dentro del rectángulo.
    '''
    def draw(self, surface) -> None:
        # Obtener la posición del mouse
        mouse_pos = pygame.mouse.get_pos()
        # El color del botón cambia si el mouse se encuentra sobre el
        color = self.__hover_color if self.__rect.collidepoint(mouse_pos) else self.__button_color

        # Dibujar el rectángulo y borde del botón con un redondeo en las esquinas
        pygame.draw.rect(surface, color, self.__rect, border_radius=self.__border_radius)
        pygame.draw.rect(surface, self.__border_color, self.__rect, width=5, border_radius=self.__border_radius)

        # Actualizar la pantalla
        surface.blit(self.__render_text, self.__render_text.get_rect(center=self.__rect.center))

    '''
    Nombre: is_clicked
    Parámetros: event (pygame.Event)
    Descripción: Verifica si el botón fue presionado con el clic izquierdo. 
    Reproduce un sonido si es así y retorna True, en caso contrario retorna False.
    '''
    def is_clicked(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.__rect.collidepoint(event.pos):
            # Reproducir el sonido
            self.__sound_effect.play()
            return True
        else:
            return False

    '''
    Nombre: get_size
    Descripción: Retorna el tamaño del botón (ancho, alto) como una tupla.
    '''
    def get_size(self) -> tuple[int, int]:
        return self.__rect.size

    '''
    Nombre: get_text
    Descripción: Retorna el texto actual del botón.
    '''
    def get_text(self) -> str:
        return self.__text

    '''
    Nombre: set_text
    Parámetros: text (str)
    Descripción: Cambia el texto del botón y actualiza su renderizado.
    '''
    def set_text(self, text: str) -> None:
        self.__text = text
        self.__render()

    '''
    Nombre: set_position
    Parámetros: position (tuple[int, int])
    Descripción: Establece la nueva posición del botón, centrando el rectángulo en el punto indicado.
    '''
    def set_position(self, position: tuple[int, int]) -> None:
        self.__position = position
        self.__render()

    '''
    Nombre: set_font_name
    Parámetros: font (str)
    Descripción: Cambia el tipo de fuente usada por el botón y vuelve a renderizar el texto.
    '''
    def set_font_name(self, font: str) -> None:
        self.__font_name = font
        self.__load_font()
        self.__render()

    '''
    Nombre: set_font_size
    Parámetros: size (int)
    Descripción: Cambia el tamaño de la fuente del texto del botón y actualiza su renderizado.
    '''
    def set_font_size(self, size: int) -> None:
        self.__font_size = size
        self.__load_font()
        self.__render()

    '''
    Nombre: __load_font
    Descripción: Carga la fuente del texto con el tamaño y nombre configurado.
    '''
    def __load_font(self) -> None:
        self.__font = pygame.font.Font(self.__font_name, self.__font_size)
        
    '''
    Nombre: __render
    Descripción: Renderiza el texto y el rectángulo del botón, ajustando el área clickable con padding.
    '''
    def __render(self) -> None:
        # Renderizar el texto
        self.__render_text = self.__font.render(self.__text, True, self.__font_color)
        # Actualizar el tamaño del rectángulo con el espacio que abarca el texto
        self.__rect = self.__render_text.get_rect(center=self.__position)
        # Agregar un padding al rectángulo
        self.__rect.inflate_ip(self.__padding, self.__padding)
