from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as pg
    from main import MainWindow
    from widget import Widget


class Scene:

    def __init__(self, window: MainWindow):
        super().__init__()
        self.window = window
        self.widget_list = []

    def get_width(self) -> int:
        return self.window.screen.get_width()

    def get_height(self) -> int:
        return self.window.screen.get_height()

    def add_widget(self, widget: Widget):
        self.widget_list.append(widget)

    def remove_widget(self, widget: Widget):
        for sub_widget in widget.sub_widget_list:
            self.remove_widget(sub_widget)
        self.widget_list.remove(widget)

    def on_key_down(self, event: pg.event.Event):
        pass

    def on_key_up(self, event: pg.event.Event):
        pass

    def on_draw(self):
        self.window.screen.fill((0, 0, 0))
        self.window.screen.blit(self.window.picture, self.window.picture.get_rect())
        for widget in self.widget_list:
            widget.draw(self.window.screen)
