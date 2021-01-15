# from scenes.game_lvl1 import GameLevel as g1
from main import GameLevel
from zastavka import *

game_data = {"pacman_coords": [(6, 6), (6, 6), (6, 6), (6, 6)],
             "ghost_coords": [(1, 1), (1, 1), (1, 1), (1, 1)],
             "map_name": ["map1.txt", "map2.txt", "map3.txt", "map4.txt"]}


def update_file(score):
    f = open('scores_info.txt', 'a')
    f.write(str(score))
    f.write('\n')
    f.close()


class Scene_manager():
    def __init__(self):
        self.artifacts = 0

    def scenes_loop(self):
        pygame.init()
        pygame.font.init()
        n = 1
        story_tell(n)
        for i in range(4):
            n += 1
            game = GameLevel(game_data["pacman_coords"][i], game_data["ghost_coords"][i], self.artifacts,
                             game_data["map_name"][i])
            game.main()
            if game.pacman.health <= 0:
                break
            story_tell(n)
            self.artifacts = game.artifacts_count
        update_file(self.artifacts) # Сохранение счета
        pygame.time.delay(100)
        pygame.quit()
