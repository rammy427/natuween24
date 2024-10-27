import pygame

class Enemy:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.__WIDTH = 20
        self.__HEIGHT = 40
        self.__SPEED = 300
        self.__screen_rect = screen_rect
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))
        self.__rect.bottomleft = screen_rect.bottomright
        self.__rect.left -= 50
        self.__color = "red"

    def update(self, dt: float) -> None:
        self.__rect.move_ip(-self.__SPEED * dt, 0)
        # Wrap around the screen.
        if self.__rect.right <= self.__screen_rect.left:
            self.__rect.left = self.__screen_rect.right
        elif self.__rect.left >= self.__screen_rect.right:
            self.__rect.right = self.__screen_rect.left
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect