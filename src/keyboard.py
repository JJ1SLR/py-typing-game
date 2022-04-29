from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Dict

from src.pgf.widget import Widget
from src.pgf.letter import Letter


class KeyBoard(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, size: int = 40):
        super().__init__(x, y, parent)
        self.x, self.y = x, y
        self.size = size
        self.sep = 2
        self.current = ""
        self.letter_dict = self.create_letters()

    def get_height(self) -> int:
        return (self.size + self.sep) * 10 + self.sep * 10

    def get_width(self) -> int:
        return (self.size + self.sep) * 3

    def set_current(self, current: str):
        self.reset()
        self.current = current
        self.letter_dict[self.current].set_color((0, 0, 255))

    def reset(self):
        self.current = ""
        for widget in self.sub_widget_list:
            if type(widget) is Letter:
                widget.reset()

    def create_letters(self) -> Dict:
        letter_dict = {}
        widget = Letter(self.x + (self.size + self.sep) * 0, self.y, self, self.size, "Q")
        letter_dict["Q"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 1, self.y, self, self.size, "W")
        letter_dict["W"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 2, self.y, self, self.size, "E")
        letter_dict["E"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 3, self.y, self, self.size, "R")
        letter_dict["R"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 4, self.y, self, self.size, "T")
        letter_dict["T"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 5, self.y, self, self.size, "Y")
        letter_dict["Y"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 6, self.y, self, self.size, "U")
        letter_dict["U"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 7, self.y, self, self.size, "I")
        letter_dict["I"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 8, self.y, self, self.size, "O")
        letter_dict["O"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 9, self.y, self, self.size, "P")
        letter_dict["P"] = widget

        widget = Letter(self.x + (self.size + self.sep) * 0, self.y + self.size + self.sep, self, self.size, "A")
        letter_dict["A"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 1, self.y + self.size + self.sep, self, self.size, "S")
        letter_dict["S"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 2, self.y + self.size + self.sep, self, self.size, "D")
        letter_dict["D"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 3, self.y + self.size + self.sep, self, self.size, "F")
        letter_dict["F"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 4, self.y + self.size + self.sep, self, self.size, "G")
        letter_dict["G"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 5, self.y + self.size + self.sep,
                        self, self.size, "H")
        letter_dict["H"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 6, self.y + self.size + self.sep,
                        self, self.size, "J")
        letter_dict["J"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 7, self.y + self.size + self.sep,
                        self, self.size, "K")
        letter_dict["K"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 8, self.y + self.size + self.sep,
                        self, self.size, "L")
        letter_dict["L"] = widget

        widget = Letter(self.x + (self.size + self.sep) * 0, self.y + (self.size + self.sep) * 2, self, self.size, "Z")
        letter_dict["Z"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 1, self.y + (self.size + self.sep) * 2, self, self.size, "X")
        letter_dict["X"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 2, self.y + (self.size + self.sep) * 2, self, self.size, "C")
        letter_dict["C"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 3, self.y + (self.size + self.sep) * 2, self, self.size, "V")
        letter_dict["V"] = widget
        widget = Letter(self.x + (self.size + self.sep) * 4, self.y + (self.size + self.sep) * 2, self, self.size, "B")
        letter_dict["B"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 5, self.y + (self.size + self.sep) * 2,
                        self, self.size, "N")
        letter_dict["N"] = widget
        widget = Letter(self.x + self.sep * 10 + (self.size + self.sep) * 6, self.y + (self.size + self.sep) * 2,
                        self, self.size, "M")
        letter_dict["M"] = widget

        return letter_dict
