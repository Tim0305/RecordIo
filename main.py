import pygame

from player.player import Player
from scenes.menu.menu_scene import MenuScene
from scenes.scene.scene_manager import SceneManager
from util.file import get_game_data

WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    # Create and init the player
    data = get_game_data() # init data
    player = Player(data["wins"], data["fails"])

    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    # Cursor img
    cursor_img = pygame.image.load("assets/cursors/hand_cursor.png")
    # Ocultar el cursor del sistema
    pygame.mouse.set_visible(False)

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

        # Obtener posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Dibujar el cursor en esa posición
        screen.blit(cursor_img, (mouse_x, mouse_y))        
        
        # call this method to update the screen everytime I have made changes (double buffering)
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(60) # Limit FPS to 60

    pygame.quit()

