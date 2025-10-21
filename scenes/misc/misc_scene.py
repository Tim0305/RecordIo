from typing import override
import random
from player.player import Player
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.keywords.keywords_scene import KeywordsScene
from scenes.scene.scene import Scene
from scenes.scene.scene_manager import SceneManager
from scenes.sequential_numbers.sequential_numbers_scene import SequentialNumbersScene

class MiscScene(Scene):
    def __init__(self, player: Player, screen, manager: SceneManager | None = None) -> None:
        super().__init__(screen, manager)
        self.__player = player
        self.__opcion = random.randint(0, 2)
        self.__is_playing = True

    @override
    def update(self, events) -> None:
        super().update(events)
        if self.manager != None:
            if self.__is_playing:
                self.__is_playing = False
                if self.__opcion == 0:
                    self.manager.go_to(InvisibleRoadScene(self.__player, 5, 5, self.screen, self.manager))              
                elif self.__opcion == 1:
                    self.manager.go_to(KeywordsScene(self.__player, 6, 3, self.screen, self.manager))                    
                elif self.__opcion == 2:
                    self.manager.go_to(SequentialNumbersScene(self.__player, 5, 5, 8, self.screen, self.manager))
            else:
                self.manager.go_back()
