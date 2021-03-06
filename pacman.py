import os

import pygame

from config import TILE_SIZE, sprites_folder
# Класс пакмена


class Pacman(pygame.sprite.Sprite):
    image = pygame.image.load(os.path.join(sprites_folder, "+y_ship"))

    def __init__(self, position, labyrinth, group):
        super().__init__(group)
        self.x, self.y = position
        self.labyrinth = labyrinth
        #self.center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
        self.center = [self.x * TILE_SIZE - TILE_SIZE * 8 + TILE_SIZE * 1.5, self.y * TILE_SIZE + TILE_SIZE * 3.5 + TILE_SIZE * 1.5]
        self.image = Pacman.image
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.check_a = 'up'  # Хранение направления движения
        self.check_last = 'up'
        self.health = 100
        self.energy = 0
        self.artifacts = 0

    def go_up(self, sprite):
        next_x, next_y = self.get_position()
        next_y -= 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.set_position((next_x, next_y))
            x, y = self.get_center()
            self.image = pygame.image.load(os.path.join(sprites_folder, sprite))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.set_center(x + TILE_SIZE, y - TILE_SIZE)  # Смещаем центр
            self.check_last = 'up'  # Записываем как последнее направление
            return 1
        else:
            return 2

    def go_down(self, sprite):
        next_x, next_y = self.get_position()
        next_y += 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.set_position((next_x, next_y))
            x, y = self.get_center()
            self.image = pygame.image.load(os.path.join(sprites_folder, sprite))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.set_center(x - TILE_SIZE, y + TILE_SIZE)
            self.check_last = 'down'
            return 1
        else:
            return 2

    def go_left(self, sprite):
        next_x, next_y = self.get_position()
        next_x -= 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.set_position((next_x, next_y))
            x, y = self.get_center()
            self.image = pygame.image.load(os.path.join(sprites_folder, sprite))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.set_center(x - TILE_SIZE, y - TILE_SIZE)
            self.check_last = 'left'
            return 1
        else:
            return 2

    def go_right(self, sprite):
        next_x, next_y = self.get_position()
        next_x += 1
        if self.labyrinth.is_free((next_x, next_y)):
            self.set_position((next_x, next_y))
            x, y = self.get_center()
            self.image = pygame.image.load(os.path.join(sprites_folder, sprite))
            self.image = pygame.transform.scale(self.image, (100, 100))
            self.set_center(x + TILE_SIZE, y + TILE_SIZE)
            self.check_last = 'right'
            return 1
        else:
            return 2

    def update_hero(self):
        next_x, next_y = self.get_position()
        if self.check_a == 'up':
            go_event = self.go_up("-x_ship")
            if go_event == 2:  # Обновляем напрваление
                self.check_a = self.check_last
        elif self.check_a == 'right':
            go_event = self.go_right("+y_ship")
            if go_event == 2:
                self.check_a = self.check_last
        elif self.check_a == 'down':
            go_event = self.go_down("+x_ship")
            if go_event == 2:
                self.check_a = self.check_last
        elif self.check_a == 'left':
            go_event = self.go_left("-y_ship")
            if go_event == 2:
                self.check_a = self.check_last

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def get_center(self):
        return self.center

    def set_center(self, x, y):
        self.center = [x, y]

    def render(self, screen):
        screen.blit(self.image, self.center)
