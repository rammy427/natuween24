import pygame

class Cat:
    def __init__(self, center):
        self.WIDTH = 96
        self.HEIGHT = 48
        self.SPEED = 5
        self.rect = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        self.rect.center = center

    def update(self, screen_rect):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.SPEED, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.SPEED, 0)
        
        self.rect.clamp_ip(screen_rect)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.rect)