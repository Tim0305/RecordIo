from typing import override

import pygame
from core.games.keywords.keywords import KeywordsGame
from player.player import Player
from scenes.scene.game_scene import GameScene
from scenes.scene.scene_manager import SceneManager
from util.timer import Timer

class KeywordsScene(GameScene):
    def __init__(self, player: Player, length: int, n: int, screen, manager: SceneManager | None = None) -> None:
        super().__init__(player, screen, manager, "assets/images/background_4.png")
        self.game = KeywordsGame(length, n)
        self.game.start()
        self.__number_of_keywords = n
        self.__show_keyword_time = 3000 # ms
        self.__is_writing = False
        self.__user_input_text = ""
        self.__font_name = "assets/fonts/Jersey15-Regular.ttf"
        self.__timer = Timer()

    @override
    def handle_events(self, events):
        super().handle_events(events)
        if self._player.get_life() == 0:
            self.show_game_over()
            if self.manager != None:
                self.manager.go_back()
        elif self.game.is_over():
            self.show_win()
            if self.manager != None:
                self.manager.go_back()
        else:
            for event in events:
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        # Borrar el último caracter
                        self.__user_input_text = self.__user_input_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        # Jugar solo si el texto ingresado tenga caracteres
                        if len(self.__user_input_text) != 0:
                            # Jugar
                            if not self.game.play(self.__user_input_text):
                                self._player.decrement_life()

                            # Limpiar la entrada
                            self.__user_input_text = ""
                            # El usuario no esta escribiendo
                            self.__is_writing = False
                    else:
                        # Agregar la letra presionada si is_writing es true respetando el tamano del keyword
                        if self.__is_writing and len(self.__user_input_text) < self.game.get_keyword_length():
                            self.__user_input_text += event.unicode

    @override
    def draw(self) -> None:
        super().draw()
        if not self.game.is_over():
            if not self.__is_writing:
                # mostrar la clave
                self.__draw_keyword(self.game.get_current_keyword())

                if not self.__timer.is_active():
                    self.__timer.start(self.__show_keyword_time)

                if self.__timer.is_finished():
                    # El jugador debe ingresar la palabra
                    self.__is_writing = True
            else:
                self.__draw_text_area(self.__user_input_text)

    def __draw_keyword(self, keyword: str) -> None:
        font = pygame.font.Font(self.__font_name, 120)
        render_text = font.render(keyword, True, (255, 255, 255))
        
        screen_width, screen_height = self.screen.get_size()

        # Rect
        text_width, text_height = render_text.get_size()
        rect = pygame.Rect(0, 0, text_width, text_height)
        rect.center = (screen_width / 2, screen_height * 0.2)
        rect.inflate_ip(100, 60)
        
        # Mostrar el rect y el texto
        pygame.draw.rect(self.screen, (100, 100, 100), rect, border_radius=50)
        self.screen.blit(render_text, render_text.get_rect(center=rect.center))

    def __draw_text_area(self, text: str):
        font = pygame.font.Font(self.__font_name, 100)
        text_area = font.render(text, True, (255, 255, 255))
        
        screen_width, screen_height = self.screen.get_size()

        # Rect
        text_area_width, _ = text_area.get_size()
        rect = pygame.Rect(0, 0, text_area_width + 50, 10)
        rect.center = (screen_width / 2, (screen_height / 2) + 150)
        
        # Mostrar el rect y el texto
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        self.screen.blit(text_area, text_area.get_rect(center=(screen_width / 2, (screen_height / 2) + 70)))
