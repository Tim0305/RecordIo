import pygame

from player.player import Player
from scenes.menu.menu_scene import MenuScene
from scenes.scene.scene_manager import SceneManager

WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    # Create the player
    player = Player()

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
        scene = scene_manager.get_current_scene()
        if scene != None:
            scene.update(events)

        # call this method to update the screen everytime I have made changes (double buffering)
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(60) # Limit FPS to 60

    pygame.quit()

