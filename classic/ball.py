from settings import *
import pygame
import random
pygame.init()
pygame.mixer.init()


class Ball:
    def __init__(self, win, center, radius, x_vel, y_vel, color):
        self.win = win
        self.x_vel = x_vel
        if random.randint(0, 2): self.x_vel *= -1
        self.y_vel = y_vel
        if random.randint(0, 2): self.y_vel *=  -1
        self.color = color
        self.counter = False
        self.winner = ""
        self.rect = pygame.draw.circle(self.win, self.color, center, radius)

    def movement(self):
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel

    def check_paddle_collision(self, p1, p2):
        if self.rect.colliderect(p1) or (p1.rect.bottom + 20 >= self.rect.centery >= p1.rect.top - 20 and self.rect.centerx <= p1.rect.right):
            self.color = p1.color
            self.rect.left = p1.rect.right
            self.x_vel *= -1
            if self.x_vel < 0:
                if self.counter: self.x_vel -= 1
            else:
                if self.counter: self.x_vel += 1
            if self.y_vel < 0:
                if self.counter: self.y_vel -= 1
            else:
                if self.counter: self.y_vel += 1

            self.counter = not self.counter
            ping.play()
            return True  # For Survival Mode

        if self.rect.colliderect(p2) or (p2.rect.bottom + 20 >= self.rect.centery >= p2.rect.top - 20 and self.rect.centerx >= p2.rect.left):
            self.color = p2.color
            self.rect.right = p2.rect.left
            self.x_vel *= -1
            if self.x_vel < 0:
                if self.counter: self.x_vel -= 1
            else:
                if self.counter: self.x_vel += 1
            if self.y_vel < 0:
                if self.counter: self.y_vel -= 1
            else:
                if self.counter: self.y_vel += 1
            self.counter = not self.counter
            ping.play()

    def check_wall_collision(self, p1, p2):
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
            self.y_vel *= -1
            ping.play()

        if self.rect.top <= 0:
            self.rect.top = 0
            self.y_vel *= -1
            ping.play()

        if self.rect.left <= 0:
            distance = p1.rect.right - self.rect.left - self.x_vel * -1
            distance = self.x_vel / distance
            if self.y_vel > 0:
                self.rect.y -= distance
            else:
                self.rect.y += distance  # What the Hell

            self.rect.left = 0
            if not p1.rect.bottom + 20 >= self.rect.centery >= p1.rect.top - 20 and self.rect.centerx <= p1.rect.right:
                self.winner = "p2"
                game_over.play()
            self.y_vel *= -1

        if self.rect.right >= WIDTH:
            distance = p2.rect.left - self.rect.right - self.x_vel
            distance = self.x_vel / distance
            if self.y_vel > 0:
                self.rect.y -= distance
            else:
                self.rect.y += distance  # What the Hell

            self.rect.right = WIDTH
            if not p2.rect.bottom + 20 >= self.rect.centery >= p2.rect.top - 20 and self.rect.centerx >= p2.rect.left:
                self.winner = "p1"
                game_over.play()
            self.y_vel *= -1


    def get_winner(self):
        return self.winner

    def update(self, p1, p2):
        self.movement()
        self.check_wall_collision(p1, p2)
        hit = self.check_paddle_collision(p1, p2)
        return hit  # For Survival

    def draw(self):
        pygame.draw.circle(self.win, self.color, self.rect.center, self.rect.width / 2)

