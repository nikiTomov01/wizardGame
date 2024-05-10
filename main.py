import pygame
import sys
from settings import *
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.tmx_data = load_pygame("./map/map.tmx") # map thingy ?

    def new_game(self):
        pass

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill((255, 255, 255))
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()