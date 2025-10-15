import pygame

from core.games.invisible_road.invisible_road import InvisibleRoadGame
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.scene.scene import Scene

class InvisibleRoadScene(Scene):
    def __init__(self, player, board_width, board_height, screen, manager = None):
        super().__init__(screen, manager)
        self.player = player
        self.game = InvisibleRoadGame(board_width, board_height)
        self.game.start()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.manager.go_to(KeywordsScene(self.player, 6, 3, self.screen, self.manager))

        # while True:
        #     if player.life == 0:
        #         print("Game Over")
        #         break
        #     elif self.game.is_over():
        #         print("You won!!!")
        #         break
        #     else:
        #         self.game.print_board()
        #         x = int(input("X: "))
        #         y = int(input("Y: "))
        #
        #         if self.game.play(x, y):
        #             print("Bien")
        #         else:
        #             player.decrement_life()
        #             print("Life: " + str(player.life))
        pass

    def draw(self):
        self.screen.fill("red")

