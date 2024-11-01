import game as g
import pygame
import asyncio

# Initialize window.
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# screen is a Surface (to render game onto).
# set_mode returns a Surface.
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen_rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
pygame.display.set_caption("Judgment Cat")

running = True

game = g.Game(screen, screen_rect)

# Lock the mouse inside the window.
locked = True
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)

async def main():
    # Main game loop.
    global running, locked
    while running:
        # Poll for events. Iterate through every event in the queue.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    locked = not locked
                    pygame.event.set_grab(locked)
                    pygame.mouse.set_visible(not locked)
                elif event.key == pygame.K_SPACE:
                    game.doCatJump()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.spawn_bullet()

        game.run()
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())