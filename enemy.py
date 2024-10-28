import pygame
import random
import platforms as p

class Enemy:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.__MAX_HP = 3
        self.__WIDTH = 20
        self.__HEIGHT = 40
        self.__SPEED = 500
        self.__GRAVITY = 9.8
        self.__hp = self.__MAX_HP
        self.__screen_rect = screen_rect
        self.__rect = pygame.Rect((0, 0), (self.__WIDTH, self.__HEIGHT))
        self.__color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.__fall_speed = 0

        # Randomly choose position and direction.
        head_right = random.choice([True, False])
        if head_right:
            self.__x_dir = 1
            # self.__rect.bottomright = screen_rect.bottomleft
        else:
            self.__x_dir = -1
            # self.__rect.bottomleft = screen_rect.bottomright
        self.__rect.center = (random.randint(0, screen_rect.width), random.randint(0, screen_rect.height))

    def update(self, screen_rect: pygame.Rect, platforms: set[p.Platform], dt: float) -> None:
        self.__rect.move_ip(self.__x_dir * self.__SPEED * dt, 0)

        self.__fall(dt)
        self.__lockToGround(screen_rect, platforms)

        # Wrap around the screen.
        if self.__rect.right <= self.__screen_rect.left:
            self.__rect.left = self.__screen_rect.right
        elif self.__rect.left >= self.__screen_rect.right:
            self.__rect.right = self.__screen_rect.left
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.__color, self.__rect)
    
    def takeDamage(self) -> None:
        self.__hp -= 1
        print("Enemy life: %s." % self.__hp)

    def isAlive(self) -> bool:
        return self.__hp > 0
    
    def getRect(self) -> pygame.Rect:
        return self.__rect
    
    def __fall(self, dt: float) -> None:
        self.__fall_speed += self.__GRAVITY * dt
        self.__rect.move_ip(0, self.__fall_speed)

    # def __jump(self, screen_rect: pygame.Rect, platforms: set[p.Platform], dt: float) -> None:
    #     if self.__is_jumping:
    #         self.__cur_jump_time += dt
    #         v = self.__LAUNCH_SPEED - self.__GRAVITY * self.__cur_jump_time
    #         self.__rect.move_ip(0, -v)
    #         if self.__isOnGround(screen_rect, platforms):
    #             # Move back a unit of v so we don't go out of bounds.
    #             self.__rect.move_ip(0, v)
    #             self.__cur_jump_time = 0
    #             self.__is_jumping = False

    def __lockToGround(self, screen_rect: pygame.Rect, platforms: set[p.Platform]) -> None:
        if self.__rect.bottom >= screen_rect.bottom:
            self.__rect.bottom = screen_rect.bottom
            self.__fall_speed = 0
        for platform in platforms:
            if self.__rect.colliderect(platform.getRect()):
                self.__rect.bottom = platform.getRect().top
                self.__fall_speed = 0