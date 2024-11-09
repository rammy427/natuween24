import pygame

class Animation:
    def __init__(self, frame_height: int, n_frames: int, frame_time: float, filename: str) -> None:
        self.__N_FRAMES = n_frames
        self.__FRAME_TIME = frame_time
        self.__sprite = pygame.image.load(filename)
        self.__FRAME_WIDTH = self.__sprite.get_rect().size[0] // n_frames
        self.__FRAME_HEIGHT = frame_height
        self.__crop_rect = pygame.Rect(0, 0, self.__FRAME_WIDTH, self.__FRAME_HEIGHT)
        self.__cur_time = 0.0
        self.__cur_frame = 0

    def update(self, dt: float, state = 0) -> None:
        self.__cur_time += dt
        if (self.__cur_time >= self.__FRAME_TIME):
            self.__cur_frame = (self.__cur_frame + 1) % self.__N_FRAMES
            new_x = self.__cur_frame * self.__FRAME_WIDTH
            new_y = state * self.__FRAME_HEIGHT
            self.__crop_rect.topleft = (new_x, new_y)
            self.__cur_time = 0.0

    def draw(self, rect: pygame.Rect, screen: pygame.Surface) -> None:
        screen.blit(self.__sprite, rect, self.__crop_rect)

    def getCurRect(self) -> pygame.Rect:
        return self.__crop_rect