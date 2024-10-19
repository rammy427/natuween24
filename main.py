import game as g
import pygame

# Initialize window.
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# screen is a Surface (to render game onto).
# set_mode returns a Surface.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Judgment Cat")

clock = pygame.time.Clock()

running = True

game = g.Game(screen, screen_rect)
# Main game loop.
while running:
    # Poll for events. Iterate through every event in the queue.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    game.run()

    # Limit framerate.
    clock.tick(FPS)

pygame.quit()