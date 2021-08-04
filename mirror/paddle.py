from classic.paddle import *


class MirrorPaddle(Paddle):
    def __init__(self, win, x, y, width, height, vel, color):
        super().__init__(win, x, y, width, height, vel, color)

    def movement(self):
        keys = pygame.key.get_pressed()
        if self.rect.y < HEIGHT/2:
            if keys[pygame.K_a]:
                self.rect.x -= self.vel
            if keys[pygame.K_d]:
                self.rect.x += self.vel
        else:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.vel
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.vel

        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH