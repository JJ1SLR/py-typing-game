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
        self.speed = [3, 1]
        self.letter = random.choice(string.ascii_uppercase)
        self.letter_change_counter = 0

    def main_loop(self):
        font = pygame.font.Font(None, 55)
        text = font.render(self.letter, True, (255, 255, 255))
        text_rect = text.get_rect()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.clock.tick(50)

            text_rect = text_rect.move(self.speed)
            if text_rect.left < 0 or text_rect.right > self.width:
                self.speed[0] = -self.speed[0]
            if text_rect.top < 0 or text_rect.bottom > self.height:
                self.speed[1] = -self.speed[1]

            self.letter_change_counter += 1
            if self.letter_change_counter % 30 == 0:
                self.letter = random.choice(string.ascii_uppercase)
                text = font.render(self.letter, True, (255, 255, 255))
                self.letter_change_counter = 0

            self.screen.fill((0, 0, 0))
            self.screen.blit(text, text_rect)
            pygame.display.flip()


def main():
    main_window = MainWindow()
    main_window.main_loop()


if __name__ == "__main__":
    main()
