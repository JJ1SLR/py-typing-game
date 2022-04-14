import sys
import pygame


class MainWindow:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))

    def main_loop(self):
        font = pygame.font.Font(None, 55)
        text = font.render("hello, world", True, (255,255,255))
        self.screen.blit(text, [20, 100])
        pygame.display.update()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


def main():
    main_window = MainWindow()
    main_window.main_loop()


if __name__ == "__main__":
    main()
