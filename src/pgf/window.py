import sys

import pygame as pg

from src.pgf.scene import Scene


class Window:

    def __init__(self, width: int = 640, height: int = 480, caption: str = '', fps: int = 50):
        pg.init()
        self.screen = pg.display.set_mode((width, height))
        self.clock = pg.time.Clock()
        if caption:
            pg.display.set_caption(caption)
        self.fps = fps
        self.scene = None
        self.picture = None

    def set_scene(self, scene: Scene):
        self.scene = scene

    def set_picture(self, picture: pg.Surface):
        self.picture = picture

    def main_loop(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    self.scene.on_key_down(event)
                if event.type == pg.KEYUP:
                    self.scene.on_key_up(event)

            self.clock.tick(self.fps)
            self.scene.on_draw()
            pg.display.flip()
