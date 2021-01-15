import pygame
import os

from config import WINDOW_SIZE, FPS, sprites_folder, TILE_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT
from game import Game
from ghost import Ghost
from labyrinth import Labyrinth
from pacman import Pacman
from energy_life import EnergyLife
from artifacts_rend import ArtifactsRender
# Класс камеры


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.center[0] += self.dx
        obj.center[1] += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.center[0] + TILE_SIZE // 2 - WINDOW_WIDTH // 2)
        self.dy = -(target.center[1] + TILE_SIZE // 2 - WINDOW_HEIGHT // 2)
# Класс уровня


class GameLevel:
    def __init__(self, pacman_coords, ghost_coords, artifacts_count, name_map):
        self.pacman_coords = pacman_coords
        self.ghost_coords = ghost_coords
        self.ghosts = []
        self.rect_ghost_last = []
        self.rect_ghost = []
        self.artifacts_count = artifacts_count
        self.name_map = name_map
        self.background = pygame.image.load(os.path.join(sprites_folder, "back.jpg"))
        self.background = pygame.transform.scale(self.background, WINDOW_SIZE)

    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(WINDOW_SIZE)
        all_sprites = pygame.sprite.Group()

        labyrinth = Labyrinth(self.name_map, ['0', '2', 'E', 'A'], '2', all_sprites)
        self.pacman = Pacman(self.pacman_coords, labyrinth, all_sprites)
        self.pacman.artifacts = self.artifacts_count  # Присваиваем пакмену то количество артефактов,
        # которое было на прошлом уровне
        for i in self.ghost_coords:
            self.ghosts.append(Ghost(i, labyrinth, all_sprites))  # Заполняем массив призраков
        game = Game(labyrinth, self.pacman, self.ghosts)
        camera = Camera()  # Создаем камеру
        energy_life = EnergyLife(screen, self.pacman)  # Создаем полоску энергии
        artifacts_rend = ArtifactsRender(screen, 0) # Создаем полоску здоровья
        rect_pacman_last = 0, 0
        for i in self.ghosts:
            i.rect_ghost_last = 0, 0

        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    # Записываем в переменную check_a, куда пойдет пакмен
                    if event.key == pygame.K_a:
                        self.pacman.check_a = 'left'
                    elif event.key == pygame.K_d:
                        self.pacman.check_a = 'right'
                    elif event.key == pygame.K_w:
                        self.pacman.check_a = 'up'
                    elif event.key == pygame.K_s:
                        self.pacman.check_a = 'down'
            rect_pacman = self.pacman.x, self.pacman.y
            for i in self.ghosts:
                i.rect_ghost = i.x, i.y
                # Обрабатываем коллизию пакмена с привидениями
                if i.rect_ghost == rect_pacman and self.pacman.health > 0:
                    self.pacman.health -= 20
                elif rect_pacman == i.rect_ghost_last and i.rect_ghost == rect_pacman_last and self.pacman.health > 0:
                    self.pacman.health -= 20
                rect_pacman_last = rect_pacman
                i.rect_ghost_last = i.rect_ghost
            # Обработка коллизии с клочком энергии
            if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'E' and self.pacman.energy < 100:
                self.pacman.energy += 20
                labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
            # Обработка коллизии с артефактом
            if labyrinth.map[rect_pacman[1]][rect_pacman[0]] == 'A' and self.pacman.energy < 100:
                self.pacman.artifacts += 1
                labyrinth.map[rect_pacman[1]][rect_pacman[0]] = '0'
            screen.blit(self.background, (0, 0))
            self.pacman.update_hero()
            for i in self.ghosts:
                i.update_hero()
            # изменяем ракурс камеры на пакмена
            camera.update(self.pacman)
            # обновляем положение всех спрайтов
            for sprite in all_sprites:
                print(sprite)
                camera.apply(sprite)
            game.render(screen) # Отрисовываем всех спрайтов
            artifacts_rend.render(self.pacman.artifacts)  # Отрисовываем количество артефактов пакмена
            energy_life.render(self.pacman)  # Отрисовываем полоску энергии и жизни пакмена
            if self.pacman.energy >= 100 or self.pacman.health <= 0:  # Если пакмен умирает или восполняет всю энергию
                # прекращаем работу функции
                break
            pygame.display.flip()
            clock.tick(FPS)
            self.artifacts_count = self.pacman.artifacts  # Сохраняем счет пакмена, для передачи его на следующем уровне
        pygame.quit()
