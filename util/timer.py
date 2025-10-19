import pygame

class Timer:
    def __init__(self) -> None:
        self.duration = 0
        self.start_time = 0
        self.active = False

    def start(self, ms: int) -> None:
        self.duration = ms
        self.start_time = pygame.time.get_ticks()
        self.active = True

    def reset(self) -> None:
        self.active = False
        self.start_time = 0

    def is_finished(self) -> bool:
        if not self.active:
            return False

        current_time = pygame.time.get_ticks()

        if current_time - self.start_time >= self.duration:
            self.active = False  # Se desactiva automáticamente
            return True
        return False
    
    def is_active(self) -> bool:
        return self.active
