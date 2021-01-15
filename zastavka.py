import pygame
import os
import time
from os import path
from config import *


def story_tell(n):  # Показывание катсцены после уровня
    img_dir = os.path.join(path.dirname(__file__), 'sprites')
    WIDTH = 1500
    HEIGHT = 843
    BLACK = (0, 0, 0)
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    running = 0
    if n == 1:
        t = "fon1.jpg"
    elif n == 2:
        t = "fon2.jpg"
    elif n == 3:
        t = "fon3.jpg"
    elif n == 4:
        t = "fon4.jpg"
    elif n == 5:
        t = "fon5.jpg"
    elif n == -1:
        t = "game-over.jpg"
    while running <= 5:
        screen.fill(BLACK)
        background = pygame.image.load(os.path.join(img_dir, t)).convert()
        background_rect = background.get_rect()
        screen.blit(background, background_rect)
        pygame.display.flip()
        time.sleep(1)
        running = running + 1
