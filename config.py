import os
# Параметры путей до папок
game_folder = os.path.dirname(__file__)
sprites_folder = os.path.join(game_folder, "sprites")
scenes_folder = os.path.join(game_folder, "scenes")
map_folder = os.path.join(scenes_folder, "maps")

# Параметры игры
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1300, 700
FPS = 8
MAPS_DIR = 'maps'
TILE_SIZE = 40

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

