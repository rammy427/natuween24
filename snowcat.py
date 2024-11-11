import pygame
import random

class Snowcat:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.__WIDTH = 100
        self.__HEIGHT = 100
        self.__SPEED = 100
        self.__SPAWN_TIME = 30
        self.__screen_rect = screen_rect
        self.__cur_time = 0.0
        self.__sprite = pygame.image.load("sprites/snowcat.png")
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.spawn()

    def update(self, dt: float) -> None:
        self.__cur_time += dt
        if (self.__cur_time >= self.__SPAWN_TIME):
            self.spawn()
        
        if self.__rect.top < self.__screen_rect.bottom:
            self.__rect.move_ip(0, self.__SPEED * dt)

    def spawn(self):
        index = random.randint(0, 9)
        self.__clip_rect = pygame.Rect(index * self.__WIDTH, 0, self.__WIDTH, self.__HEIGHT)
        LEFT = self.__screen_rect.left + self.__WIDTH // 2
        RIGHT = self.__screen_rect.right - self.__WIDTH // 2
        x = random.randint(LEFT, RIGHT)
        y = -self.__HEIGHT // 2
        self.__rect.center = pygame.Vector2(x, y)
        self.__cur_time = 0.0
        print("Index: %s" % index)
        print("Position: (%s, %s)" % (x, y))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, self.__rect, self.__clip_rect)