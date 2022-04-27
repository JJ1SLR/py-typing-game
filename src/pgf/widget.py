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

    def mouse_down_impl(self, event: pg.event.Event, handled: bool) -> bool:
        return handled

    def mouse_up_impl(self, event: pg.event.Event, handled: bool) -> bool:
        return handled

    def on_mouse_down(self, event: pg.event.Event) -> bool:
        handled = False
        for widget in self.sub_widget_list:
            handled |= widget.on_mouse_down(event)
        if self.is_in_widget(event.pos[0], event.pos[1]):
            handled = self.mouse_down_impl(event, handled)
        return handled

    def on_mouse_up(self, event: pg.event.Event) -> bool:
        handled = False
        for widget in self.sub_widget_list:
            handled |= widget.on_mouse_up(event)
        if self.is_in_widget(event.pos[0], event.pos[1]):
            handled = self.mouse_up_impl(event, handled)
        return handled

    def is_in_widget(self, x: int, y: int):
        return self.x <= x <= self.x + self.get_width() and self.y <= y <= self.y + self.get_height()

    def draw(self, screen: pg.surface):
        if not self.sub_widget_list:
            raise NotImplementedError()
        for sub_widget in self.sub_widget_list:
            sub_widget.draw(screen)
