import pygame
import cat as c

class HealthBar:
    def __init__(self, cat: c.Cat) -> None:
        self.__cat = cat
        # Face sprite info.
        self.__face_sprite = pygame.image.load("sprites/whiskers.png")
        self.__face_rect = self.__face_sprite.get_rect()
        self.__N_FACE_FRAMES = 2
        self.__face_frame_width = self.__face_rect.size[0] // self.__N_FACE_FRAMES
        self.__face_frame_height = self.__face_rect.size[1]
        self.__face_crop_rect = pygame.Rect(0, 0, self.__face_frame_width, self.__face_frame_height)
        # HP bar sprite info.
        self.__hp_sprite = pygame.image.load("sprites/lifebar.png")
        self.__hp_rect = self.__hp_sprite.get_rect()
        self.__hp_rect.left = self.__face_crop_rect.right
        self.__N_HP_FRAMES = 10
        self.__hp_frame_width = self.__hp_rect.size[0] // 10
        self.__hp_frame_height = self.__hp_rect.size[1]
        self.__hp_crop_rect = pygame.Rect(0, 0, self.__hp_frame_width, self.__hp_frame_height)

    def update(self):
        # Update HP bar.
        hp = self.__cat.getHP()
        self.__hp_crop_rect.left = (self.__N_HP_FRAMES - hp - 1) * self.__hp_frame_width
        # Update face.
        index = int(self.__cat.isInvincible())
        self.__face_crop_rect.left = index * self.__face_frame_width

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__hp_sprite, self.__hp_rect, self.__hp_crop_rect)
        screen.blit(self.__face_sprite, self.__face_rect, self.__face_crop_rect)