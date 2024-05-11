import pygame, sys
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self, game):
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, (0, 0, 255), [0, 0, 1000, 1000])