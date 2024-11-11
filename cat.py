import pygame
from enum import Enum
import platforms as p
import animation as a

class Animations(Enum):
    IdleLeft = 0
    IdleRight = 1
    RunningLeft = 2
    RunningRight = 3
    JumpingLeft = 4
    JumpingRight = 5
    Count = 6

class Cat:
    def __init__(self, center: pygame.Vector2) -> None:
        self.__MAX_HP = 9
        self.__GOD_TIME = 3
        self.__WIDTH = 106
        self.__HEIGHT = 71
        self.__SPEED = 500
        self.__GRAVITY = 15
        self.__LAUNCH_SPEED = 8
        self.__hp = self.__MAX_HP
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
        self.__last_dir = -1
        self.__cur_anim = Animations.IdleLeft
        self.__animation = a.Animation(self.__HEIGHT, 8, 0.125, "sprites/puma.png")
        self.__is_jumping = False
        # self.__cur_jump_time = 0
        self.__fall_speed = 0
        self.__is_invincible = False
        self.__cur_god_time = 0

    def update(self, screen_rect: pygame.Rect, platforms: set[p.Platform], dt: float) -> None:
        # Process movement inputs.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.__last_dir = -1
            if not self.__is_jumping:
                self.__cur_anim = Animations.RunningLeft
            self.__rect.move_ip(-self.__SPEED * dt, 0)
        if keys[pygame.K_d]:
            self.__last_dir = 1
            if not self.__is_jumping:
                self.__cur_anim = Animations.RunningRight
            self.__rect.move_ip(self.__SPEED * dt, 0)

        # Update god timer.
        if self.__is_invincible:
            self.__cur_god_time += dt
            if self.__cur_god_time >= self.__GOD_TIME:
                self.__is_invincible = False
                self.__cur_god_time = 0
        
        self.__fall(dt)
        # self.__jump(screen_rect, platforms, dt)
        self.__lockToGround(screen_rect, platforms)

        # Wrap around the screen.
        if self.__rect.right <= screen_rect.left:
            self.__rect.left = screen_rect.right
        elif self.__rect.left >= screen_rect.right:
            self.__rect.right = screen_rect.left

        # Clamp at top.
        if self.__rect.top <= screen_rect.top:
            self.__rect.top = screen_rect.top
        
        # Update animation with current state.
        self.__animation.update(dt, self.__cur_anim.value)
        if self.__is_jumping:
            if self.__last_dir == -1:
                self.__cur_anim = Animations.JumpingLeft
            else:
                self.__cur_anim = Animations.JumpingRight
        else:
            if self.__last_dir == -1:
                self.__cur_anim = Animations.IdleLeft
            else:
                self.__cur_anim = Animations.IdleRight
    
    def draw(self, screen: pygame.Surface) -> None:
        self.__animation.draw(self.__rect, screen)

    def getPos(self) -> pygame.Vector2:
        return self.__rect.center
    
    def getRect(self) -> pygame.Rect:
        return self.__rect
    
    def getHP(self) -> int:
        return self.__hp
    
    def takeDamage(self) -> None:
        if not self.__is_invincible:
            self.__hp -= 1
            self.__is_invincible = True
            # print("Life: %s." % self.__hp)

    def isAlive(self) -> bool:
        return self.__hp > 0
    
    def isInvincible(self) -> bool:
        return self.__is_invincible
    
    def jump(self) -> None:
        self.__rect.move_ip(0, -1)
        self.__fall_speed = -self.__LAUNCH_SPEED
        self.__is_jumping = True
    
    def __fall(self, dt: float) -> None:
        self.__fall_speed += self.__GRAVITY * dt
        self.__rect.move_ip(0, self.__fall_speed)

    def __lockToGround(self, screen_rect: pygame.Rect, platforms: set[p.Platform]) -> None:
        if self.__rect.bottom >= screen_rect.bottom:
            self.__rect.bottom = screen_rect.bottom
            self.__fall_speed = 0
            self.__is_jumping = False
        for platform in platforms:
            if self.__rect.colliderect(platform.getRect()) and self.__fall_speed > 0:
                self.__rect.bottom = platform.getRect().top
                self.__fall_speed = 0
                self.__is_jumping = False