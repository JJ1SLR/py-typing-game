from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as pg
    from src.pgf.window import Window

from src.pgf.root_widget import RootWidget


class Scene:

    def __init__(self, window: Window):
        super().__init__()
        self.window = window
        self.root_widget = RootWidget(self)

    def get_width(self) -> int:
        return self.window.screen.get_width()

    def get_height(self) -> int:
        return self.window.screen.get_height()

    def on_key_down(self, event: pg.event.Event):
        pass

    def on_key_up(self, event: pg.event.Event):
        pass

    def on_mouse_down(self, event: pg.event.Event):
        pass

    def on_mouse_up(self, event: pg.event.Event):
        pass

    def on_draw(self):
        self.window.screen.fill((0, 0, 0))
        if self.window.picture:
            self.window.screen.blit(self.window.picture, self.window.picture.get_rect())
        self.root_widget.draw(self.window.screen)
