from settings import *
import pygame
pygame.init()


class Button:
    def __init__(self, win, x, y, text, font, width=200, height=50, color=BLACK):
        self.win = win
        self.color = color

        self.border = pygame.Rect(0, 0, width, height)
        self.rect = pygame.Rect(0, 0, width - 10, height - 10)
        self.border.center = (x, y)
        self.rect.center = self.border.center
        self.border_color = WHITE
        self.rect_color = self.color

        self.text = text
        self.text_color = BLACK
        self.font = font

    def hovered_on(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.border_color = self.color
            self.rect_color = WHITE
            self.text_color = self.border_color
            return True
        else:
            self.border_color = WHITE
            self.rect_color = self.color
            self.text_color = self.border_color
            return False

    def update(self):
        self.hovered_on()

    def draw(self):
        self.update()
        pygame.draw.rect(self.win, self.border_color, self.border)
        pygame.draw.rect(self.win, self.rect_color, self.rect)
        display_text(self.win, self.text, self.text_color, self.font, (self.border.centerx, self.border.centery + 5))

