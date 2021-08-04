from .paddle import *
from .ball import *
import menu
import pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

PAUSE = pygame.event.Event(pygame.USEREVENT + 1)


class Game:
    def __init__(self, win):
        self.win = win

    def display_border(self):
        pygame.draw.line(self.win, WHITE, (WIDTH/2 - 2.5, 0), (WIDTH/2 - 2.5, HEIGHT), 5)

    def check_winner(self, p1, p2, ball):
        winner = ball.get_winner()
        if winner:
            ball.x_vel = 5
            ball.y_vel = 5
            self.win.fill(LIGHT_BLACK)

            ball.draw()
            p1.draw()
            p2.draw()
            ball.rect.center = (WIDTH / 2 - 2, HEIGHT / 2)
            p1.rect.center = (20, HEIGHT / 2)
            p2.rect.center = (WIDTH - 20, HEIGHT / 2)
            if winner == "p1":
                p1.score += 1
                display_text(self.win, f"{dict_colors[p1.color]} WINS!", p1.color, get_font(100), (WIDTH/2 - 3, HEIGHT/2 - 30))
                display_text(self.win, f"PRESS SPACE", p1.color, get_font(50), (WIDTH / 2 - 10, HEIGHT / 2 + 10))
            else:
                p2.score += 1
                display_text(self.win, f"{dict_colors[p2.color]} WINS!", p2.color, get_font(100), (WIDTH/2 - 3, HEIGHT/2 - 30))
                display_text(self.win, f"PRESS SPACE", p2.color, get_font(50), (WIDTH/2 - 10, HEIGHT/2 + 10))

            pygame.event.post(PAUSE)
        ball.winner = ""

    def display_score(self, p1, p2):
        display_text(self.win, str(p1.score), p1.color, get_font(50), (WIDTH/2 - 30, HEIGHT/2))
        display_text(self.win, str(p2.score), p2.color, get_font(50), (WIDTH/2 + 28, HEIGHT/2))

    def run(self, p1_color, p2_color):
        p1 = Paddle(self.win, 20, HEIGHT / 2 - 25, 10, 100, 10, p1_color, 1)
        p2 = Paddle(self.win, WIDTH - 30, HEIGHT / 2 - 25, 10, 100, 10, p2_color, 2)
        ball = Ball(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, 5, 5, LIGHT_WHITE)
        clock = pygame.time.Clock()
        run = True

        self.pause_start(p1, p2, ball)

        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ping.play()
                    game_menu = menu.Menu(self.win)
                    game_menu.run()

                if event.type == pygame.USEREVENT + 1:
                    self.pause()

            self.win.fill(LIGHT_BLACK)
            self.display_border()
            p1.update()
            p2.update()
            ball.update(p1, p2)

            p1.draw()
            p2.draw()
            self.display_score(p1, p2)
            ball.draw()
            self.check_winner(p1, p2, ball)

            pygame.display.update()

    def pause(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_menu = menu.Menu(self.win)
                    game_menu.run()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        waiting = False

    def pause_start(self, p1, p2, ball):
        self.win.fill(LIGHT_BLACK)
        p1.draw()
        p2.draw()
        ball.draw()
        display_text(self.win, f"PRESS SPACE", WHITE, get_font(50), (WIDTH / 2 - 5, HEIGHT / 2 - 40))
        pygame.display.update()
        pygame.event.post(PAUSE)