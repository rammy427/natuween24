import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        # Fill the screen with color to clear previous frame.
        self.screen.fill("black")
        self.update_frame()
        self.render_frame()
        # Flip display to render the new frame.
        pygame.display.flip()

    def update_frame(self):
        pass

    def render_frame(self):
       pass
