# Importar la librería pygame para el control del tiempo dentro del juego
import pygame


'''
Clase que representa un temporizador. Permite medir intervalos de tiempo en milisegundos dentro del juego.
'''
class Timer:
    '''
    Nombre: __init__
    Descripción: Inicializa el temporizador con una duración y tiempo inicial en cero.
    Por defecto, el temporizador no está activo.
    '''
    def __init__(self) -> None:
        self.duration = 0
        self.start_time = 0
        self.active = False

    '''
    Nombre: start
    Parámetros: ms (int)
    Descripción: Inicia el temporizador con una duración específica en milisegundos.
    Guarda el tiempo actual como referencia y activa el estado del temporizador.
    '''
    def start(self, ms: int) -> None:
        self.duration = ms
        self.start_time = pygame.time.get_ticks()
        self.active = True

    '''
    Nombre: is_finished
    Descripción: Verifica si el tiempo del temporizador ha finalizado.
    Si la duración establecida ha transcurrido, el temporizador se desactiva y retorna True. En caso contrario, retorna False.
    '''
    def is_finished(self) -> bool:
        # Si no está activo, retorna False
        if not self.active:
            return False

        current_time = pygame.time.get_ticks()

        # Verifica si el tiempo ha transcurrido
        if current_time - self.start_time >= self.duration:
            self.active = False  # Se desactiva automáticamente al terminar
            return True
        return False

    '''
    Nombre: is_active
    Descripción: Retorna True o False si el temporizador se encuentra activo.
    '''
    def is_active(self) -> bool:
        return self.active
