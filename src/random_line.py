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
        self.line = [Letter(x + i * (size + 2), y, self, scene, size) for i in range(count)]

    def get_width(self) -> int:
        return (self.size + 2) * self.count - 2

    def get_height(self) -> int:
        return self.size

    def draw(self, screen: pg.surface):
        raise NotImplementedError()
