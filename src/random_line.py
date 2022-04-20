import string

import pygame as pg

from widget import Widget
from letter import Letter


class RandomLine(Widget):

    def __init__(self, x, y, size=50, count=10):
        self.x, self.y = x, y
        self.size = size
        self.count = count
        self.line = [Letter(x + i * (size + 2), y, size ) for i in range(count)]


