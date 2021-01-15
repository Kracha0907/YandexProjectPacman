import pygame
import os

from config import TILE_SIZE, sprites_folder, game_folder, map_folder


class Labyrinth(pygame.sprite.Sprite):
    image_back = pygame.image.load(os.path.join(sprites_folder, "back.jpg"))
    image_wall = pygame.image.load(os.path.join(sprites_folder, "download"))
    image_wall = pygame.transform.scale(image_wall, (40, 40))

    image_energy = pygame.image.load(os.path.join(sprites_folder, "blue_star.png"))
    image_energy = pygame.transform.scale(image_energy, (80, 60))
    image_artifact = pygame.image.load(os.path.join(sprites_folder, "artifact.png"))
    image_artifact = pygame.transform.scale(image_artifact, (80, 60))

    def __init__(self, filename, free_tiles, finish_tile, group):
        super().__init__(group)
        self.map = []
        with open(os.path.join(map_folder, filename)) as input_file:
            for line in input_file:
                self.map.append(list(map(str, line.split())))
                print(self.map)
        self.check = 0
        self.center = [0, 0]
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tiles
        self.finish_tile = finish_tile

    def render(self, screen):
        colors = {'0': (0, 0, 0), '1': (100, 100, 255), '2': (230, 60, 60)}
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.tile_size, y * self.tile_size,
                                   self.tile_size, self.tile_size)
                if self.get_tile_id((x, y)).isdigit():
                    if self.get_tile_id((x, y)) == '1':
                        self.center_wall = [x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 2 + self.center[0],
                                            y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 2 + self.center[1]]
                        self.image = Labyrinth.image_wall
                        screen.blit(self.image, self.center_wall)
                elif self.get_tile_id((x, y)) == 'E':
                    self.center_energy = [x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5 + self.center[0],
                                          y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5 + self.center[1]]
                    self.image = Labyrinth.image_energy
                    screen.blit(self.image, self.center_energy)
                elif self.get_tile_id((x, y)) == 'A':
                    self.center_artyfact = [x * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5 + self.center[0],
                                            y * TILE_SIZE - TILE_SIZE * 2 + TILE_SIZE * 1.5 + self.center[1]]
                    self.image = Labyrinth.image_artifact
                    screen.blit(self.image, self.center_artyfact)
        self.check = 1

    def get_tile_id(self, position):
        return self.map[position[1]][position[0]]

    def is_free(self, position):
        return self.get_tile_id(position) in self.free_tiles
