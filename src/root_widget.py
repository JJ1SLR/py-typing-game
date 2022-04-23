from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from scene import Scene

from widget import Widget


class RootWidget(Widget):
    def __init__(self, scene: Scene):
        super().__init__(0, 0, parent=None, scene=scene)

    def get_width(self) -> int:
        return self.scene.get_width()

    def get_height(self) -> int:
        return self.scene.get_height()
