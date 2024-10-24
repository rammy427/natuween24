import pygame

class Bullet:
    def __init__(self, center, dir):
        self.WIDTH = 10
        self.HEIGHT = 10
        self.SPEED = 1000
        # Direction will be decided at spawn time.
        self.dir = dir
        self.rect = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        self.rect.center = center
    
    def update(self, dt):
        self.rect.move_ip(self.dir * self.SPEED * dt)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.rect)