from classes.player.player import Player
from scenes.invisible_road_scene import InvisibleRoadScene
from scenes.keywords_scene import KeywordsScene
from scenes.memory_scene import MemoryScene
from scenes.sequential_numbers_scene import SequentialNumbersScene

if __name__ == "__main__":
    # Create the player
    player = Player()

    # Test games
    # scene = InvisibleRoadScene(player, 2, 2)
    # scene = KeywordsScene(player, 6, 3)
    scene = MemoryScene(player, 4, 3)   
    # scene = SequentialNumbersScene(player, 5, 5, 3)
