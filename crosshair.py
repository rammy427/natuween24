import pygame

class Crosshair:
    def __init__(self):
        self.__WIDTH = 20
        self.__HEIGHT = 20
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))

    def update(self, screen_rect):
        self.__rect.center = pygame.mouse.get_pos()
        self.__rect.clamp_ip(screen_rect)

    def draw(self, screen):
        pygame.draw.rect(screen, 'white', self.__rect)

    def getPos(self):
        return self.__rect.center