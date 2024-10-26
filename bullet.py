import pygame

class Bullet:
    def __init__(self, center, dir):
        self.__WIDTH = 10
        self.__HEIGHT = 10
        self.__SPEED = 1000
        # Direction will be decided at spawn time.
        self.__dir = dir
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
    
    def update(self, dt):
        self.__rect.move_ip(self.__dir * self.__SPEED * dt)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "red", self.__rect)