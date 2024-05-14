import pygame
import math

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups):
        super().__init__(groups)
        self.game = game
        self.pos = (x - 32, y - 32)
        self.image = pygame.image.load("./character/fireBallPixel.png").convert_alpha()
        self.speed = 5
        self.rect = self.image.get_rect(topleft = self.pos)

        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[0], -self.dir[1]))
        self.image = pygame.transform.rotate(self.image, angle)

    # if camera simulation is removed fireballs look normal and not stuck to screen
    #def draw(self):
    #    self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)
        # self.rect.x = self.pos[0] + self.dir[0] * self.speed
        # self.rect.y = self.pos[1] + self.dir[1] * self.speed
        self.rect.x, self.rect.y = self.pos