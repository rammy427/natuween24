import pygame

class Enemy:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.__WIDTH = 20
        self.__HEIGHT = 40
        self.__SPEED = 100
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))
        self.__rect.bottomleft = screen_rect.bottomright
        self.__rect.left -= 50
        self.__color = "red"

    def update(self, dt: float) -> None:
        self.__rect.move_ip(-self.__SPEED * dt, 0)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect