import pygame
import cat as c

class HealthBar:
    def __init__(self, cat: c.Cat) -> None:
        self.__cat = cat
        self.__sprite = pygame.image.load("sprites/lifebar.png")
        self.__rect = self.__sprite.get_rect()
        self.__N_FRAMES = 10
        self.__frame_width = self.__rect.size[0] // 10
        self.__frame_height = self.__rect.size[1]
        self.__crop_rect = pygame.Rect(0, 0, self.__frame_width, self.__frame_height)

    def update(self):
        hp = self.__cat.getHP()
        self.__crop_rect.left = (self.__N_FRAMES - hp - 1) * self.__frame_width

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect, self.__crop_rect)