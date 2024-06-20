import pygame
import random
from attack import Attack
from drops import Drops
from settings import RES, TEXT_COL, GLOBAL_ELEM_DICT
from settings import draw_text
from healthBar import HealthBar

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
        self.elem_pick()
        self.image = pygame.image.load(f"./enemies/{self.elem}/{self.elem}Slime.png") #pipes in element of the enemy to get the correct sprite image
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))
        self.old_rect = self.rect
        
        self.i_frame = pygame.time.get_ticks()
        
        #stats
        self.base_dmg = 2
        self.hp = 7
        self.lvl = self.game.player.lvl
        self.healthBar = HealthBar(self.game, self.rect.x, self.rect.y, 32, 8, self.hp)
        #print(self.elem)

        #attack stuff
        self.attack_group = pygame.sprite.Group() # enemy attack sprites
        self.attack_timer = pygame.time.get_ticks()

    def draw(self):
        self.game.screen.blit(self.image, self.rect)
        self.attack_group.draw(self.game.screen)
        #draw_text(self, f"HP: {self.hp}", self.game.font, TEXT_COL, self.rect.x - 16, self.rect.y - 32)
        self.healthBar.draw()

    def random_movement(self): #very long probably bad could be done so much better movement but for now it works
        #for x
        self.space_count_x += 1
        self.rect.x += self.direction_x * self.speed

        if (self.space_count_x >= self.turn_x):
            self.direction_x *= -1
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)
        #change direction for x if hitting screen edge
        if (self.rect.x <= 0): 
            self.direction_x = 1  # turn right
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)
        elif (self.rect.x >= RES[0] - 32):
            self.direction_x = -1
            self.space_count_x = 0
            self.turn_x = random.randrange(1, 100)

        #for y
        self.space_count_y += 1
        self.rect.y += self.direction_y * self.speed

        if (self.space_count_y >= self.turn_y):
            self.direction_y *= -1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)
        if (self.rect.y <= 0):
            self.direction_y = 1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)
        elif (self.rect.y >= RES[1] -32):
            self.direction_y = -1
            self.space_count_y = 0
            self.turn_y = random.randrange(1, 100)

        #check for collision
        for obj in self.game.level.collidable_sprite_group.sprites():
            if obj.rect.colliderect(self.rect):
                #for X
                if self.rect.left <= obj.rect.right and self.old_rect.left >= obj.old_rect.left:
                    self.rect.left = obj.rect.right
                if self.rect.right >= obj.rect.left and self.old_rect.right <= obj.old_rect.right:
                    self.rect.right = obj.rect.left

                #for Y
                if self.rect.bottom >= obj.rect.top and self.old_rect.bottom <= obj.old_rect.top:
                    self.rect.bottom = obj.rect.top
                if self.rect.top <= obj.rect.bottom and self.old_rect.top >= obj.old_rect.bottom:
                    self.rect.top = obj.rect.bttom
                

    # checks if a specified interval has passed after last dmg check and reduces enemy.hp
    def take_dmg(self, dmg):
        if pygame.time.get_ticks() - self.i_frame >= 1000:
            #is there a way to not write 12 if checks for player/mob elem interaction?
            if (self.game.player.curr_element == "fire" and self.elem == "air"):
                dmg += 5
            if (self.game.player.curr_element == "water" and self.elem == "fire"):
                dmg += 5
            if (self.game.player.curr_element == "air" and self.elem == "fire"):
                dmg -= 3
            if (self.game.player.curr_element == "earth"):
                dmg += 3
            self.hp -= dmg
            self.i_frame = pygame.time.get_ticks()
            if self.hp <= 0:
                self.kill()
                self.game.player.exp += 20
                Drops(self.game, self.rect.x, self.rect.y, pygame.image.load("./character/elementalParticles/fireParticle.png"), self.game.level.drops_list)

    def attack_player(self):
        player_pos = (self.game.player.player_rect.x, self.game.player.player_rect.y)
        Attack(self.game, self.rect.x, self.rect.y, player_pos, "enemy", pygame.image.load(f"./character/{self.elem}BallPixel.png"), self.base_dmg, self.attack_group) 
        self.attack_timer = pygame.time.get_ticks()

    def elem_pick(self):
        random_elem = random.randrange(0, 5)
        if (random_elem == 0):
            self.elem = GLOBAL_ELEM_DICT[random_elem]
        elif(random_elem == 1):
            self.elem = GLOBAL_ELEM_DICT[random_elem]
        elif(random_elem == 2):
            self.elem = GLOBAL_ELEM_DICT[random_elem]
        elif(random_elem == 3):
            self.elem = GLOBAL_ELEM_DICT[random_elem]
        else:
            self.elem = "fire"

    def update(self):
        # enemy attack speed (currently shots every 1.5 second)
        self.old_rect = self.rect
        self.healthBar.update(self.hp, self.rect.x, self.rect.y)
        self.random_movement()
        if pygame.time.get_ticks() - self.attack_timer >= 1500: #attacks player when a specified time interval has passed
            self.attack_player()
        for attack in self.attack_group.sprites():
            attack.update()