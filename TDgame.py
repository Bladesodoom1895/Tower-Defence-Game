import pygame

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

class Game:
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.win = pygame.display.set_mode((
            self.width, self.height))
        caption = pygame.display.set_caption('Tower Defence')
        self.enemies = []
        self.towers = []
        self.lives = 20
        self.money = 200

    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()
