from settings import *
import pygame
pygame.init()


class Paddle:
    def __init__(self, win, x, y, width, height, vel, color, player):
        self.win = win
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = color
        self.vel = vel
        self.score = 0
        self.player = player

    def movement(self):
        keys = pygame.key.get_pressed()
        if self.player == 1:
            if keys[pygame.K_w]:
                self.rect.y -= self.vel
            if keys[pygame.K_s]:
                self.rect.y += self.vel
        elif self.player == 2:
            if keys[pygame.K_UP]:
                self.rect.y -= self.vel
            if keys[pygame.K_DOWN]:
                self.rect.y += self.vel

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self):
        self.movement()

    def draw(self):
        pygame.draw.rect(self.win, self.color, self.rect)
