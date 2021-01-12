import pygame

from config import WINDOW_SIZE, FPS
from game import Game
from ghost import Ghost
from labyrinth import Labyrinth
from pacman import Pacman
from energy_life import EnergyLife
from artifacts_rend import ArtifactsRender


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labyrinth = Labyrinth("map.txt", ['0', '2', 'E', 'A'], '2')
    pacman = Pacman((6, 6), labyrinth)
    ghost = Ghost((1, 1), labyrinth)
    game = Game(labyrinth, pacman, ghost)
    energy_life = EnergyLife(screen, pacman)
    artifacts_rend = ArtifactsRender(screen, 0)

    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    pacman.check_a = 'left'
                elif event.key == pygame.K_d:
                    pacman.check_a = 'right'
                elif event.key == pygame.K_w:
                    pacman.check_a = 'up'
                elif event.key == pygame.K_s:
                    pacman.check_a = 'down'
        rect_pacman = pacman.x, pacman.y
        rect_ghost = ghost.x, ghost.y
        if rect_ghost == rect_pacman and pacman.health > 0:
            pacman.health -= 20
        if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'E' and pacman.energy < 100:
            pacman.energy += 20
            labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
        if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'A' and pacman.energy < 100:
            pacman.artifacts += 1
            labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
        pacman.update_hero()
        ghost.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        artifacts_rend.render(pacman.artifacts)
        energy_life.render(pacman)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
