import pygame
from settings import *
from attack import Attack

class Player:
    def __init__(self, game):
        self.game = game
        self.x = RES[0] / 2
        self.y = RES[1] / 2
        self.direction = pygame.math.Vector2(0, 0)
        self.player_image = pygame.image.load("./character/pixelFlameChar.png").convert_alpha()
        self.attack_group = pygame.sprite.Group() # attack sprites
        self.i_frame = pygame.time.get_ticks() #used to give player damage immunity
        self.attack_interval = pygame.time.get_ticks() #used to check time between last attack
        self.attack_speed = 500 #sets the needed amount of time to pass before attacking again

        #stats
        self.hp = 10
        self.base_dmg = 5
        self.lvl = 1
        self.exp = 0
        
    def movement(self):
        speed = SPEED * self.game.delta_time

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= speed
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.y += speed
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_d]:
            self.x += speed
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.x -= speed
            self.direction.x = -1
        else:
            self.direction.x = 0

    def attack(self):
        Attack(self.game, self.x, self.y, pygame.mouse.get_pos(), "player", self.base_dmg, self.attack_group)

    def take_damage(self, enemy_dmg):
        if pygame.time.get_ticks() - self.i_frame >= 1000:
            print("damage taken:", enemy_dmg)
            self.hp -= enemy_dmg
            print("hp left: ", self.hp)
            self.i_frame = pygame.time.get_ticks()

    def draw(self):
        #pygame.draw.rect(self.game.screen, (0, 0, 0), [self.x, self.y, 32, 32])
        player_rect = self.player_image.get_rect(center = (self.x, self.y))
        self.game.screen.blit(self.player_image, player_rect)
        self.attack_group.draw(self.game.screen)

    def draw_stats(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.game.screen.blit(img, (x, y))


    def update(self):
        self.movement()
        mousePress = pygame.mouse.get_pressed() #gets pressed mouse keys
        if mousePress[0] == True: #check if left mouse button is pressed
            if pygame.time.get_ticks() - self.attack_interval >= self.attack_speed:
                self.attack()
                self.attack_interval = pygame.time.get_ticks()
        for attack in self.attack_group.sprites():
            attack.update()
        self.draw_stats("HP: {hp}".format(hp = self.hp), self.game.font, TEXT_COL, 10, 5)
        self.draw_stats("LVL: {lvl}".format(lvl = self.lvl), self.game.font, TEXT_COL, 120, 5)
        self.draw_stats("EXP: {exp}".format(exp = self.exp), self.game.font, TEXT_COL, 230, 5)
