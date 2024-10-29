import pygame

class Crosshair:
    def __init__(self) -> None:
        self.__sprite = pygame.image.load("sprites/reticle.png")
        self.__rect = self.__sprite.get_rect()

    def update(self, screen_rect: pygame.Rect) -> None:
        self.__rect.center = pygame.mouse.get_pos()
        self.__rect.clamp_ip(screen_rect)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect)

    def getPos(self) -> pygame.Vector2:
        return self.__rect.center