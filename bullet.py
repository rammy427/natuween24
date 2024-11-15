import animation as a
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
        self.__animation = a.Animation(self.__HEIGHT, 4, 0.03125, "sprites/laser.png")
    
    def update(self, dt: float) -> None:
        self.__rect.move_ip(self.__DIR * self.__SPEED * dt)
        self.__animation.update(dt)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.__animation.draw(self.__rect, screen)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect