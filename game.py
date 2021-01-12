class Game:
    def __init__(self, labyrinth, hero, ghost):
        self.labyrinth = labyrinth
        self.hero = hero
        self.ghost = ghost

    def render(self, screen):
        self.labyrinth.render(screen)
        self.hero.render(screen)
        self.ghost.render(screen)