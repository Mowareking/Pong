from classic.ball import *


class MirrorBall(Ball):
    def __init__(self, win, center, radius, x_vel, y_vel, color):
        super().__init__(win, center, radius, x_vel, y_vel, color)

    def check_paddle_collision(self, p1, p2):
        if self.rect.colliderect(p1) or (p1.rect.left >= self.rect.centerx >= p1.rect.right and self.rect.centery <= p1.rect.bottom):
            self.color = p1.color
            self.rect.top = p1.rect.bottom
            self.y_vel *= -1
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

        if self.rect.colliderect(p2) or (p2.rect.left >= self.rect.centerx >= p2.rect.right and self.rect.centery >= p2.rect.top):
            self.color = p2.color
            self.rect.bottom = p2.rect.top
            self.y_vel *= -1
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
            self.winner = "p1"
            self.y_vel *= -1
            game_over.play()

        if self.rect.top <= 0:
            self.rect.top = 0
            self.winner = "p2"
            self.y_vel *= -1
            game_over.play()

        if self.rect.left <= 0:
            self.rect.left = 0
            self.x_vel *= -1
            ping.play()

        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.x_vel *= -1
            ping.play()

