import sys

import pygame as pg

from one_letter_scene import OneLetterScene

ONE_LETTER_SCENE = 1


class MainWindow:

    def __init__(self, width=640, height=480):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("Typing Game")
        self.clock = pg.time.Clock()
        self.scene = MainWindow.get_scene(self.screen, ONE_LETTER_SCENE)

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

    @staticmethod
    def get_scene(screen, scene_type):
        if scene_type == ONE_LETTER_SCENE:
            return OneLetterScene(screen)


def main():
    main_window = MainWindow()
    main_window.main_loop()


if __name__ == "__main__":
    main()
