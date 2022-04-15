import sys
import string
import random

import pygame


class MainWindow:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        # self.speed = [3, 1]
        self.letter = random.choice(string.ascii_uppercase)

    def main_loop(self):
        font = pygame.font.Font(None, 200)
        text = font.render(self.letter, True, (255, 255, 255))
        text_rect = text.get_rect()

        correct = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if pygame.K_a <= event.key <= pygame.K_z:
                        if event.key == ord(self.letter.lower()):
                            correct = True
                            text = font.render(self.letter, True, (0, 255, 0))
                        else:
                            correct = False
                            text = font.render(self.letter, True, (255, 0, 0))
                if event.type == pygame.KEYUP:
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
            pygame.display.flip()


def main():
    main_window = MainWindow()
    main_window.main_loop()


if __name__ == "__main__":
    main()
