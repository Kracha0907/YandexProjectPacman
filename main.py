import pygame

from config import WINDOW_SIZE, FPS
from game import Game
from ghost import Ghost
from labyrinth import Labyrinth
from pacman import Pacman


def main():
    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)

    labyrinth = Labyrinth("map.txt", [0, 2], 2)
    pacman = Pacman((6, 6), labyrinth)
    ghost = Ghost((1, 1), labyrinth)
    game = Game(labyrinth, pacman, ghost)

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
        pacman.update_hero()
        ghost.update_hero()
        screen.fill((0, 0, 0))
        game.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()