import pygame
import sys
from settings import *
from player import Player
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.font = pygame.font.SysFont("arialblack", 20)
        self.new_game()
    
    def new_game(self):
        self.player = Player(self)
        self.level = Level(self)

    def update(self):
        self.player.update()
        self.level.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill((255, 255, 255))
        #draw level first then player
        self.level.draw()
        if self.player.hp > 0:
            self.player.draw()
        if self.player.leveled_up == True:
            for card in self.player.card_list:
                if card.draw():
                    self.player.exp = 0
                    self.player.leveled_up = False
                    self.level.populate_level()
        
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