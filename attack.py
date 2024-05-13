import pygame
import math

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.image = pygame.image.load("./character/fireBallPixel.png").convert_alpha()
        self.speed = 5

        self.pos = (x, y)
        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[0], -self.dir[1]))
        self.image = pygame.transform.rotate(self.image, angle)

    def draw(self):
        attack_rect = self.image.get_rect(center = self.pos)
        self.game.screen.blit(self.image, attack_rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)