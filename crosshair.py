import pygame

class Crosshair:
    def __init__(self, pos):
        self.pos = pos
        self.WIDTH = 30
        self.HEIGHT = 30
        self.rect = pygame.Rect(pos, (self.WIDTH, self.HEIGHT))

    def update(self, screen_rect):
        self.rect.center = pygame.mouse.get_pos()
        self.rect.clamp_ip(screen_rect)

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.rect)