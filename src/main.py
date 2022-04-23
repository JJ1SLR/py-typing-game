import sys

import pygame as pg

from src.pgf.window import Window
from one_letter_scene import OneLetterScene
from line_scene import LineScene

ONE_LETTER_SCENE = 1
LINE_SCENE = 2


class MainWindow(Window):

    def __init__(self, width: int = 640, height: int = 480, scene_type: int = ONE_LETTER_SCENE):
        super().__init__(width, height, "Typing Game")
        self.set_scene(self.get_scene(scene_type))
        picture = pg.image.load("../image/20220422235656.jpg")
        self.picture = pg.transform.scale(picture, (width, height))

    def get_scene(self, scene_type: int):
        if scene_type == ONE_LETTER_SCENE:
            return OneLetterScene(self)
        elif scene_type == LINE_SCENE:
            return LineScene(self)


def main():
    main_window = MainWindow(scene_type=LINE_SCENE)
    main_window.main_loop()


if __name__ == "__main__":
    main()
