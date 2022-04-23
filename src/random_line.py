from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pgf.scene import Scene

from src.pgf.widget import Widget
from src.pgf.letter import Letter


class RandomLine(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, size: int = 70, count: int = 10):
        super().__init__(x, y, parent)
        self.x, self.y = x, y
        self.size = size
        self.count = count
        self.current = 0
        [Letter(x + i * (size + 2), y, self, size) for i in range(count)]

    def judge(self, event_key: int) -> bool:
        b_retval = self.sub_widget_list[self.current].judge(event_key)
        if b_retval:
            self.current += 1
        return b_retval

    def is_complete(self) -> bool:
        return self.current >= self.count

    def reset(self):
        for letter in self.sub_widget_list:
            letter.reset()

    def set_center(self):
        self.x = (self.scene.get_width() - self.get_width()) / 2
        self.y = (self.scene.get_height() - self.get_height()) / 2
        for i in range(self.count):
            self.sub_widget_list[i].x = self.x + i * (self.size + 2)
            self.sub_widget_list[i].y = self.y

    def get_width(self) -> int:
        return (self.size + 2) * self.count - 2

    def get_height(self) -> int:
        return self.size
