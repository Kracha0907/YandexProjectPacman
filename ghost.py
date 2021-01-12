import os

import pygame
import random

from config import sprites_folder
from pacman import Pacman


class Ghost(Pacman):
    def __init__(self, position, labyrinth):
        super().__init__(position, labyrinth)
        self.image = pygame.image.load(os.path.join(sprites_folder, "приведение_вверх.png"))

    def update_hero(self):
        next_x, next_y = self.get_position()
        if self.check_a == 'up':
            go_event = self.go_up("приведение_вверх.png")
            if go_event == 2:
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
