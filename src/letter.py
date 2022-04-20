import random
import string

import pygame as pg

from widget import Widget


class Letter(Widget):

    def __init__(self, x, y, size=200, letter=''):
        super().__init__(x, y)
        if letter:
            self.letter = letter
        else:
            self.letter = random.choice(string.ascii_uppercase)
        self.color = (255, 255, 255)
        self.font = pg.font.Font(None, size)
        self.txt_surface = self.font.render(self.letter, True, (255, 255, 255))
        self.text_rect = self.txt_surface.get_rect()
        self.real_x, self.real_y = (x - self.text_rect.width) / 2, (y - self.text_rect.height) / 2

    def judge(self, event_key):
        if event_key == ord(self.letter.lower()):
            self._set_ok()
            return True
        else:
            self._set_ng()
            return False

    def _set_ok(self):
        self.txt_surface = self.font.render(self.letter, True, (0, 255, 0))

    def _set_ng(self):
        self.txt_surface = self.font.render(self.letter, True, (255, 0, 0))

    def next(self):
        self.letter = random.choice(string.ascii_uppercase)
        self.txt_surface = self.font.render(self.letter, True, (255, 255, 255))

    def draw(self, screen):
        self.text_rect = self.txt_surface.get_rect()
        self.real_x, self.real_y = (self.x - self.text_rect.width) / 2, (self.y - self.text_rect.height) / 2
        screen.blit(self.txt_surface, [self.real_x, self.real_y])
