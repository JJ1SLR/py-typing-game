from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from scene import Scene

import pygame as pg

from widget import Widget
from letter import Letter


class RandomLine(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None,
                 size: int = 50, count: int = 10):
        super().__init__(x, y, parent, scene)
        self.x, self.y = x, y
        self.size = size
        self.count = count
        self.current = 0
        self.line = [Letter(x + i * (size + 2), y, self, scene, size) for i in range(count)]

    def judge(self, event_key: int) -> bool:
        b_retval = self.line[self.current].judge(event_key)
        if b_retval:
            self.current += 1
        return b_retval

    def is_complete(self) -> bool:
        return self.current >= self.count

    def reset(self):
        for letter in self.line:
            letter.reset()

    def set_scene_center(self):
        self.x = (self.scene.get_width() - self.get_width()) / 2
        self.y = (self.scene.get_height() - self.get_height()) / 2
        for i in range(self.count):
            self.line[i].x = self.x + i * (self.size + 2)
            self.line[i].y = self.y

    def get_width(self) -> int:
        return (self.size + 2) * self.count - 2

    def get_height(self) -> int:
        return self.size

    def draw(self, screen: pg.surface):
        for letter in self.line:
            letter.draw(screen)
