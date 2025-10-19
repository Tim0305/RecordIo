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
        self._pixel_font_name = "assets/fonts/Jersey15-Regular.ttf"
        self._arcade_font_name = "assets/fonts/ka1.ttf"
        self.__show_message_time = 3000 # ms

    def draw(self) -> None:
        # Background
        self.screen.blit(self._background, (0, 0))

        # Life text
        self.__update_life_text()

    def __update_life_text(self) -> None:
        # Lifes text
        text = "Lifes: " + str(self._player.get_life())

        # Render text
        font = pygame.font.Font(self._pixel_font_name, 80)
        life_text = font.render(text, True, (255, 255, 255))

        # Posicionar el texto
        screen_width, _ = self.screen.get_size()
        x = screen_width - (life_text.get_size()[0] / 2) - 50
        y = 50
        self.screen.blit(life_text, life_text.get_rect(center=(x, y)))

    def show_win(self) -> None:
        self.__show_message("You Won", (0, 0, 0), (217, 219, 145))

    def show_game_over(self):
        self.__show_message("Game Over", (218, 223, 242), (46, 75, 179))

    def __show_message(self, message: str, font_color: tuple[int, int, int], bg_color: tuple[int, int, int]) -> None:
        # Render text
        font = pygame.font.Font(self._arcade_font_name, 120)
        game_over_text = font.render(message, True, font_color)

        screen_width, screen_height = self.screen.get_size()

        # Rect
        text_width, text_height = game_over_text.get_size()
        rect = pygame.Rect(0, 0, text_width, text_height)
        rect.center = (screen_width / 2, screen_height / 2)
        rect.inflate_ip(60, 60) # Agranda el rect

        # Mostrar el rext y texto
        pygame.draw.rect(self.screen, bg_color, rect, border_radius=50)
        self.screen.blit(game_over_text, game_over_text.get_rect(center=(screen_width / 2, screen_height / 2)))

        # Esperar un tiempo
        pygame.display.flip() # Actualizar la ventana
        pygame.time.delay(self.__show_message_time)

