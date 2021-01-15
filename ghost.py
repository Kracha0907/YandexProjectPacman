import os

import pygame
import random

from config import sprites_folder, TILE_SIZE
from pacman import Pacman
# Класс приведения


class Ghost(Pacman):
    image = pygame.image.load(os.path.join(sprites_folder, "приведение_вверх.png"))

    def __init__(self, position, labyrinth, group):
        super().__init__(position, labyrinth, group)
        self.image = Ghost.image
        self.center = [self.x * TILE_SIZE - TILE_SIZE * 3 + TILE_SIZE * 1.5,
                       self.y * TILE_SIZE - TILE_SIZE * 1.5 + TILE_SIZE * 1.5]
        self.rect_ghost_last = None # Координаты прямоугольника привидения последнего отображения
        self.rect_ghost = None # Текущие координаты прямоугольника приведения

    def update_hero(self):
        # Проверка на возможность идти дальше
        next_x, next_y = self.get_position()
        if self.check_a == 'up':
            go_event = self.go_up("приведение_вверх.png")
            if go_event == 2: # Если идти дальшек нельзя, то выбираем случайное направление
                self.check_a = random.choice(['right', 'down', 'left'])
        elif self.check_a == 'right':
            go_event = self.go_right("приведение_вправо.png")
            if go_event == 2:
                self.check_a = random.choice(['up', 'down', 'left'])
        elif self.check_a == 'down':
            go_event = self.go_down("приведение_вниз.png")
            if go_event == 2:
                self.check_a = random.choice(['right', 'up', 'left'])
        elif self.check_a == 'left':
            go_event = self.go_left("приведение_влево.png")
            if go_event == 2:
                self.check_a = random.choice(['right', 'down', 'up'])
