# from scenes.game_lvl1 import GameLevel as g1
from main import GameLevel as g1
from zastavka import *


def update_file(score):
    f = open('scores_info.txt', 'a')
    f.write(str(score))
    f.write('\n')
    f.close()


class Scene_manager():
    def __init__(self):
        self.all_scenes = [g1]
        self.e = ''
        self.a = 0

    def scenes_loop(self):
        pygame.init()
        pygame.font.init()
        n = 1
        story_tell(n)
        for i in self.all_scenes:
            n += 1
            game = i()
            game.main()
            if game.pacman.health <= 0:
                break
            story_tell(n)
        update_file(self.a) # Сохранение счета
        pygame.time.delay(100)
        pygame.quit()
