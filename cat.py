import pygame

class Cat:
    def __init__(self, center):
        self.WIDTH = 96
        self.HEIGHT = 48
        self.SPEED = 500
        self.GRAVITY = 9.8
        self.LAUNCH_SPEED = 4
        self.rect = pygame.Rect(0, 0, self.WIDTH, self.HEIGHT)
        self.rect.center = center
        self.isJumping = False
        self.cur_time = 0

    def update(self, screen_rect, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.move_ip(-self.SPEED * dt, 0)
        if keys[pygame.K_d]:
            self.rect.move_ip(self.SPEED * dt, 0)
        
        if keys[pygame.K_w] and not self.isJumping:
            self.isJumping = True
        
        if self.isJumping:
            self.cur_time += dt
            v = self.LAUNCH_SPEED - self.GRAVITY * self.cur_time
            self.rect.move_ip(0, -v)
        
        self.rect.clamp_ip(screen_rect)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.rect)