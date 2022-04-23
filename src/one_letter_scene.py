from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

from src.pgf.letter import Letter
from src.pgf.score import Score
from src.pgf.scene import Scene


class OneLetterScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.letter = Letter(0, 0, parent=self.root_widget)
        self.letter.set_center()
        self.scoreOK = Score(5, 5, parent=self.root_widget, text="OK:")
        self.scoreNG = Score(5, 35, parent=self.root_widget, text="NG:")
        self.scoreTotal = Score(5, 65, parent=self.root_widget, text="Total:")
        self.scoreCombo = Score(5, window.screen.get_height() - 60 - 5, parent=self.root_widget, size=60,
                                text="COMBO:")
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")
        self.correct = False

    def on_key_down(self, event: pg.event.Event):
        if pg.K_a <= event.key <= pg.K_z:
            if self.letter.judge(event.key):
                self.correct = True
                self.scoreOK.add()
                self.scoreTotal.add()
                self.scoreCombo.add()
                self.clickSnd.play()
                if self.scoreCombo.num > 1 and self.scoreCombo.num % 10 == 0:
                    self.comboSnd.play()
            else:
                self.correct = False
                self.scoreNG.add()
                self.scoreTotal.add()
                self.scoreCombo.reset()
                self.errorSnd.play()

    def on_key_up(self, event: pg.event.Event):
        if self.correct:
            self.letter.next()
            self.letter.set_center()
            self.correct = False
