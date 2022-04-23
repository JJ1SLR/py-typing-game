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
        if scene:
            self.scene = scene
        elif parent:
            self.scene = parent.scene
        else:
            raise Exception("There is no scene for widget: %r" % self)
        self.sub_widget_list = []
        if parent:
            self.parent.add_widget(self)

    def add_widget(self, widget: Widget):
        widget.parent = self
        self.sub_widget_list.append(widget)

    def remove_widget(self, widget: Widget):
        widget.parent = None
        self.sub_widget_list.remove(widget)

    def set_center(self):
        self.x = (self.parent.get_width() - self.get_width()) / 2
        self.y = (self.parent.get_height() - self.get_height()) / 2

    @abstractmethod
    def get_width(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_height(self) -> int:
        raise NotImplementedError()

    def draw(self, screen: pg.surface):
        if not self.sub_widget_list:
            raise NotImplementedError()
        for sub_widget in self.sub_widget_list:
            sub_widget.draw(screen)
