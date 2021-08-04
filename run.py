from menu import Menu
import pygame
import os
pygame.init()

if __name__ == "__main__":
    win = pygame.display.set_mode((900, 500))
    icon = pygame.image.load(os.path.join("assets", "icon.png"))
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Pong")
    game = Menu(win)
    game.run()