import pygame as pg


class Score:

    def __init__(self, x, y, w, h, text='', num=0):
        self.rect = pg.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.num = num
        self.font = pg.font.Font(None, h-5)
        self.txt_surface = self.font.render(text + ' ' + str(num), True, self.color)

    def update(self):
        self.txt_surface = self.font.render(self.text + ' ' + str(self.num), True, self.color)
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def add(self):
        self.num += 1
        self.update()

    def reset(self):
        self.num = 0
        self.update()

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Blit the rect.
        # pg.draw.rect(screen, self.color, self.rect, 2)
