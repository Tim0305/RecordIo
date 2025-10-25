'''
Clase base que representa una escena del juego.
Define la estructura general que deben seguir las escenas, 
incluyendo la gestión de eventos, el dibujo y la actualización.
'''
class Scene:
    '''
    Nombre: __init__
    Parámetros: screen (pygame.Surface), manager (SceneManager | None)
    Descripción: Inicializa la escena asignándole una pantalla y, opcionalmente, un administrador de escenas.
    '''
    def __init__(self, screen, manager = None) -> None:
        self.manager = manager
        self.screen = screen

    '''
    Nombre: set_manager
    Parámetros: manager (SceneManager)
    Descripción: Asigna un nuevo administrador de escenas a la escena actual.
    '''
    def set_manager(self, manager) -> None:
        self.manager = manager

    '''
    Nombre: set_screen
    Parámetros: screen (pygame.Surface)
    Descripción: Cambia la superficie donde se dibuja la escena.
    '''
    def set_screen(self, screen) -> None:
        self.screen = screen 

    '''
    Nombre: handle_events
    Parámetros: events (list[pygame.Event])
    Descripción: Método que debe ser implementado por las subclases para manejar eventos del usuario (teclado, ratón, etc.).
    '''
    def handle_events(self, events) -> None: 
        ...

    '''
    Nombre: draw
    Descripción: Método que debe ser implementado por las subclases para dibujar los elementos visuales de la escena.
    '''
    def draw(self) -> None: 
        ...

    '''
    Nombre: update
    Parámetros: events (list[pygame.Event])
    Descripción: Actualiza el estado de la escena. Por defecto, llama a draw() y handle_events().
    '''
    def update(self, events) -> None:
        self.draw()
        self.handle_events(events)
