from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

from src.pgf.scene import Scene

from random_line import RandomLine
from score_board import ScoreBoard


class LineScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.line = RandomLine(0, 0, parent=self.root_widget)
        self.line.set_center()
        self.scoreBoard = ScoreBoard(0, 0, parent=self.root_widget)
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")
        self.correct = False

    def on_key_down(self, event: pg.event.Event):
        if pg.K_a <= event.key <= pg.K_z:
            if self.line.judge(event.key):
                self.correct = True
                self.scoreBoard.add_ok()
                self.clickSnd.play()
            else:
                self.correct = False
                self.scoreBoard.add_ng()
                self.errorSnd.play()

    def on_key_up(self, event: pg.event.Event):
        if self.correct:
            if self.line.is_complete():
                self.comboSnd.play()
                self.root_widget.remove_widget(self.line)
                self.line = RandomLine(0, 0, parent=self.root_widget)
                self.line.set_center()
            self.correct = False
