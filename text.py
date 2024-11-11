import pygame

class TextManager:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.small_font = pygame.font.Font("fonts/coracat.ttf", 24)
        self.big_font = pygame.font.Font("fonts/coracat.ttf", 48)
        self.__screen_rect = screen_rect

    def drawScore(self, score: int, top_score: int, screen: pygame.Surface) -> None:
        score_text = self.small_font.render("Score: %s" % score, True, "white")
        score_rect = score_text.get_rect()
        score_rect.topright = self.__screen_rect.topright

        top_score_text = self.small_font.render("Top Score: %s" % top_score, True, "white")
        top_score_rect = top_score_text.get_rect()
        top_score_rect.topright = score_rect.bottomright

        screen.blit(score_text, score_rect)
        screen.blit(top_score_text, top_score_rect)

    def drawGameOver(self, screen: pygame.Surface) -> None:
        text = self.big_font.render("GAME OVER!", True, "yellow")
        text_rect = text.get_rect()
        text_rect.center = self.__screen_rect.center
        screen.blit(text, text_rect)

        retry_prompt = self.small_font.render("ENTER: Retry", True, "white")
        retry_prompt_rect = retry_prompt.get_rect()
        # retry_prompt_rect.centerx = self.__screen_rect.centerx
        # retry_prompt_rect.top = text_rect.bottom
        retry_prompt_rect.midtop = (self.__screen_rect.centerx, text_rect.bottom)
        screen.blit(retry_prompt, retry_prompt_rect)

        quit_prompt = self.small_font.render("ESC: Quit", True, "white")
        quit_prompt_rect = quit_prompt.get_rect()
        quit_prompt_rect.midtop = (self.__screen_rect.centerx, retry_prompt_rect.bottom)
        screen.blit(quit_prompt, quit_prompt_rect)