from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as pg
    from scene import Scene

import abc
from abc import abstractmethod


class Widget(metaclass=abc.ABCMeta):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None):
        self.x, self.y = x, y
        self.parent = parent
        self.scene = scene
        self.sub_widget_list = []
        if scene:
            self.scene.add_widget(self)
        if parent:
            self.parent.add_widget(self)

    def add_widget(self, widget: Widget):
        self.sub_widget_list.append(widget)

    @abstractmethod
    def get_width(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_height(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def draw(self, screen: pg.surface):
        raise NotImplementedError()
