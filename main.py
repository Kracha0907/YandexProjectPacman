import pygame

from config import WINDOW_SIZE, FPS
from game import Game
from ghost import Ghost
from labyrinth import Labyrinth
from pacman import Pacman
from energy_life import EnergyLife
from artifacts_rend import ArtifactsRender


class GameLevel:
    def __init__(self, pacman_coords, ghost_coords, artifacts_count, name_map):
        self.pacman_coords = pacman_coords
        self.ghost_coords = ghost_coords
        self.artifacts_count = artifacts_count
        self.name_map = name_map

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(WINDOW_SIZE)
        all_sprites = pygame.sprite.Group()

        labyrinth = Labyrinth(self.name_map, ['0', '2', 'E', 'A'], '2', all_sprites)
        self.pacman = Pacman(self.pacman_coords, labyrinth, all_sprites)
        self.pacman.artifacts = self.artifacts_count
        ghost = Ghost(self.ghost_coords, labyrinth, all_sprites)
        game = Game(labyrinth, self.pacman, ghost)
        energy_life = EnergyLife(screen, self.pacman)
        artifacts_rend = ArtifactsRender(screen, 0)

        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.pacman.check_a = 'left'
                    elif event.key == pygame.K_d:
                        self.pacman.check_a = 'right'
                    elif event.key == pygame.K_w:
                        self.pacman.check_a = 'up'
                    elif event.key == pygame.K_s:
                        self.pacman.check_a = 'down'
            rect_pacman = self.pacman.x, self.pacman.y
            rect_ghost = ghost.x, ghost.y
            if rect_ghost == rect_pacman and self.pacman.health > 0:
                self.pacman.health -= 20
            if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'E' and self.pacman.energy < 100:
                self.pacman.energy += 20
                labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
            if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'A' and self.pacman.energy < 100:
                self.pacman.artifacts += 1
                labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
            self.pacman.update_hero()
            ghost.update_hero()
            screen.fill((0, 0, 0))
            game.render(screen)
            artifacts_rend.render(self.pacman.artifacts)
            energy_life.render(self.pacman)
            if self.pacman.energy >= 100 or self.pacman.health <= 0:
                break
            pygame.display.flip()
            clock.tick(FPS)
            self.artifacts_count = self.pacman.artifacts
        pygame.quit()
