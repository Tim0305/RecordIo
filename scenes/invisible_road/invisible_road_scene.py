import pygame
import time

from core.games.invisible_road.invisible_road import InvisibleRoadGame
from scenes.invisible_road.block import Block
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.scene.scene import Scene

class InvisibleRoadScene(Scene):
    def __init__(self, player, board_width, board_height, screen, manager = None):
        super().__init__(screen, manager)
        self.player = player
        self.game = InvisibleRoadGame(board_width, board_height)
        self.game.start()
        self.__blocks = []
        self.__block_width = 130
        self.__block_height = 130
        self.__spacing = 5
        self.__show_road_time = 5000 # ms
        self.__show_road_start_time = pygame.time.get_ticks()
        self.__road_visible = True

        # Background
        # Convierte la imagen al mismo formato de la pantalla
        background = pygame.image.load("assets/images/background_wood.png").convert()
        background = pygame.transform.scale(background, self.screen.get_size())
        self.screen.blit(background, (0, 0))

        self.__draw_blocks()
        self.__show_road()

    def handle_events(self, events):
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

        for event in events:
            for i in range(len(self.__blocks)):
                for j in range(len(self.__blocks[i])):
                    if self.__blocks[i][j].is_clicked(event):
                        if self.game.play(j, i):
                            self.__blocks[i][j].set_selected(True)
                            print("Bien")
                        else:
                            self.player.decrement_life()
                            print("Life: " + str(self.player.life))
    
    def draw(self):
        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                self.__blocks[i][j].draw(self.screen)

    def update(self, events):
        if self.__road_visible:
            self.__show_road()

        super().update(events)

    def __draw_blocks(self):
        self.__blocks.clear()

        # Centrar el tablero
        total_blocks_width = self.game.get_board_width() * (self.__block_width + self.__spacing) - self.__spacing
        total_blocks_height = self.game.get_board_height() * (self.__block_height + self.__spacing) - self.__spacing
        screen_width, screen_height = self.screen.get_size()

        # Posicion inicial
        x_start = (screen_width - total_blocks_width + self.__block_width) // 2 
        y_start = (screen_height - total_blocks_height + self.__block_height) // 2 
        
        for i in range(self.game.get_board_height()):
            self.__blocks.append([])

            x = x_start
            y = y_start + i * (self.__block_height + self.__spacing)

            for j in range(self.game.get_board_width()):
                block = Block(self.__block_width, self.__block_height, (x, y))
                x += self.__block_width + self.__spacing
                self.__blocks[i].append(block)

    def __show_road(self):
        road = self.game.get_road()
        if pygame.time.get_ticks() - self.__show_road_start_time < self.__show_road_time:
            # Mostrar el camino
            for i in range(len(road)):
                x, y = road[i]
                self.__blocks[y][x].set_selected(True)
        else:
            # Ocultar el camino
            for i in range(len(road)):
                x, y = road[i]
                self.__blocks[y][x].set_selected(False)

            self.__road_visible = False
