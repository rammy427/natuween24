import crosshair as c
import cat as ct
import pygame

class Game:
    def __init__(self, screen, screen_rect):
        self.screen = screen
        self.screen_rect = screen_rect
        self.crosshair = c.Crosshair(screen_rect.center)
        self.puma = ct.Cat((screen_rect.centerx, screen_rect.bottom - 100))

    def run(self):
        # Fill the screen with color to clear previous frame.
        self.screen.fill("black")
        self.update_frame()
        self.render_frame()
        # Flip display to render the new frame.
        pygame.display.flip()

    def update_frame(self):
        self.crosshair.update(self.screen_rect)
        self.puma.update(self.screen_rect)

    def render_frame(self):
       self.puma.draw(self.screen)
       self.crosshair.draw(self.screen)
