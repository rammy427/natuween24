import crosshair as c
import cat as ct
import bullet as b
import pygame

FPS = 144

class Game:
    def __init__(self, screen, screen_rect):
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screen_rect = screen_rect
        self.crosshair = c.Crosshair(screen_rect.center)
        self.puma = ct.Cat((screen_rect.centerx, screen_rect.bottom - 100))
        self.bullets = []

    def run(self):
        # Fill the screen with color to clear previous frame.
        self.screen.fill("black")
        self.update_frame()
        self.render_frame()
        # Flip display to render the new frame.
        pygame.display.flip()

    def update_frame(self):
        dt = self.clock.tick(FPS) / 1000
        self.crosshair.update(self.screen_rect)
        self.puma.update(self.screen_rect, dt)
        for bullet in self.bullets:
            bullet.update(dt)

    def render_frame(self):
       self.puma.draw(self.screen)
       self.crosshair.draw(self.screen)
       for bullet in self.bullets:
           bullet.draw(self.screen)

    def spawn_bullet(self):
        puma_pos = pygame.Vector2(self.puma.rect.centerx, self.puma.rect.centery)
        crosshair_pos = pygame.Vector2(self.crosshair.rect.centerx, self.crosshair.rect.centery)
        dir = pygame.Vector2.normalize(crosshair_pos - puma_pos)
        self.bullets.append(b.Bullet(puma_pos, dir))