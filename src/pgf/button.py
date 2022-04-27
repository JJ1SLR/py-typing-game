from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Callable

import pygame as pg

from src.pgf.widget import Widget


class Button(Widget):

    def __init__(self, x: int = 0, y: int = 0, width: int = 160, height: int = 120, size: int = 50,
                 parent: Widget = None, text: str = ''):
        super().__init__(x, y, parent)
        self.color = (255, 255, 255)
        self.width, self.height = width, height
        self.size = size
        self.text = text
        self.font = pg.font.Font(None, size)
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.text_x = x + (width - self.txt_surface.get_rect().width ) / 2
        self.text_y = y + (height - self.txt_surface.get_rect().height) / 2
        self.mouse_down_handler = None
        self.mouse_up_handler = None

    def set_mouse_down_handler(self, handler: Callable):
        self.mouse_down_handler = handler

    def set_mouse_up_handler(self, handler: Callable):
        self.mouse_up_handler = handler

    def mouse_down_impl(self, event: pg.event.Event, handled: bool) -> bool:
        if self.mouse_down_handler:
            return self.mouse_down_handler(self, event, handled)
        return False

    def mouse_up_impl(self, event: pg.event.Event, handled: bool) -> bool:
        if self.mouse_up_handler:
            return self.mouse_up_handler(self, event, handled)
        return False

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.text_x, self.text_y])
