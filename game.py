import crosshair as c
import cat as ct
import bullet as b
import enemy as e
import platforms as p
import pygame

FPS = 60

class Game:
    def __init__(self, screen: pygame.Surface, screen_rect: pygame.Rect) -> None:
        self.__SPAWN_TIME = 2
        self.__clock = pygame.time.Clock()
        self.__cur_time = 0.0
        self.__screen = screen
        self.__screen_rect = screen_rect
        self.__crosshair = c.Crosshair()
        self.__puma = ct.Cat((screen_rect.centerx, 50))
        # self.__puma = ct.Cat((screen_rect.centerx, screen_rect.bottom))
        self.__bullets: set[b.Bullet] = set()
        self.__enemies: set[e.Enemy] = set()
        self.__platforms: set[p.Platform] = set()
        self.__platforms.add(p.Platform((screen_rect.centerx, screen_rect.bottom - 50), 200))

    def run(self) -> None:
        # Fill the screen with color to clear previous frame.
        self.__screen.fill("black")
        self.update_frame()
        self.render_frame()
        # Flip display to render the new frame.
        pygame.display.flip()

    def update_frame(self) -> None:
        # Calculate delta time in milliseconds.
        dt = self.__clock.tick(FPS) / 1000
        gameIsOver = not self.__puma.isAlive()

        if not gameIsOver:
            self.__cur_time += dt
            if (self.__cur_time >= self.__SPAWN_TIME):
                # Spawn a new enemy.
                # self.__enemies.add(e.Enemy(self.__screen_rect))
                # Reset timer.
                self.__cur_time = 0

            # Update the entities' transformations.
            self.__crosshair.update(self.__screen_rect)
            self.__puma.update(self.__screen_rect, self.__platforms, dt)
            for bullet in self.__bullets:
                bullet.update(dt)
            for enemy in self.__enemies:
                if enemy.getRect().colliderect(self.__puma.getRect()):
                    self.__puma.takeDamage()
                enemy.update(dt)
            
            self.doBulletEnemyCollisions()

    def render_frame(self) -> None:
       self.__puma.draw(self.__screen)
       self.__crosshair.draw(self.__screen)
       for platform in self.__platforms:
           platform.draw(self.__screen)
       for enemy in self.__enemies:
           enemy.draw(self.__screen)
       for bullet in self.__bullets:
           bullet.draw(self.__screen)

    def spawn_bullet(self) -> None:
        puma_pos = pygame.Vector2(self.__puma.getPos())
        crosshair_pos = pygame.Vector2(self.__crosshair.getPos())
        dir = pygame.Vector2.normalize(crosshair_pos - puma_pos)
        self.__bullets.add(b.Bullet(puma_pos, dir))

    def doCatJump(self) -> None:
        self.__puma.jump()

    def doBulletEnemyCollisions(self) -> None:
        marked_bullets: set[b.Bullet] = set()
        marked_enemies: set[b.Enemy] = set()
        for bullet in self.__bullets:
            for enemy in self.__enemies:
                if bullet.getRect().colliderect(enemy.getRect()):
                    print("Collision detected!")
                    marked_bullets.add(bullet)
                    marked_enemies.add(enemy)
        
        # Remove the marked bullets and enemies from the original set.
        self.__bullets -= marked_bullets
        self.__enemies -= marked_enemies