import pygame as pg

from widget import Widget


class Score(Widget):

    def __init__(self, x: int, y: int, size: int, text: str = '', num: int = 0):
        super().__init__(x, y)
        self.color = (255, 255, 255)
        self.text = text
        self.num = num
        self.font = pg.font.Font(None, size-5)
        self.txt_surface = self.font.render(text + ' ' + str(num), True, self.color)

    def update(self):
        self.txt_surface = self.font.render(self.text + ' ' + str(self.num), True, self.color)

    def add(self):
        self.num += 1
        self.update()

    def reset(self):
        self.num = 0
        self.update()

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.x + 5, self.y + 5])
