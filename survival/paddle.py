from classic.paddle import *


class SurvivalPaddle(Paddle):
    def __init__(self, win, x, y, width, height, vel, color, player):
        super().__init__(win, x, y, width, height, vel, color, player)

    def movement(self, ball):
        self.rect.centery = ball.rect.centery

        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, ball):
        self.movement(ball)