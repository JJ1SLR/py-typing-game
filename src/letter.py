import random
import string

import pygame as pg



class Letter:

    def __init__(self, x, y):
        self.letter = random.choice(string.ascii_uppercase)
        self.color = (255, 255, 255)
        self.font = pg.font.Font(None, 200)
        self.txt_surface = self.font.render(self.letter, True, (255, 255, 255))
        self.text_rect = self.txt_surface.get_rect()
        self.x, self.y = (x - self.text_rect.width) / 2, (y - self.text_rect.height) / 2

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

    def update(self):
        self.letter = random.choice(string.ascii_uppercase)
        self.txt_surface = self.font.render(self.letter, True, (255, 255, 255))

    def draw(self, screen):
        screen.blit(self.txt_surface, [self.x, self.y])
