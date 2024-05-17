import pygame
import random
from attack import Attack
from settings import RES

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups):
        super().__init__(groups)
        self.game = game
        self.x = x
        self.y = y
        self.speed = 1
        self.direction_x = -1
        self.direction_y = -1
        self.turn_x = random.randrange(1, 100)
        self.turn_y = random.randrange(1, 100)
        self.space_count_x = 0
        self.space_count_y = 0
        self.image = pygame.image.load("./character/fireBallPixel.png")
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        #temp enemy
        self.tempEnemy = pygame.Surface((32, 32)).convert_alpha()
        self.tempEnemy.fill((0,0,0))
        self.tempRect = self.tempEnemy.get_rect(topleft = (self.x, self.y))
        self.i_frame = pygame.time.get_ticks()

        #stats
        self.base_dmg = 2
        self.hp = 7
        self.lvl = self.game.player.lvl

        #attack stuff
        self.attack_group = pygame.sprite.Group() # enemy attack sprites
        self.attack_timer = pygame.time.get_ticks()

    def draw(self):
        self.game.screen.blit(self.tempEnemy, self.tempRect)
        self.attack_group.draw(self.game.screen)

    def random_movement(self): #very long probably bad could be done so much better movement but for now it works
        #for x
        self.space_count_x += 1
        self.tempRect.x += self.direction_x * self.speed

        if (self.space_count_x >= self.turn_x):
            self.direction_x *= -1
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)
        #change direction for x if hitting screen edge
        if (self.tempRect.x <= 0): 
            self.direction_x = 1  # turn right
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)
        elif (self.tempRect.x >= RES[0]):
            self.direction_x = -1
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)

        #for y
        self.space_count_y += 1
        self.tempRect.y += self.direction_y * self.speed

        if (self.space_count_y >= self.turn_y):
            self.direction_y *= -1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)
        if (self.tempRect.y <= 0):
            self.direction_y = 1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)
        elif (self.tempRect.y >= RES[1]):
            self.direction_y = -1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)


    def take_dmg(self, dmg):
        if pygame.time.get_ticks() - self.i_frame >= 1000:
            self.hp -= dmg
            self.i_frame = pygame.time.get_ticks()
            if self.hp <= 0:
                self.kill()
                self.game.player.exp += 20
            print(self.hp)

    def attack_player(self):
        player_pos = (self.game.player.x, self.game.player.y)
        Attack(self.game, self.tempRect.x, self.tempRect.y, player_pos, "enemy", self.base_dmg, self.attack_group) 
        self.attack_timer = pygame.time.get_ticks()

    def update(self):
        # enemy attack speed (currently shots every 1.5 second)
        self.random_movement()
        if self.attack_timer is not None:
            if pygame.time.get_ticks() - self.attack_timer >= 1500:
                self.attack_player()
        for attack in self.attack_group.sprites():
            attack.update()