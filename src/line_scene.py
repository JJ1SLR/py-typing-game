from __future__ import annotations
from typing import TYPE_CHECKING, Callable
if TYPE_CHECKING:
    from main import MainWindow

import pygame as pg

from src.pgf.scene import Scene

from src.pgf.button import Button

from random_line import RandomLine
from score_board import ScoreBoard
from keyboard import KeyBoard


class LineScene(Scene):

    def __init__(self, window: MainWindow):
        super().__init__(window)
        self.line = RandomLine(0, 0, parent=self.root_widget, size=90)
        self.line.set_center()
        self._new_line()
        self.scoreBoard = ScoreBoard(0, 0, parent=self.root_widget)
        self.keyboard = KeyBoard(350, 50, parent=self.root_widget)
        self.reset_button = Button(self.get_width() - 165, 5, 160, 120, 50, self.root_widget, "Reset")
        self.reset_button.set_mouse_up_handler(self.create_on_button_reset())
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")
        self.correct = False

    def create_on_button_reset(self) -> Callable:
        def on_button_reset(_button: Button, _event: pg.event.Event, _handled: bool) -> bool:
            self.scoreBoard.reset()
            self.root_widget.remove_widget(self.line)
            self.root_widget.remove_widget(self.lineNext)
            self.line = RandomLine(0, 0, parent=self.root_widget, size=90)
            self.line.set_center()
            self._new_line()
            self.keyboard.reset()
            return True
        return on_button_reset

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
                self.line = self.lineNext
                self.line.set_size(90)
                self.line.set_center()
                self._new_line()
            self.keyboard.reset()
            self.correct = False
        else:
            self.keyboard.set_current(self.line.get_current_letter())

    def _new_line(self):
        self.lineNext = RandomLine(0, 0, parent=self.root_widget)
        self.lineNext.set_position(self.line.x, self.line.y + self.line.get_height() + 5)
        self.lineNext.set_size(50)
