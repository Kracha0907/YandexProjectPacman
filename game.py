class Game:
    def __init__(self, labyrinth, hero, ghosts):
        self.labyrinth = labyrinth
        self.hero = hero
        self.ghosts = ghosts

    def render(self, screen):
        # Отрисовка всех спрайтов игры
        self.labyrinth.render(screen)
        self.hero.render(screen)
        for i in self.ghosts:
            i.render(screen)
