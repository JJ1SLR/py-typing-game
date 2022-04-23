from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

from random_line import RandomLine
from src.pgf import score

from src.pgf.scene import Scene


class LineScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.line = RandomLine(0, 0, parent=self.root_widget)
        self.line.set_center()
        self.scoreOK = score.Score(5, 5, parent=self.root_widget, text="OK:")
        self.scoreNG = score.Score(5, 35, parent=self.root_widget, text="NG:")
        self.scoreTotal = score.Score(5, 65, parent=self.root_widget, text="Total:")
        self.scoreCombo = score.Score(5, window.screen.get_height() - 60 - 5, parent=self.root_widget, size=60, text="COMBO:")
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")
        self.correct = False

    def on_key_down(self, event: pg.event.Event):
        if pg.K_a <= event.key <= pg.K_z:
            if self.line.judge(event.key):
                self.correct = True
                self.scoreOK.add()
                self.scoreTotal.add()
                self.scoreCombo.add()
                self.clickSnd.play()
            else:
                self.correct = False
                self.scoreNG.add()
                self.scoreTotal.add()
                self.scoreCombo.reset()
                self.errorSnd.play()

    def on_key_up(self, event: pg.event.Event):
        if self.correct:
            if self.line.is_complete():
                self.comboSnd.play()
                self.root_widget.remove_widget(self.line)
                self.line = RandomLine(0, 0, parent=self.root_widget)
                self.line.set_center()
            self.correct = False
