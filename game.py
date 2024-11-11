from enum import Enum
import crosshair as c
import cat as ct
import bullet as b
import enemy as e
import platforms as p
import text as t
import healthbar as h
import animation as a
import snowcat as s
import pygame

FPS = 60

class States(Enum):
    Playing = 0
    GameOver = 1
    Quit = 2    

class Game:
    def __init__(self, screen: pygame.Surface, screen_rect: pygame.Rect) -> None:
        self.__SPAWN_TIME = 3
        self.__JUMP_COOL_TIME = 1.5
        self.__clock = pygame.time.Clock()
        self.__cur_jump_cool_time = 0.0
        self.__jump_counter = 0
        self.__can_jump = True
        self.__cur_spawn_time = 0.0
        self.__screen = screen
        self.__screen_rect = screen_rect
        self.__text_manager = t.TextManager(screen_rect)
        self.__crosshair = c.Crosshair()
        self.__puma = ct.Cat((screen_rect.centerx, 50))
        self.__bullets: set[b.Bullet] = set()
        self.__enemies: set[e.Enemy] = set()
        self.__platforms: set[p.Platform] = set()
        self.__health_bar = h.HealthBar(self.__puma)
        self.__state = States.Playing
        self.__score = 0
        self.__top_score = 0
        self.__bg_sprite = pygame.image.load("sprites/bg.png")
        self.__gameover_sprite = pygame.image.load("sprites/gameover.png")
        self.__snowcat = s.Snowcat(screen_rect)
        self.loadTopScore()

        # Add 5 platforms.
        half_width = 200
        vertical = 150
        self.__platforms.add(p.Platform((screen_rect.left + half_width, screen_rect.top + vertical)))
        self.__platforms.add(p.Platform((screen_rect.left + half_width, screen_rect.bottom - vertical)))
        self.__platforms.add(p.Platform((screen_rect.right - half_width, screen_rect.top + vertical)))
        self.__platforms.add(p.Platform((screen_rect.right - half_width, screen_rect.bottom - vertical)))
        self.__platforms.add(p.Platform(screen_rect.center))

        # Create snowfall animation and extend across screen.
        sprite_width = screen_rect.width
        sprite_height = 720
        self.__snowfall_anim = a.Animation(sprite_height, 3, 0.25, "sprites/snowfall.png")
        self.__snow_rects: list[pygame.Rect] = []
        for y in range(screen_rect.top, screen_rect.bottom, sprite_height):
            for x in range(screen_rect.left, screen_rect.right, sprite_width):
                self.__snow_rects.append(pygame.Rect(x, y, sprite_width, sprite_height))

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
        self.__health_bar.update()
        
        if not self.__puma.isAlive():
            self.endGame()

        if self.__state == States.Playing:
            self.__snowfall_anim.update(dt)
            self.__snowcat.update(dt)

            self.__cur_spawn_time += dt
            if (self.__cur_spawn_time >= self.__SPAWN_TIME):
                # Spawn a new enemy.
                self.__enemies.add(e.Enemy(self.__screen_rect))
                # Reset timer.
                self.__cur_spawn_time = 0

            # Update the entities' transformations.
            self.__crosshair.update(self.__screen_rect)
            self.__puma.update(self.__screen_rect, self.__platforms, dt)
            self.updateJumpCooldown(dt)
            marked_bullets: set[b.Bullet] = set()
            for bullet in self.__bullets:
                bullet.update(dt)
                if self.bulletIsDying(bullet):
                    marked_bullets.add(bullet)
            for enemy in self.__enemies:
                if enemy.getRect().colliderect(self.__puma.getRect()):
                    self.__puma.takeDamage()
                enemy.update(self.__screen_rect, self.__puma.getPos(), self.__platforms, dt)
            
            self.__bullets -= marked_bullets
            self.doBulletEnemyCollisions()
        else:
            # If game ended and player presses Enter, the game restarts.
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.resetGame()
            elif keys[pygame.K_ESCAPE]:
                self.__state = States.Quit

    def render_frame(self) -> None:
       if self.__state == States.GameOver:
          self.__screen.blit(self.__gameover_sprite, self.__screen_rect)
          self.__text_manager.drawGameOver(self.__screen)
       else:
          self.__screen.blit(self.__bg_sprite, self.__screen_rect)
          for rect in self.__snow_rects:
            self.__snowfall_anim.draw(rect, self.__screen)
            self.__puma.draw(self.__screen)
            for platform in self.__platforms:
                platform.draw(self.__screen)
            self.__crosshair.draw(self.__screen)
            for enemy in self.__enemies:
                enemy.draw(self.__screen)
            for bullet in self.__bullets:
                bullet.draw(self.__screen)
            self.__health_bar.draw(self.__screen)
            self.__snowcat.draw(self.__screen)
       
       self.__text_manager.drawScore(self.__score, self.__top_score, self.__screen)

    def spawn_bullet(self) -> None:
        if self.__state == States.Playing:
            puma_pos = pygame.Vector2(self.__puma.getPos())
            crosshair_pos = pygame.Vector2(self.__crosshair.getPos())
            dir = pygame.Vector2.normalize(crosshair_pos - puma_pos)
            self.__bullets.add(b.Bullet(puma_pos, dir))

    def doCatJump(self) -> None:
        if self.__can_jump:
            self.__puma.jump()
            self.__jump_counter += 1
    
    def updateJumpCooldown(self, dt: float) -> None:
        if self.__can_jump:
            if self.__jump_counter >= 3:
                self.__can_jump = False
        else:
            self.__cur_jump_cool_time += dt
            if self.__cur_jump_cool_time >= self.__JUMP_COOL_TIME:
                self.__cur_jump_cool_time = 0.0
                self.__jump_counter = 0
                self.__can_jump = True

    def doBulletEnemyCollisions(self) -> None:
        marked_bullets: set[b.Bullet] = set()
        marked_enemies: set[b.Enemy] = set()
        for bullet in self.__bullets:
            for enemy in self.__enemies:
                if bullet.getRect().colliderect(enemy.getRect()):
                    print("Collision detected!")
                    # Mark the bullet to destroy it.
                    marked_bullets.add(bullet)
                    # Process enemy damage.
                    enemy.takeDamage()
                    if not enemy.isAlive():
                        self.__score += 1
                        print("Score: %s." % self.__score)
                        print("Top Score: %s." % self.__top_score)
                        marked_enemies.add(enemy)
        
        # Remove the marked bullets and enemies from the original set.
        self.__bullets -= marked_bullets
        self.__enemies -= marked_enemies

    def bulletIsDying(self, bullet: b.Bullet) -> bool:
        # Check if bullet hits any platform.
        for platform in self.__platforms:
            if bullet.getRect().colliderect(platform.getRect()):
                return True
        # If it hits no platforms, check if it goes out of bounds.
        return not self.__screen_rect.contains(bullet.getRect())

    def saveTopScore(self) -> None:
        if self.__score > self.__top_score:
            # Set top score to the new score.
            self.__top_score = self.__score
            # Write into a new or existing file.
            with open("score.txt", 'w') as file:
                file.write(str(self.__top_score))

    def loadTopScore(self) -> None:
        try:
            with open("score.txt") as file:
                self.__top_score = int(file.read())
        except IOError:
            print("File not found. Setting score to 0.")
            self.__top_score = 0

    def resetGame(self) -> None:
        self.__bullets.clear()
        self.__enemies.clear()
        self.__puma = ct.Cat((self.__screen_rect.centerx, 50))
        self.__health_bar = h.HealthBar(self.__puma)
        self.__cur_spawn_time = 0.0
        self.__score = 0
        self.__state = States.Playing
    
    def endGame(self) -> None:
        self.__state = States.GameOver
        self.saveTopScore()

    def hasQuit(self) -> bool:
        return self.__state == States.Quit