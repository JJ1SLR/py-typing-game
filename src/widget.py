from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as pg
    from scene import Scene


class Widget:

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None):
        self.x, self.y = x, y
        self.parent = parent
        self.scene = scene

    def draw(self, screen: pg.surface):
        pass
