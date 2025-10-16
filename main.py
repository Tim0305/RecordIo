import pygame

from classes.player.player import Player
from scenes.invisible_road.invisible_road_scene import InvisibleRoadScene
from scenes.menu.menu_scene import MenuScene
from scenes.scene.scene import SceneManager

WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    # Create the player
    player = Player()

    # Test games
    # scene = InvisibleRoadScene(player, 2, 2)
    # scene = KeywordsScene(player, 6, 3)
    # scene = MemoryScene(player, 4, 3)   
    # scene = SequentialNumbersScene(player, 5, 5, 3)

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # Scene manager
    scene_manager = SceneManager()
    scene_manager.go_to(MenuScene(player, screen, scene_manager))

    while running:
        # Pygame events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE
        scene_manager.get_current_scene().handle_events(events)
        scene_manager.get_current_scene().draw()

        # call this method to update the screen everytime I have made changes (double buffering)
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(60) # Limit FPS to 60

    pygame.quit()

