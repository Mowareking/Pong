from classic.game import *
from .ball import *


class RumbleGame(Game):
    def __init__(self, win):
        super().__init__(win)
        self.mode = ""

    def check_winner(self, p1, p2, balls):
        winner = balls[0].get_winner()
        if not winner and len(balls) == 2:
            winner = balls[1].get_winner()

        if winner:
            balls[0] = Ball(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, 5, 5, LIGHT_WHITE)
            if random.randint(0, 2): balls[0].x_vel *= -1
            if random.randint(0, 2): balls[0].y_vel *= -1
            self.win.fill(LIGHT_BLACK)

            if len(balls) == 2:
                balls[1].draw()
                balls.pop()

            balls[0].draw()
            p1.draw()
            p2.draw()
            balls[0].rect.center = (WIDTH / 2 - 2, HEIGHT / 2)
            p1.rect.center = (20, HEIGHT / 2)
            p2.rect.center = (WIDTH - 20, HEIGHT / 2)

            modes = ["BIG PADDLES", "SMALL PADDLES", "BIG BALL", "SMALL BALL", "FAST PADDLES", "SLOW PADDLES", "SWAP", "EXTRA BALL", "FAZE BALL", "INSANE"]
            self.mode = random.choice(modes)

            if self.mode == "INSANE":
                p1.rect.height = random.randint(50, 151)
                p2.rect.height = random.randint(50, 151)
                p1.vel = random.randint(5, 16)
                p2.vel = random.randint(5, 16)
                balls.pop()
                x_vel = y_vel = random.randint(2, 8)
                balls.append(FazeBall(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, x_vel, y_vel, LIGHT_WHITE))

            if self.mode == "BIG PADDLES":
                p1.rect.height = p2.rect.height = 150
                p1.vel = p2.vel = 10
            if self.mode == "SMALL PADDLES":
                p1.rect.height = p2.rect.height = 50
                p1.vel = p2.vel = 10
            if self.mode == "BIG BALL":
                balls[0].rect.width = 30
                p1.rect.height = p2.rect.height = 100
                p1.vel = p2.vel = 10
            if self.mode == "SMALL BALL":
                balls[0].rect.width = 5
                p1.rect.height = p2.rect.height = 100
                p1.vel = p2.vel = 10
            if self.mode == "FAST PADDLES":
                p1.rect.height = p2.rect.height = 100
                p1.vel = p2.vel = 15
            if self.mode == "SLOW PADDLES":
                p1.rect.height = p2.rect.height = 100
                p1.vel = p2.vel = 5
            if self.mode == "SWAP":
                p1.rect.center, p2.rect.center = p2.rect.center, p1.rect.center
                p1.rect.height = p2.rect.height = 100
                p1.vel = p2.vel = 10
            if self.mode == "EXTRA BALL":
                x_vel = y_vel = random.randint(2, 8)
                if x_vel == 5:
                    x_vel += 1
                    y_vel += 1

                balls.append(Ball(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, x_vel, y_vel, LIGHT_WHITE))
                if balls[0].x_vel > 0 and balls[1].x_vel > 0: balls[1].x_vel *= -1
                if balls[0].y_vel > 0 and balls[1].y_vel > 0: balls[1].y_vel *= -1

            if self.mode == "FAZE BALL":
                balls[0] = FazeBall(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, 5, 5, LIGHT_WHITE)
                if random.randint(0, 2): balls[0].x_vel *= -1
                if random.randint(0, 2): balls[0].y_vel *= -1

            bug_fix_rect = pygame.Rect(0, 0, 100, 100)
            bug_fix_rect.center = (WIDTH/2, HEIGHT/2)
            pygame.draw.rect(self.win, LIGHT_BLACK, bug_fix_rect)

            if winner == "p1":
                p1.score += 1
                display_text(self.win, f"{dict_colors[p1.color]} WINS!", p1.color, get_font(100),
                             (WIDTH / 2 - 3, HEIGHT / 2 - 30))
                display_text(self.win, f"NEXT MODE: {self.mode}", p1.color, get_font(50), (WIDTH / 2 - 10, HEIGHT / 2 + 10))
                display_text(self.win, "PRESS SPACE", p1.color, get_font(50),
                             (WIDTH / 2 - 10, HEIGHT / 2 + 40))
            else:
                p2.score += 1
                display_text(self.win, f"{dict_colors[p2.color]} WINS!", p2.color, get_font(100),
                             (WIDTH / 2 - 3, HEIGHT / 2 - 30))
                display_text(self.win, f"NEXT MODE: {self.mode}", p2.color, get_font(50), (WIDTH / 2 - 10, HEIGHT / 2 + 10))
                display_text(self.win, "PRESS SPACE", p2.color, get_font(50),
                             (WIDTH / 2 - 10, HEIGHT / 2 + 40))

            pygame.event.post(PAUSE)
        balls[0].winner = ""

    def display_score(self, p1, p2):
        if self.mode == "SWAP":
            display_text(self.win, str(p2.score), p2.color, get_font(50), (WIDTH/2 - 30, HEIGHT/2))
            display_text(self.win, str(p1.score), p1.color, get_font(50), (WIDTH/2 + 28, HEIGHT/2))
        else:
            display_text(self.win, str(p1.score), p1.color, get_font(50), (WIDTH/2 - 30, HEIGHT/2))
            display_text(self.win, str(p2.score), p2.color, get_font(50), (WIDTH/2 + 28, HEIGHT/2))

    def run(self, p1_color, p2_color):
        p1 = Paddle(self.win, 20, HEIGHT / 2 - 25, 10, 100, 10, p1_color, 1)
        p2 = Paddle(self.win, WIDTH - 30, HEIGHT / 2 - 25, 10, 100, 10, p2_color, 2)
        ball = Ball(self.win, (WIDTH/2 - 2, HEIGHT/2), 8, 5, 5, LIGHT_WHITE)
        balls = [ball]
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

            p1.draw()
            p2.draw()
            self.display_score(p1, p2)
            for ball in balls:
                if not self.mode == "SWAP":
                    ball.update(p1, p2)
                else:
                    ball.update(p2, p1)
                ball.draw()
            self.check_winner(p1, p2, balls)
            pygame.display.update()

