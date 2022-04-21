from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

import letter
import score

from scene import Scene


class OneLetterScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.letter = letter.Letter(0, 0, scene=self)
        self.letter.set_scene_center()
        self.scoreOK = score.Score(5, 5, scene=self, text="OK:")
        self.scoreNG = score.Score(5, 35, scene=self, text="NG:")
        self.scoreTotal = score.Score(5, 65, scene=self, text="Total:")
        self.scoreCombo = score.Score(5, window.screen.get_height() - 60 - 5, scene=self, size=60, text="COMBO:")
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
            self.letter.set_scene_center()
            self.correct = False
