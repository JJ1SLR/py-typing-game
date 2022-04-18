import sys

import pygame as pg
import score
import letter


class MainWindow:

    def __init__(self, width=640, height=480):
        pg.init()
        self.width = width
        self.height = height
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption("Typing Game")
        self.clock = pg.time.Clock()
        self.letter = letter.Letter(self.width, self.height)
        self.scoreOK = score.Score(5, 5, 200, 30, "OK:")
        self.scoreNG = score.Score(5, 35, 200, 30, "NG:")
        self.scoreTotal = score.Score(5, 65, 200, 30, "Total:")
        self.scoreCombo = score.Score(5, height - 60 - 5, 200, 60, "COMBO:")
        self.clickSnd = pg.mixer.Sound("../sound/click.wav")
        self.errorSnd = pg.mixer.Sound("../sound/error.wav")
        self.comboSnd = pg.mixer.Sound("../sound/combo.wav")

    def main_loop(self):

        correct = False

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if pg.K_a <= event.key <= pg.K_z:
                        if self.letter.judge(event.key):
                            correct = True
                            self.scoreOK.add()
                            self.scoreTotal.add()
                            self.scoreCombo.add()
                            self.clickSnd.play()
                            if self.scoreCombo.num > 1 and self.scoreCombo.num % 10 == 0:
                                self.comboSnd.play()
                        else:
                            correct = False
                            self.scoreNG.add()
                            self.scoreTotal.add()
                            self.scoreCombo.reset()
                            self.errorSnd.play()
                if event.type == pg.KEYUP:
                    if correct:
                        self.letter.next()
                        correct = False

            self.clock.tick(50)

            self.screen.fill((0, 0, 0))
            self.letter.draw(self.screen)
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
