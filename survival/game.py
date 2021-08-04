from classic.game import *
from survival.paddle import *
from classic.ball import *


class SurvivalGame(Game):
    def __init__(self, win):
        super().__init__(win)

    def check_winner(self, p1, p2, ball):
        hit = ball.get_winner()
        if hit:
            ball.x_vel = 5
            ball.y_vel = 5
            self.win.fill(LIGHT_BLACK)

            file = open("survival/highscore.txt", "r+")
            highscore = file.readlines()[0]
            highscore = int(highscore.strip())
            if p1.score > highscore:
                display_text(self.win, f"NEW HIGHSCORE!", p1.color, get_font(100), (WIDTH/2 - 3, HEIGHT/2 - 30))
                display_text(self.win, f"YOU SCORED: {p1.score}", p1.color, get_font(50), (WIDTH/2 - 7, HEIGHT/2 + 10))
                file.seek(0)
                file.truncate()
                file.write(str(p1.score))
            else:
                display_text(self.win, f"YOU SCORED: {p1.score}", p1.color, get_font(100), (WIDTH/2 - 3, HEIGHT/2 - 30))
                display_text(self.win, f"CURRENT HIGHSCORE: {highscore}", p1.color, winner_font, (WIDTH/2 - 7, HEIGHT/2 + 10))
            file.close()

            ball.draw()
            p1.draw()
            p2.draw()
            ball.rect.center = (WIDTH/2 - 2, HEIGHT/2)
            p1.rect.center = (20, HEIGHT / 2)
            p2.rect.center = (WIDTH - 20, HEIGHT/2)
            p1.score = 0
            pygame.event.post(PAUSE)
        ball.winner = ""

    def display_score(self, p1):
        display_text(self.win, str(p1.score), p1.color, get_font(50), (WIDTH / 2 - 30, HEIGHT / 2))

    def run(self, p1_color, p2_color):
        p1 = Paddle(self.win, 20, HEIGHT/2 - 25, 10, 100, 10, p1_color, 1)
        p2 = SurvivalPaddle(self.win, WIDTH - 30, HEIGHT / 2 - 25, 10, 100, 10, p2_color, 2)
        ball = Ball(self.win, (WIDTH/2 - 2, HEIGHT / 2), 8, 5, 5, LIGHT_WHITE)
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
                    game_menu = menu.Menu(self.win)
                    game_menu.run()

                if event.type == pygame.USEREVENT + 1:
                    self.pause()

            self.win.fill(LIGHT_BLACK)
            self.display_border()
            p1.update()
            p2.update(ball)
            hit = ball.update(p1, p2)
            if hit:
                p1.score += 1

            p1.draw()
            p2.draw()
            self.display_score(p1)
            ball.draw()
            self.check_winner(p1, p2, ball)

            pygame.display.update()