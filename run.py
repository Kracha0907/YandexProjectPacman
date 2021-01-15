import pygame
from menu import *
# Запуск игры


def main():
    pygame.init()
    pygame.font.init()
    Button_game()  # Переходим в главное меню
    sys.exit(0)


if __name__ == '__main__':
    main()
