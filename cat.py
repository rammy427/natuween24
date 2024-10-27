import pygame

class Cat:
    def __init__(self, center: pygame.Vector2) -> None:
        self.__MAX_HP = 9
        self.__WIDTH = 96
        self.__HEIGHT = 48
        self.__SPEED = 500
        self.__GRAVITY = 9.8
        self.__LAUNCH_SPEED = 4
        self.__hp = self.__MAX_HP
        self.__rect = pygame.Rect(0, 0, self.__WIDTH, self.__HEIGHT)
        self.__rect.center = center
        self.__isJumping = False
        self.__cur_time = 0

    def update(self, screen_rect: pygame.Rect, dt: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.__rect.move_ip(-self.__SPEED * dt, 0)
        if keys[pygame.K_d]:
            self.__rect.move_ip(self.__SPEED * dt, 0)
        
        # Cat can only jump if it isn't midair.
        if keys[pygame.K_w] and not self.__isJumping:
            self.__isJumping = True
        
        self.__jump(screen_rect, dt)
        self.__rect.clamp_ip(screen_rect)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, "yellow", self.__rect)

    def getPos(self) -> pygame.Vector2:
        return self.__rect.center
    
    def getRect(self) -> pygame.Rect:
        return self.__rect
    
    def takeDamage(self) -> None:
        self.__hp -= 1
        print("Life: %s." % self.__hp)

    def isAlive(self) -> bool:
        return self.__hp > 0
    
    def __jump(self, screen_rect: pygame.Rect, dt: float) -> None:
        if self.__isJumping:
            self.__cur_time += dt
            v = self.__LAUNCH_SPEED - self.__GRAVITY * self.__cur_time
            self.__rect.move_ip(0, -v)
            if self.__hasHitGround(screen_rect):
                # Move back a unit of v so we don't go out of bounds.
                self.__rect.move_ip(0, v)
                self.__cur_time = 0
                self.__isJumping = False

    def __hasHitGround(self, screen_rect: pygame.Rect) -> bool:
        return self.__rect.bottom >= screen_rect.bottom