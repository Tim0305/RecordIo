import pygame

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

class SceneManager():
    def __init__(self):
        self.scene = None

    def go_to(self, scene):
        self.scene = scene
