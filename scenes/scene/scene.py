class Scene:
    def __init__(self, screen, manager = None) -> None:
        self.manager = manager
        self.screen = screen

    def set_manager(self, manager) -> None:
        self.manager = manager

    def set_screen(self, screen) -> None:
        self.screen = screen 

    def handle_events(self, events) -> None: ...

    def draw(self) -> None: ...

    def update(self, events) -> None:
        self.draw()
        self.handle_events(events)
