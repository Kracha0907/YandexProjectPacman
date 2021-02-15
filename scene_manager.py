from main import GameLevel
from zastavka import *

# Данные по каждой сцене
game_data = {"pacman_coords": [(6, 6), (6, 6), (6, 6), (6, 6)],
             "ghost_coords": [[(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1)],
                              [(1, 1), (1, 1), (1, 1)]],
             "map_name": ["map1.txt", "map2.txt", "map3.txt", "map4.txt"]}


def update_file(score):  # Обновление файла
    f = open('scores_info.txt', 'a')
    f.write(str(score))
    f.write('\n')
    f.close()


def deathOrFinal(image):  # Вывод картинки GameOver или YouWin
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("My Game")
    screen.fill(BLACK)
    img_dir = os.path.join(path.dirname(__file__), 'sprites')
    background = pygame.image.load(os.path.join(img_dir, image)).convert()
    background_rect = background.get_rect()
    if image == "you-win.jpg":
        screen.blit(background, (WINDOW_WIDTH // 2 - background_rect.width // 2,
                                 WINDOW_HEIGHT // 2 - background_rect.height // 2,
                                 background_rect.width, background_rect.height))
    else:
        screen.blit(background, background_rect)
    pygame.display.flip()
    time.sleep(1)


class Scene_manager:
    def __init__(self):
        self.artifacts = 0  # Заводим переменную для подсчета артефактов пакмена после прохождения уровня
        self.death = False

    def scenes_loop(self, img_dir=None, WIDTH=None, HEIGHT=None):
        pygame.init()
        pygame.font.init()
        n = 1
        story_tell(n)  # Функция воспроизведения всех катсцен
        for i in range(4):
            n += 1
            game = GameLevel(game_data["pacman_coords"][i], game_data["ghost_coords"][i], self.artifacts,
                             game_data["map_name"][i])
            game.main()
            if game.pacman.health <= 0:  # В случае смерти показываем GameOver и закрываем сцену
                deathOrFinal("game-over.jpg")
                self.death = True
                break
            story_tell(n)
            self.artifacts = game.artifacts_count
        if not self.death:  # Если в конце пакмен не умер, то игра пройдена
            deathOrFinal("you-win.jpg")
        update_file(self.artifacts)  # Сохранение счета
        pygame.time.delay(100)
        pygame.quit()
