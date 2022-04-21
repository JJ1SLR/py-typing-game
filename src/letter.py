from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from scene import Scene

import random
import string

import pygame as pg

from widget import Widget


class Letter(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None, size:int = 200, letter: str = ''):
        super().__init__(x, y, parent, scene)
        if letter:
            self.letter = letter
        else:
            self.letter = random.choice(string.ascii_uppercase)
        self.color = (255, 255, 255)
        self.font = pg.font.Font(None, size)
        self.txt_surface = self.font.render(self.letter, True, (255, 255, 255))
        self.real_x, self.real_y = self.x, self.y

    def judge(self, event_key: int) -> bool:
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

    def set_scene_center(self):
        text_rect = self.txt_surface.get_rect()
        self.real_x = (self.scene.get_width() - text_rect.width) / 2
        self.real_y = (self.scene.get_height() - text_rect.height) / 2

    def get_width(self) -> int:
        return self.txt_surface.get_rect().width

    def get_height(self) -> int:
        return self.txt_surface.get_rect().height

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.real_x, self.real_y])
