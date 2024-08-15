import pygame
from settings import *
from level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Blind Caver')

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.level = Level()

    def run(self):
        running = True

        while running:
            self.clock.tick()
            dt = self.clock.get_fps() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.level.run(dt)

            pygame.display.update()

        pygame.quit()

Game().run()
