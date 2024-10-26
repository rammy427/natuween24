import pygame

class Cat:
    def __init__(self, center):
        self.__WIDTH = 96
        self.__HEIGHT = 48
        self.__SPEED = 500
        self.__GRAVITY = 9.8
        self.__LAUNCH_SPEED = 4
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
        self.__isJumping = False
        self.__cur_time = 0

    def update(self, screen_rect, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.__rect.move_ip(-self.__SPEED * dt, 0)
        if keys[pygame.K_d]:
            self.__rect.move_ip(self.__SPEED * dt, 0)
        
        if keys[pygame.K_w] and not self.__isJumping:
            self.__isJumping = True
        
        if self.__isJumping:
            self.__cur_time += dt
            v = self.__LAUNCH_SPEED - self.__GRAVITY * self.__cur_time
            self.__rect.move_ip(0, -v)
            if not screen_rect.contains(self.__rect):
                self.__cur_time = 0
                self.__isJumping = False
        
        self.__rect.clamp_ip(screen_rect)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "yellow", self.__rect)

    def getPos(self):
        return self.__rect.center