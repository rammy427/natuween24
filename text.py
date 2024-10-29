import pygame

class TextManager:
    def __init__(self, screen_rect: pygame.Rect) -> None:
        self.font = pygame.font.Font(None, 48)
        self.__screen_rect = screen_rect

    def drawScore(self, score: int, top_score: int, screen: pygame.Surface) -> None:
        score_text = self.font.render("Score: %s" % score, True, "white")
        score_rect = score_text.get_rect()
        score_rect.topright = self.__screen_rect.topright

        top_score_text = self.font.render("Top Score: %s" % top_score, True, "white")
        top_score_rect = top_score_text.get_rect()
        top_score_rect.topright = score_rect.bottomright

        screen.blit(score_text, score_rect)
        screen.blit(top_score_text, top_score_rect)