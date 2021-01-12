import pygame
from config import *


pygame.font.init()


class ArtifactsRender:
    def __init__(self, screen, value):
        self.artifacts = value
        self.screen = screen

    def render(self, value=0):
        font = pygame.font.SysFont("Arial", 35, True)
        self.artifacts = value
        x = 20
        y = 10
        width = WINDOW_WIDTH
        color = pygame.Color('red')
        hsv = color.hsva
        color.hsva = (160, 100, 75, 100)
        score_text = font.render(f"{self.artifacts}", 0, color)
        self.screen.blit(score_text, (width - 100 * len(str(self.artifacts)), 100))
        self.image = pygame.image.load(os.path.join(sprites_folder, "artifact.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.screen.blit(self.image, (width - 70 * len(str(self.artifacts)), 85))
 