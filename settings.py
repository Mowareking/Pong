import pygame
import os
pygame.init()
pygame.font.init()
pygame.mixer.init()


def get_font(size):
    return pygame.font.Font(os.path.join("assets", "Pixeltype.ttf"), size)


def display_text(win, text, color, font, pos):
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=pos)
    win.blit(text, text_rect)


def display_help_text(win, text, color, font, y, x=10):
    text = font.render(text, True, color)
    text_rect = text.get_rect(x=x, y=y)
    win.blit(text, text_rect)


WIDTH, HEIGHT = 900, 500
FPS = 60
ping = pygame.mixer.Sound(os.path.join("assets", "pong.ogg",))
game_over = pygame.mixer.Sound(os.path.join("assets", "game_over.wav"))
woosh = pygame.mixer.Sound(os.path.join("assets", "woosh.wav"))
score_font = winner_font = get_font(50)

LIGHT_BLACK = (64, 64, 64)  # Fight Me
LIGHT_WHITE = (251, 255, 255) # FIGHT ME

LIGHT_BLUE = (36, 248, 229)
RED = (255, 7, 58)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (176, 38, 255)
ORANGE = (255, 95, 31)
GREEN = (57, 255, 20)
PINK = (255, 16, 240)
MAROON = (128,0,0)
YELLOW = (250, 237, 39)

colors = [RED, ORANGE, YELLOW, GREEN, LIGHT_BLUE, PINK, PURPLE, MAROON, BLACK, WHITE]

dict_colors = {
    (36, 248, 229): "BLUE",
    (255, 7, 58): "RED",
    (255, 255, 255): "WHITE",
    (0, 0, 0): "BLACK",
    (176, 38, 255): "PURPLE",
    (255, 95, 31): "ORANGE",
    (57, 255, 20): "GREEN",
    (255, 16, 240): "PINK",
    (128, 0, 0): "MAROON",
    (250, 237, 39): "YELLOW"
}
