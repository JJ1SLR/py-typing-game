import random
import string

import pygame as pg

from src.pgf.widget import Widget


class Letter(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, size: int = 200, letter: str = ''):
        super().__init__(x, y, parent)
        if letter:
            self.letter = letter
        else:
            self.letter = random.choice(string.ascii_uppercase)
        self.color = (255, 255, 255)
        self.font = pg.font.Font(None, size)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def judge(self, event_key: int) -> bool:
        if event_key == ord(self.letter.lower()):
            self._set_ok()
            return True
        else:
            self._set_ng()
            return False

    def _set_ok(self):
        self.color = (0, 255, 0)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def _set_ng(self):
        self.color = (255, 0, 0)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def set_color(self, color: tuple):
        self.color = color
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def reset(self):
        self.color = (255, 255, 255)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def next(self):
        self.letter = random.choice(string.ascii_uppercase)
        self.color = (255, 255, 255)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def set_size(self, size: int):
        self.font = pg.font.Font(None, size)
        self.txt_surface = self.font.render(self.letter, True, self.color)

    def get_width(self) -> int:
        return self.txt_surface.get_rect().width

    def get_height(self) -> int:
        return self.txt_surface.get_rect().height

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.x, self.y])
