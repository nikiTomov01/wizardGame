import pygame
import math
from attack import Attack

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups):
        super().__init__(groups)
        self.game = game
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pygame.image.load("./character/fireBallPixel.png")
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        #temp enemy
        self.tempEnemy = pygame.Surface((32, 32)).convert_alpha()
        self.tempEnemy.fill((0,0,0))
        self.tempRect = self.tempEnemy.get_rect(topleft = (self.x, self.y))

        #attack stuff
        self.attack_group = pygame.sprite.Group()
        self.attack_timer = pygame.time.get_ticks()

    def draw(self):
        self.game.screen.blit(self.tempEnemy, self.tempRect)
        self.attack_group.draw(self.game.screen)

    def attack_player(self):
        player_pos = (self.game.player.x, self.game.player.y)
        Attack(self.game, self.x, self.y, player_pos, "enemy", self.attack_group) 
        self.attack_timer = pygame.time.get_ticks()        

    def update(self):
        # enemy attack speed (currently shots every 1.5 second)
        if self.attack_timer is not None:
            if pygame.time.get_ticks() - self.attack_timer >= 1500:
                self.attack_player()
        for attack in self.attack_group.sprites():
            attack.update()