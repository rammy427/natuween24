import crosshair as c
import cat as ct
import bullet as b
import pygame

FPS = 144

class Game:
    def __init__(self, screen, screen_rect):
        self.__clock = pygame.time.Clock()
        self.__screen = screen
        self.__screen_rect = screen_rect
        self.__crosshair = c.Crosshair()
        self.__puma = ct.Cat((screen_rect.centerx, screen_rect.bottom))
        self.__bullets = []

    def run(self):
        # Fill the screen with color to clear previous frame.
        self.__screen.fill("black")
        self.update_frame()
        self.render_frame()
        # Flip display to render the new frame.
        pygame.display.flip()

    def update_frame(self):
        dt = self.__clock.tick(FPS) / 1000
        self.__crosshair.update(self.__screen_rect)
        self.__puma.update(self.__screen_rect, dt)
        for bullet in self.__bullets:
            bullet.update(dt)

    def render_frame(self):
       self.__puma.draw(self.__screen)
       self.__crosshair.draw(self.__screen)
       for bullet in self.__bullets:
           bullet.draw(self.__screen)

    def spawn_bullet(self):
        puma_pos = pygame.Vector2(self.__puma.getPos())
        crosshair_pos = pygame.Vector2(self.__crosshair.getPos())
        dir = pygame.Vector2.normalize(crosshair_pos - puma_pos)
        self.__bullets.append(b.Bullet(puma_pos, dir))