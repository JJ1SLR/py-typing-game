from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pgf.scene import Scene

from src.pgf.widget import Widget
from src.pgf.score import Score


class ScoreBoard(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None):
        super().__init__(x, y, parent)
        self.scoreOK = Score(5, 5, parent=self, text="OK:")
        self.scoreNG = Score(5, 35, parent=self, text="NG:")
        self.scoreTotal = Score(5, 65, parent=self, text="Total:")
        self.maxCombo = Score(5, 95, parent=self, text="Max Combo:")
        combo_y = self.scene.get_height() - 65
        self.scoreCombo = Score(5, combo_y, parent=self, size=60, text="COMBO:")

    def add_ok(self):
        self.scoreOK.add()
        self.scoreTotal.add()
        self.scoreCombo.add()
        if self.scoreCombo.num > self.maxCombo.num:
            self.maxCombo.add()

    def add_ng(self):
        self.scoreNG.add()
        self.scoreTotal.add()
        self.scoreCombo.reset()

    def get_combo(self) -> int:
        return self.scoreCombo.num

    def get_width(self) -> int:
        if self.scene:
            return self.scene.get_width()
        return 640

    def get_height(self) -> int:
        if self.scene:
            return self.scene.get_height()
        return 480
