import pygame
import random

class Enemy:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.__WIDTH = 20
        self.__HEIGHT = 40
        self.__SPEED = 300
        self.__screen_rect = screen_rect
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))
        self.__color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Randomly choose position and direction.
        head_right = random.choice([True, False])
        if head_right:
            self.__x_dir = 1
            self.__rect.bottomright = screen_rect.bottomleft
        else:
            self.__x_dir = -1
            self.__rect.bottomleft = screen_rect.bottomright

    def update(self, dt: float) -> None:
        self.__rect.move_ip(self.__x_dir * self.__SPEED * dt, 0)
        # Wrap around the screen.
        if self.__rect.right <= self.__screen_rect.left:
            self.__rect.left = self.__screen_rect.right
        elif self.__rect.left >= self.__screen_rect.right:
            self.__rect.right = self.__screen_rect.left
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)
    
    def getRect(self) -> pygame.Rect:
        return self.__rect