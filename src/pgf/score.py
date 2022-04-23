from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pgf.scene import Scene

import pygame as pg

from src.pgf.widget import Widget


class Score(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None,
                 size: int = 30, text: str = '', num: int = 0):
        super().__init__(x, y, parent, scene)
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

    def get_width(self) -> int:
        return self.txt_surface.get_rect().width

    def get_height(self) -> int:
        return self.txt_surface.get_rect().height

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.x + 5, self.y + 5])
