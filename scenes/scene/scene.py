class Scene():
    def __init__(self, screen, manager = None):
        self.manager = manager
        self.screen = screen

    def set_manager(self, manager):
        self.manager = manager

    def set_screen(self, screen):
        self.screen = screen 

    def handle_events(self, events):
        pass

    def draw(self):
        pass

    def update(self, events):
        self.draw()
        self.handle_events(events)

class SceneManager():
    def __init__(self):
        self.scene_stack = []
        self.current_scene = None

    def go_to(self, scene):
        self.scene_stack.append(self.current_scene)
        self.current_scene = scene

    def go_back(self):
        self.current_scene = self.scene_stack.pop()

    def get_current_scene(self):
        return self.current_scene
