from classic.ball import *


class FazeBall(Ball):
    def __init__(self, win, center, radius, x_vel, y_vel, color):
        super().__init__(win, center, radius, x_vel, y_vel, color)

    def check_wall_collision(self, p1, p2):
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0
            woosh.play()

        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
            woosh.play()

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