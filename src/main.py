import sys
import string
import random

import pygame as pg
import score


class MainWindow:
    def __init__(self, width=640, height=480):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        # self.speed = [3, 1]
        self.letter = random.choice(string.ascii_uppercase)
        self.scoreOK = score.Score(5, 5, 200, 30, "OK:")
        self.scoreNG = score.Score(5, 35, 200, 30, "NG:")
        self.scoreTotal = score.Score(5, 65, 200, 30, "Total:")
        self.scoreCombo = score.Score(5, height - 60 - 5, 200, 60, "COMBO:")

    def main_loop(self):
        font = pg.font.Font(None, 200)
        text = font.render(self.letter, True, (255, 255, 255))
        text_rect = text.get_rect()

        correct = False

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if pg.K_a <= event.key <= pg.K_z:
                        if event.key == ord(self.letter.lower()):
                            correct = True
                            text = font.render(self.letter, True, (0, 255, 0))
                            self.scoreOK.add()
                            self.scoreTotal.add()
                            self.scoreCombo.add()
                        else:
                            correct = False
                            text = font.render(self.letter, True, (255, 0, 0))
                            self.scoreNG.add()
                            self.scoreTotal.add()
                            self.scoreCombo.reset()
                if event.type == pg.KEYUP:
                    if correct:
                        self.letter = random.choice(string.ascii_uppercase)
                        text = font.render(self.letter, True, (255, 255, 255))
                        correct = False

            self.clock.tick(50)

            # text_rect = text_rect.move(self.speed)
            # if text_rect.left < 0 or text_rect.right > self.width:
            #     self.speed[0] = -self.speed[0]
            # if text_rect.top < 0 or text_rect.bottom > self.height:
            #     self.speed[1] = -self.speed[1]
            self.screen.fill((0, 0, 0))
            self.screen.blit(text, [(self.width - text_rect.width) / 2, (self.height - text_rect.height) / 2])
            self.scoreOK.draw(self.screen)
            self.scoreNG.draw(self.screen)
            self.scoreTotal.draw(self.screen)
            self.scoreCombo.draw(self.screen)
            pg.display.flip()


def main():
    main_window = MainWindow()
    main_window.main_loop()


if __name__ == "__main__":
    main()
