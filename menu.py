import classic.game
import survival.game
import mirror.game
import rumble.game
from settings import *
from button import *
import pygame
pygame.init()
pygame.mixer.init()


class Menu:
    def __init__(self, win):
        self.win = win

    def controls(self):
        run = True
        back_button = Button(self.win, WIDTH/2, HEIGHT - 70, "BACK", get_font(50))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.hovered_on():
                    ping.play()
                    run = False
                    self.run()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run = False
                    self.run()

            self.win.fill(LIGHT_BLACK)
            display_text(self.win, "CONTROLS", WHITE, get_font(120), (WIDTH/2, 60))
            display_help_text(self.win, "PLAYER 1 -", WHITE, get_font(50),70)
            display_help_text(self.win, "UP ARROW - UP / LEFT ARROW - LEFT (MIRROR)", WHITE, get_font(40), 110)
            display_help_text(self.win, "DOWN ARROW - DOWN / RIGHT ARROW - RIGHT (MIRROR)", WHITE, get_font(40), 140)
            display_help_text(self.win, "PLAYER 2 -", WHITE, get_font(50), 180)
            display_help_text(self.win, "W - UP / A - LEFT (MIRROR)", WHITE, get_font(40), 220)
            display_help_text(self.win, "S - DOWN / D - RIGHT (MIRROR)", WHITE, get_font(40), 250)
            display_help_text(self.win, "ESC - BACK TO MENU", WHITE, get_font(50), 310)

            back_button.draw()

            pygame.display.update()

    def gamemode(self):
        run = True
        survival_button = Button(self.win, WIDTH/2, HEIGHT/2 - 85, "SURVIVAL", get_font(50))
        classic_button = Button(self.win, WIDTH/2, HEIGHT/2 - 28, "CLASSIC", get_font(50))
        mirror_button = Button(self.win, WIDTH/2, HEIGHT/2 + 28, "MIRROR", get_font(50))
        rumble_button = Button(self.win, WIDTH/2, HEIGHT/2 + 85, "RUMBLE", get_font(50))
        back_button = Button(self.win, WIDTH/2, HEIGHT - 70, "BACK", get_font(50))

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and survival_button.hovered_on():
                    ping.play()
                    run = False
                    self.choose_color("survival")

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and classic_button.hovered_on():
                    ping.play()
                    run = False
                    self.choose_color("classic")

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mirror_button.hovered_on():
                    ping.play()
                    run = False
                    self.choose_color("mirror")

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and rumble_button.hovered_on():
                    ping.play()
                    run = False
                    self.choose_color("rumble")

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.hovered_on():
                    ping.play()
                    run = False
                    self.run()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ping.play()
                    run = False
                    self.run()

            self.win.fill(LIGHT_BLACK)

            display_text(self.win, "GAMEMODE", WHITE, get_font(120), (WIDTH/2, 60))

            survival_button.draw()
            classic_button.draw()
            mirror_button.draw()
            rumble_button.draw()
            back_button.draw()

            pygame.display.update()

    def help(self):
        run = True
        back_button = Button(self.win, WIDTH/2, HEIGHT - 70, "BACK", get_font(50))

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button.hovered_on():
                    ping.play()
                    run = False
                    self.run()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ping.play()
                    run = False
                    self.run()

            self.win.fill(LIGHT_BLACK)
            display_text(self.win, "HELP", WHITE, get_font(120), (WIDTH/2, 60))
            display_help_text(self.win, "GAMEMODES:", WHITE, get_font(60), 100)
            display_help_text(self.win, "SURVIVAL - HOW HIGH CAN YOU SCORE?", WHITE, get_font(50), 140)
            display_help_text(self.win, "PS: IT IS IMPOSSIBLE TO WIN", WHITE, get_font(50), 170)
            display_help_text(self.win, "CLASSIC - NORMAL 2 PLAYER PONG", WHITE, get_font(50), 200)
            display_help_text(self.win, "MIRROR - PONG BUT DIZZY", WHITE, get_font(50), 230)
            display_help_text(self.win, "RUMBLE - PONG WITH POWERUPS! GET READY TO RUMBLE", WHITE, get_font(50), 260)
            display_help_text(self.win, "Made by Jahin Rahman", WHITE, get_font(40), HEIGHT - 30, 630)

            back_button.draw()

            pygame.display.update()

    def run(self):
        run = True
        gamemode_button = Button(self.win, WIDTH/2, HEIGHT/2 - 85, "GAMEMODE", get_font(50))
        control_button = Button(self.win, WIDTH/2, HEIGHT/2 - 28, "CONTROLS", get_font(50))
        help_button = Button(self.win, WIDTH/2, HEIGHT/2 + 28, "HELP", get_font(50))
        exit_button = Button(self.win, WIDTH/2, HEIGHT - 70, "EXIT", get_font(50))

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if gamemode_button.hovered_on():
                        ping.play()
                        run = False
                        self.gamemode()

                    elif control_button.hovered_on():
                        ping.play()
                        run = False
                        self.controls()

                    elif help_button.hovered_on():
                        ping.play()
                        run = False
                        self.help()

                    elif exit_button.hovered_on():
                        pygame.quit()
                        quit()

            self.win.fill(LIGHT_BLACK)

            display_text(self.win, "PONG", WHITE, get_font(120), (WIDTH/2, 60))

            gamemode_button.draw()
            control_button.draw()
            help_button.draw()
            exit_button.draw()

            pygame.display.update()

    def choose_color(self, game_mode):
        player = 1
        p1_color = ""
        p2_color = ""
        buttons = []
        run = True
        back_button = Button(self.win, WIDTH/2, HEIGHT - 70, "BACK", get_font(50))

        for i in range(1, 11):
            current_button = Button(self.win, 100 + i * 60, HEIGHT/2, "", get_font(10), width=50, height=50, color=colors[i-1])
            buttons.append(current_button)

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in buttons:
                        if button.hovered_on():
                            ping.play()
                            if player == 1:
                                p1_color = button.color
                            else:
                                p2_color = button.color

                            player += 1
                            buttons.remove(button)
                            pass

                    if back_button.hovered_on():
                        ping.play()
                        run = False
                        self.gamemode()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ping.play()
                    run = False
                    self.run()

            self.win.fill(LIGHT_BLACK)

            display_text(self.win, f"PLAYER {player} CHOOSE COLOUR", WHITE, get_font(120), (WIDTH/2, 60))

            for button in buttons:
                button.draw()

            back_button.draw()

            if player > 2:
                if game_mode == "survival":
                    game = survival.game.SurvivalGame(self.win)
                    game.run(p1_color, p2_color)
                if game_mode == "classic":
                    game = classic.game.Game(self.win)
                    game.run(p1_color, p2_color)
                if game_mode == "rumble":
                    game = rumble.game.RumbleGame(self.win)
                    game.run(p1_color, p2_color)
                if game_mode == "mirror":
                    game = mirror.game.MirrorGame(self.win)
                    game.run(p1_color, p2_color)

            pygame.display.update()
