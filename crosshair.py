import pygame

class Crosshair:
    def __init__(self) -> None:
        self.__WIDTH = 20
        self.__HEIGHT = 20
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))

    def update(self, screen_rect: pygame.Rect) -> None:
        self.__rect.center = pygame.mouse.get_pos()
        self.__rect.clamp_ip(screen_rect)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, 'white', self.__rect)

    def getPos(self) -> pygame.Vector2:
        return self.__rect.center