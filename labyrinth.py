import pygame
import os

from config import TILE_SIZE, sprites_folder


class Labyrinth:
    def __init__(self, filename, free_tiles, finish_tile):
        self.map = []
        with open(f"{filename}") as input_file:
            for line in input_file:
                self.map.append(list(map(str, line.split())))
                print(self.map)
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile
        self.background = pygame.image.load(os.path.join(sprites_folder, "back.jpg"))
        self.background = pygame.transform.scale(self.background, (1500, 840))

    def render(self, screen):
        colors = {'0': (0, 0, 0), '1': (100, 100, 255), '2': (230, 60, 60)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                if self.get_tile_id((x, y)).isdigit():
                    if self.get_tile_id((x, y)) == '1':
                        self.center = x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 2, y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 2
                        self.image = pygame.image.load(os.path.join(sprites_folder, "download"))
                        self.image = pygame.transform.scale(self.image, (40, 40))
                        screen.blit(self.image, self.center)
                elif self.get_tile_id((x, y)) == 'E':
                    self.center = x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5, y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5
                    self.image = pygame.image.load(os.path.join(sprites_folder, "blue_star.png"))
                    self.image = pygame.transform.scale(self.image, (80, 60))
                    screen.blit(self.image, self.center)
                elif self.get_tile_id((x, y)) == 'A':
                    self.center = x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5, y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5
                    self.image = pygame.image.load(os.path.join(sprites_folder, "artifact.png"))
                    self.image = pygame.transform.scale(self.image, (80, 60))
                    screen.blit(self.image, self.center)

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles
