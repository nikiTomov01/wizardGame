import pygame
import math

class Enemy:
    def __init__(self, game, x, y):
        self.game = game
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pygame.image.load("./character/fireBallPixel.png")
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.tempEnemy = pygame.Surface((32, 32)).convert_alpha()
        self.tempEnemy.fill((0,0,0))
        self.tempRect = self.tempEnemy.get_rect(topleft = (self.x, self.y))

    def draw(self):
        self.game.screen.blit(self.tempEnemy, self.tempRect)