import pygame

class Platform:
    def __init__(self, pos: pygame.Vector2) -> None:
        self.__sprite = pygame.image.load("sprites/platform.png")
        self.__rect = self.__sprite.get_rect()
        self.__rect.center = pos

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect