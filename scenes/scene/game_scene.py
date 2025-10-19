import pygame
from player.player import Player
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager

class GameScene(Scene):
    def __init__(self, player: Player, screen, manager: SceneManager | None, background_img: str) -> None:
        super().__init__(screen, manager)
        self._player = player

        # Background
        # Convierte la imagen al mismo formato de la pantalla
        self._background = pygame.image.load(background_img).convert()
        self._background = pygame.transform.scale(self._background, self.screen.get_size())

        # Lifes
        self._life_text = "Lifes: "
        self._win_text = "You Won!!!"
        self._game_over_text = "Game Over" 
        self._font_name = "assets/fonts/Jersey15-Regular.ttf"
        self._render_life_text = None
        self._render_win_text = None
        self._render_game_over_text = None

    def draw(self) -> None:
        # Background
        self.screen.blit(self._background, (0, 0))

        # Life text
        self.__update_life_text()

    def __update_life_text(self):
        # Lifes text
        self._life_text = "Lifes: " + str(self._player.get_life())

        # Render text
        font = pygame.font.Font(self._font_name, 60)
        self._render_life_text = font.render(self._life_text, True, (255, 255, 255))

        # Posicionar el texto
        screen_width, _ = self.screen.get_size()
        x = screen_width - (self._render_life_text.get_size()[0] / 2) - 70
        y = 50
        self.screen.blit(self._render_life_text, self._render_life_text.get_rect(center=(x, y)))

    def show_win(self):
        # Render text
        font = pygame.font.Font(self._font_name, 120)
        self._render_win_text = font.render(self._life_text, True, (255, 255, 255))

        # Posicionar el texto
        screen_width, _ = self.screen.get_size()
        x = screen_width - (self._render_life_text.get_size()[0] / 2) - 70
        y = 50
        self.screen.blit(self._render_life_text, self._render_life_text.get_rect(center=(x, y)))

        pass

    def show_game_over(self):
        # Render text
        font = pygame.font.Font(self._font_name, 60)
        self._render_life_text = font.render(self._life_text, True, (255, 255, 255))

        # Posicionar el texto
        screen_width, _ = self.screen.get_size()
        x = screen_width - (self._render_life_text.get_size()[0] / 2) - 70
        y = 50
        self.screen.blit(self._render_life_text, self._render_life_text.get_rect(center=(x, y)))
        pass
