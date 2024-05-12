import pygame
from settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x = 800 / 2
        self.y = 600 / 2
        self.direction = pygame.math.Vector2(0, 0)
        self.player_image = pygame.image.load("./character/pixelFlameChar.png").convert_alpha()
        
    def movement(self):
        #speed = SPEED * self.game.delta_time

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            #self.y -= speed
            self.direction.y = -1
        elif keys[pygame.K_s]:
            #self.y += speed
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_d]:
            #self.x += speed
            self.direction.x = 1
        elif keys[pygame.K_a]:
            #self.x -= speed
            self.direction.x = -1
        else:
            self.direction.x = 0

    def draw(self):
        #pygame.draw.rect(self.game.screen, (0, 0, 0), [self.x, self.y, 32, 32])
        player_rect = self.player_image.get_rect(center = (self.x, self.y))
        self.game.screen.blit(self.player_image, player_rect)


    def update(self):
        self.movement()
