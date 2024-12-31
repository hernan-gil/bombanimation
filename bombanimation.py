import pygame
import sys

# Inicialización de pygame
pygame.init()

# Configuración de la ventana
SPRITE_WIDTH = 416
SPRITE_HEIGHT = 64
COLUMNS = 13
FRAME_WIDTH = SPRITE_WIDTH // COLUMNS
FRAME_HEIGHT = SPRITE_HEIGHT
SCALE = 256 / FRAME_HEIGHT  # Escala para ajustar la altura a 256 píxeles
SCALED_FRAME_WIDTH = int(FRAME_WIDTH * SCALE)
SCALED_FRAME_HEIGHT = int(FRAME_HEIGHT * SCALE)
WINDOW_SIZE = (SCALED_FRAME_WIDTH, SCALED_FRAME_HEIGHT)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sprite Animation")

# Cargar la imagen del sprite
sprite_sheet = pygame.image.load("BombExploding.png").convert_alpha()

# Configurar variables de la animación
current_frame = 0
last_update_time = pygame.time.get_ticks()
FRAME_DELAY = 1000  # 1 segundo entre frames

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar el frame
    current_time = pygame.time.get_ticks()
    if current_time - last_update_time > FRAME_DELAY:
        last_update_time = current_time
        current_frame = (current_frame + 1) % COLUMNS

    # Dibujar el frame actual
    x_offset = current_frame * FRAME_WIDTH
    frame_rect = pygame.Rect(x_offset, 0, FRAME_WIDTH, FRAME_HEIGHT)
    frame_surface = pygame.Surface((FRAME_WIDTH, FRAME_HEIGHT), pygame.SRCALPHA)
    frame_surface.blit(sprite_sheet, (0, 0), frame_rect)
    scaled_frame = pygame.transform.scale(frame_surface, (SCALED_FRAME_WIDTH, SCALED_FRAME_HEIGHT))
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(scaled_frame, (0, 0))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()
sys.exit()
