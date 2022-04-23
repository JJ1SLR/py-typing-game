from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.pgf.scene import Scene

from src.pgf.widget import Widget
from src.pgf.score import Score


class ScoreBoard(Widget):

    def __init__(self, x: int = 0, y: int = 0, parent: Widget = None, scene: Scene = None):
        super().__init__(x, y, parent, scene)
        self.scoreOK = Score(5, 5, parent=self, scene=scene, text="OK:")
        self.scoreNG = Score(5, 35, sparent=self, cene=scene, text="NG:")
        self.scoreTotal = Score(5, 65, parent=self, scene=scene, text="Total:")
        self.maxCombo = Score(5, 95, parent=self, scene=scene, text="Max Combo:")
        combo_y = 125
        if scene:
            combo_y = scene.get_height() - 65
        self.scoreCombo = Score(5, combo_y, parent=self, scene=scene, size=60, text="COMBO:")

    def get_width(self) -> int:
        if self.scene:
            return self.scene.get_width()
        return 640

    def get_height(self) -> int:
        if self.scene:
            return self.scene.get_height()
        return 480
