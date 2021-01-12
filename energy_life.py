import pygame

class EnergyLife:
    def __init__(self, screen, p):
        self.energy = p.energy
        self.life = p.health
        self.screen = screen

    def render(self, p):
        self.energy = p.energy
        self.life = p.health
        x = 1100
        y = 10
        color = pygame.Color('black')
        color.hsva = (190, 100, 100, 100)
        pygame.draw.rect(self.screen, color, ((x, y), (1.5 * self.energy, 20)))
        color.hsva = (190, 100, 75, 100)
        pygame.draw.rect(self.screen, color, ((x - 1, y - 1), (1.5 * 100 + 2, 21)), 5)
        y = 50
        color.hsva = (0, 100, 100, 100)
        pygame.draw.rect(self.screen, color, ((x, y), (1.5 * self.life, 20)))
        color.hsva = (0, 100, 75, 100)
        pygame.draw.rect(self.screen, color, ((x - 1, y - 1), (1.5 * 100 + 2, 21)), 5)
