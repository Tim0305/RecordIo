# Importar la clase Scene
from scenes.scene.scene import Scene

'''
Clase que administra el flujo entre escenas.
Permite cambiar a nuevas escenas, regresar a anteriores y obtener la escena actual.
'''
class SceneManager():
    '''
    Nombre: __init__
    Descripción: Inicializa el administrador con una pila vacía de escenas 
    y una escena actual nula.
    '''
    def __init__(self) -> None:
        self.scene_stack = []  # Guarda las escenas anteriores
        self.current_scene = None  # Escena actual activa

    '''
    Nombre: go_to
    Parámetros: scene (Scene)
    Descripción: Cambia a una nueva escena, guardando la escena actual en la pila.
    '''
    def go_to(self, scene: Scene) -> None:
        self.scene_stack.append(self.current_scene) # Agrega la escena actual a la pila
        self.current_scene = scene # Cambia la escena actual

    '''
    Nombre: go_back
    Descripción: Regresa a la escena anterior sacándola de la pila de escenas.
    '''
    def go_back(self) -> None:
        self.current_scene = self.scene_stack.pop()

    '''
    Nombre: get_current_scene
    Descripción: Retorna la escena actual activa. Si no hay una escena actual, retorna None.
    '''
    def get_current_scene(self) -> Scene | None:
        return self.current_scene