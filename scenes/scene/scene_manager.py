from scenes.scene.scene import Scene

class SceneManager():
    def __init__(self) -> None:
        self.scene_stack = []
        self.current_scene = None

    def go_to(self, scene: Scene) -> None:
        self.scene_stack.append(self.current_scene)
        self.current_scene = scene

    def go_back(self) -> None:
        self.current_scene = self.scene_stack.pop()

    def get_current_scene(self) -> Scene | None:
        return self.current_scene

