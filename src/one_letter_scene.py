from __future__ import annotations
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

from src.pgf.letter import Letter
from src.pgf.scene import Scene
from score_board import ScoreBoard

from src.pgf.button import Button


class OneLetterScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.letter = Letter(0, 0, parent=self.root_widget)
        self.letter.set_center()
        self.scoreBoard = ScoreBoard(0, 0, parent=self.root_widget)
        self.reset_button = Button(self.get_width() - 165, 5, 160, 120, 50, self.root_widget, "Reset")
        self.reset_button.set_mouse_up_handler(self.create_on_button_reset())
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")
        self.correct = False

    def create_on_button_reset(self) -> Callable:
        def on_button_reset(_button: Button, _event: pg.event.Event, _handled: bool) -> bool:
            self.scoreBoard.reset()
            self.letter.next()
            self.letter.set_center()
            return True
        return on_button_reset

    def on_key_down(self, event: pg.event.Event):
        if pg.K_a <= event.key <= pg.K_z:
            if self.letter.judge(event.key):
                self.correct = True
                self.scoreBoard.add_ok()
                self.clickSnd.play()
                if self.scoreBoard.get_combo() > 1 and self.scoreBoard.get_combo() % 10 == 0:
                    self.comboSnd.play()
            else:
                self.correct = False
                self.scoreBoard.add_ng()
                self.errorSnd.play()

    def on_key_up(self, event: pg.event.Event):
        if self.correct:
            self.letter.next()
            self.letter.set_center()
            self.correct = False
