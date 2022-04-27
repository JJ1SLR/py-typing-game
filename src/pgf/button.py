import random
import string

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

    def mouse_down(self, event: pg.event.Event, handled: bool) -> bool:
        print("Mouse Down! ", handled)
        return True

    def mouse_up(self, event: pg.event.Event, handled: bool) -> bool:
        print("Mouse Up! ", handled)
        return True

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def draw(self, screen: pg.surface):
        screen.blit(self.txt_surface, [self.text_x, self.text_y])
