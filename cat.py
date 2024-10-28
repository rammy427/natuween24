import pygame
import platforms as p

class Cat:
    def __init__(self, center: pygame.Vector2) -> None:
        self.__MAX_HP = 9
        self.__GOD_TIME = 3
        self.__WIDTH = 96
        self.__HEIGHT = 48
        self.__SPEED = 500
        self.__GRAVITY = 9.8
        self.__LAUNCH_SPEED = 5.5
        self.__hp = self.__MAX_HP
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
        # self.__is_jumping = False
        # self.__cur_jump_time = 0
        self.__fall_speed = 0
        self.__is_invincible = False
        self.__cur_god_time = 0

    def update(self, screen_rect: pygame.Rect, platforms: set[p.Platform], dt: float) -> None:
        # Process movement inputs.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.__rect.move_ip(-self.__SPEED * dt, 0)
        if keys[pygame.K_d]:
            self.__rect.move_ip(self.__SPEED * dt, 0)

        # Update god timer.
        if self.__is_invincible:
            self.__cur_god_time += dt
            if self.__cur_god_time >= self.__GOD_TIME:
                self.__is_invincible = False
                self.__cur_god_time = 0
        
        # Cat can only jump if it isn't midair.
        # if keys[pygame.K_w] and not self.__is_jumping:
        #     self.__is_jumping = True
        
        self.__fall(screen_rect, platforms, dt)
        # self.__jump(screen_rect, platforms, dt)
        self.__rect.clamp_ip(screen_rect)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "yellow", self.__rect)

    def getPos(self) -> pygame.Vector2:
        return self.__rect.center
    
    def getRect(self) -> pygame.Rect:
        return self.__rect
    
    def takeDamage(self) -> None:
        if not self.__is_invincible:
            self.__hp -= 1
            self.__is_invincible = True
            print("Life: %s." % self.__hp)

    def isAlive(self) -> bool:
        return self.__hp > 0
    
    def __fall(self, screen_rect: pygame.Rect, platforms: set[p.Platform], dt: float) -> None:
        if self.__isOnGround(screen_rect, platforms):
            self.__fall_speed = 0
        else:
            self.__fall_speed += self.__GRAVITY * dt
            self.__rect.move_ip(0, self.__fall_speed)

    def jump(self):
        self.__rect.move_ip(0, -1)
        self.__fall_speed -= self.__LAUNCH_SPEED

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

    def __isOnGround(self, screen_rect: pygame.Rect, platforms: set[p.Platform]) -> bool:
        if self.__rect.bottom >= screen_rect.bottom:
            return True
        for platform in platforms:
            if self.__rect.colliderect(platform.getRect()):
                return True
        return False