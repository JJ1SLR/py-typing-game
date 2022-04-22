import sys

import pygame as pg

from one_letter_scene import OneLetterScene
from line_scene import  LineScene

ONE_LETTER_SCENE = 1
LINE_SCENE = 2


class MainWindow:

    def __init__(self, width: int = 640, height: int = 480, scene_type: int = ONE_LETTER_SCENE):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Typing Game")
        self.clock = pg.time.Clock()
        self.scene = self.get_scene(scene_type)
        picture = pg.image.load("../image/20220422235656.jpg")
        self.picture = pg.transform.scale(picture, (640, 480))

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    self.scene.on_key_down(event)
                if event.type == pg.KEYUP:
                    self.scene.on_key_up(event)

            self.clock.tick(50)
            self.scene.on_draw()
            pg.display.flip()

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
