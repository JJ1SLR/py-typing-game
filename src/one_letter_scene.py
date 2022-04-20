from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import pygame as pg
    from main import MainWindow
    from widget import Widget


import pygame as pg

import letter
import score

from scene import Scene


class OneLetterScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.letter = letter.Letter(self.window.screen.get_width(), self.window.screen.get_height())
        self.add_widget(self.letter)
        self.scoreOK = score.Score(5, 5, 30, "OK:")
        self.add_widget(self.scoreOK)
        self.scoreNG = score.Score(5, 35, 30, "NG:")
        self.add_widget(self.scoreNG)
        self.scoreTotal = score.Score(5, 65, 30, "Total:")
        self.add_widget(self.scoreTotal)
        self.scoreCombo = score.Score(5, window.screen.get_height() - 60 - 5, 60, "COMBO:")
        self.add_widget(self.scoreCombo)
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
            self.correct = False
