import pygame

class Bullet:
    def __init__(self, center: pygame.Vector2, dir: pygame.Vector2) -> None:
        self.__WIDTH = 10
        self.__HEIGHT = 10
        self.__SPEED = 1000
        # Direction will be decided at spawn time.
        self.__DIR = dir
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
    
    def update(self, dt: float) -> None:
        self.__rect.move_ip(self.__DIR * self.__SPEED * dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "red", self.__rect)