import pygame

class HealthBar():
    def __init__(self, game, x, y, w, h, max_hp):
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp
        self.max_hp = max_hp

    def draw(self):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(self.game.screen, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(self.game.screen, "green", (self.x, self.y, self.w * ratio, self.h))

    def update(self, currHp, currX, currY):
        self.hp = currHp
        self.x = currX
        self.y = currY - 8
