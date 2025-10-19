from typing import override
import pygame

from core.games.invisible_road.invisible_road import InvisibleRoadGame
from player.player import Player
from scenes.invisible_road.block import Block
from scenes.scene.game_scene import GameScene
from scenes.scene.scene_manager import SceneManager

class InvisibleRoadScene(GameScene):
    def __init__(self, player: Player, board_width: int, board_height: int, screen, manager: SceneManager | None = None) -> None:
        super().__init__(player, screen, manager, "assets/images/background_wood.png")
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
        self.__draw_blocks()
        self.__show_road()

    @override
    def handle_events(self, events) -> None:
        if self.player.get_life() == 0:
            self.show_game_over()
            if self.manager != None:
                self.manager.go_back()
        elif self.game.is_over():
            self.show_win()
            if self.manager != None:
                self.manager.go_back()
        else:
            for event in events:
                for i in range(len(self.__blocks)):
                    for j in range(len(self.__blocks[i])):
                        if self.__blocks[i][j].is_clicked(event):
                            if self.game.play(j, i):
                                self.__blocks[i][j].set_selected(True)
                            else:
                                self.player.decrement_life()
                                print("Life: " + str(self.player.get_life()))
        
    @override
    def draw(self) -> None:
        super().draw()

        for i in range(len(self.__blocks)):
            for j in range(len(self.__blocks[i])):
                self.__blocks[i][j].draw(self.screen)

    @override
    def update(self, events) -> None:
        if self.__road_visible:
            self.__show_road()

        super().update(events)

    def __draw_blocks(self) -> None:
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

    def __show_road(self) -> None:
        road = self.game.get_road()
        if pygame.time.get_ticks() - self.__show_road_start_time < self.__show_road_time:
            # Deshabilitar todos los bloques
            for i in range(len(self.__blocks)):
                for j in range(len(self.__blocks[i])):
                    self.__blocks[i][j].disable()

            # Mostrar el camino
            for i in range(len(road)):
                x, y = road[i]
                self.__blocks[y][x].set_selected(True)
        else:
            # Deshabilitar todos los bloques
            for i in range(len(self.__blocks)):
                for j in range(len(self.__blocks[i])):
                    self.__blocks[i][j].enable()

            # Ocultar el camino
            for i in range(len(road)):
                x, y = road[i]
                self.__blocks[y][x].set_selected(False)

            self.__road_visible = False
