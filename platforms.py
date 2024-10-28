import pygame

class Platform:
    def __init__(self, pos: pygame.Vector2, width: int) -> None:
        self.__HEIGHT = 10
        self.__rect = pygame.Rect((0, 0), (width, self.__HEIGHT))
        self.__rect.center = pos
        self.__color = "blue"

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect