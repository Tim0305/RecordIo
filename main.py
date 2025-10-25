# Importar las librerías necesarias para el manejo de gráficos, escenas y guardado de la información
import pygame
from player.player import Player
from scenes.menu.menu_scene import MenuScene
from scenes.scene.scene_manager import SceneManager
from util.file import get_game_data

# Tamaño de la pantalla
WIDTH = 1280
HEIGHT = 720

if __name__ == "__main__":
    # Crear e inicializar el jugador con la información de data.txt
    data = get_game_data()
    player = Player(data["wins"], data["fails"])

    # Configuración de pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Pantalla
    clock = pygame.time.Clock()
    
    # Bandera que indica si el juego se está ejecutando o no
    running = True

    # Imagen del cursor
    cursor_img = pygame.image.load("assets/cursors/hand_cursor.png")
    
    # Ocultar el cursor del sistema
    pygame.mouse.set_visible(False)

    # Scene manager
    scene_manager = SceneManager()
    # Ir al menú principal
    scene_manager.go_to(MenuScene(player, screen, scene_manager))

    # Ciclo principal
    while running:
        # Pygame events
        events = pygame.event.get()
        for event in events:
            # Terminar el programa cuando se cierra la ventana
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE
        scene = scene_manager.get_current_scene() # Obtener la escena actual
        if scene != None:
            scene.update(events) # Actualizar la escena

        # Obtener la posición del mouse
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Dibujar el cursor personalizado en esa posición
        screen.blit(cursor_img, (mouse_x, mouse_y))        
        
        # Actualizar la pantalla
        pygame.display.flip()
        # pygame.display.update()
        clock.tick(60) # Limit FPS to 60

    # Terminar el programa
    pygame.quit()

