import pygame
import random
from settings import *
from attack import Attack
from uiCard import UICard
from healthBar import HealthBar

class Player:
    def __init__(self, game):
        self.game = game
        self.x = RES[0] / 2
        self.y = RES[1] / 2
        self.direction = pygame.math.Vector2(0, 0)
        self.player_image = pygame.image.load("./character/pixelFlameChar.png").convert_alpha()
        self.player_rect = self.player_image.get_rect(center = (self.x, self.y))
        self.old_rect = self.player_rect.copy()
        self.attack_group = pygame.sprite.Group() # attack sprites
        self.i_frame = pygame.time.get_ticks() #used to give player damage immunity
        self.attack_interval = pygame.time.get_ticks() #used to check time between last attack
        self.attack_speed = 500 #sets the needed amount of time to pass before attacking again
        self.level_up_card_dict = {0 : pygame.image.load("./ui/fireUpCard.png"), 
                                   1 : pygame.image.load("./ui/waterUpCard.png"),
                                   2 : pygame.image.load("./ui/airUpCard.png"),
                                   3 : pygame.image.load("./ui/earthUpCard.png")}
        self.elems_rank = {0 : 0, 1 : 0, 2 : 0, 3 : 0}
        #self.attack_image_dict = {"fire": pygame.image.load("./character/fireBallPixel.png"),
        #                          "water": pygame.image.load("./character/waterBallTemp.png"),
        #                          "air": pygame.image.load("./character/fireBallPixel.png"),
        #                          "earth": pygame.image.load("./character/rockBallPixel.png")}

        #stats
        self.hp = 10
        self.ms = SPEED
        #self.element = "fire"
        self.base_dmg = 5
        self.elem_particles = 0
        self.healthBar = HealthBar(self.game, self.player_rect.x, self.player_rect.y, 32, 8, self.hp)

        #lvl stuff
        self.lvl = 1
        self.exp = 0
        self.leveled_up = False
        self.curr_element = GLOBAL_ELEM_DICT[0]
        self.curr_max_elem = self.elems_rank[0]
        self.nextElem = 0

        #level up stuff
        self.card_list = []
        self.temp_card_image = pygame.image.load("./ui/dmg-up-card.png")
        
    def movement(self):
        speed = self.ms * self.game.delta_time
        #self.player_rect = self.player_image.get_rect(center = (self.x, self.y))

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

        self.player_rect.x += self.direction.x * speed
        self.player_rect.y += self.direction.y * speed

        for object in self.game.level.collidable_sprite_group.sprites():
            if object.rect.colliderect(self.player_rect):
                #left
                if self.player_rect.left <= object.rect.right and self.old_rect.left >= object.old_rect.right:
                    self.player_rect.left = object.rect.right

                #right
                if self.player_rect.right >= object.rect.left and self.old_rect.right <= object.old_rect.left:
                    self.player_rect.right = object.rect.left

                #bottom
                if self.player_rect.bottom >= object.rect.top and self.old_rect.bottom <= object.old_rect.top:
                    self.player_rect.bottom = object.rect.top

                #top
                if self.player_rect.top <= object.rect.bottom and self.old_rect.top >= object.old_rect.bottom:
                    self.player_rect.top = object.rect.bottom

        # restricts movement outside of screen for X
        if self.player_rect.x <= 0:
            self.player_rect.x = 0
        elif self.player_rect.x >= RES[0] - 26:
            self.player_rect.x = RES[0] - 26

        # restricts movement outside of screen for Y
        if self.player_rect.y <= 0:
            self.player_rect.y = 0
        elif self.player_rect.y >= RES[1] - 32:
            self.player_rect.y = RES[1] - 32

    def attack(self):
        Attack(self.game, self.player_rect.x + 16, self.player_rect.y + 16, pygame.mouse.get_pos(), "player", pygame.image.load(f"./character/{self.curr_element}BallPixel.png") ,self.base_dmg, self.attack_group)

    def take_damage(self, enemy_dmg):
        if pygame.time.get_ticks() - self.i_frame >= 1000:
            #print("damage taken:", enemy_dmg)
            self.hp -= enemy_dmg
            #print("hp left: ", self.hp)
            self.i_frame = pygame.time.get_ticks()

    def draw(self):
        #pygame.draw.rect(self.game.screen, (0, 0, 0), [self.x, self.y, 32, 32])
        
        self.game.screen.blit(self.player_image, self.player_rect)
        self.attack_group.draw(self.game.screen)
        draw_text(self, f"HP: {self.hp}", self.game.font, TEXT_COL, 10, 5)
        draw_text(self, f"LVL: {self.lvl}", self.game.font, TEXT_COL, 120, 5)
        draw_text(self, f"EXP: {self.exp}", self.game.font, TEXT_COL, 230, 5)
        draw_text(self, f"Elem particles: {self.elem_particles}", self.game.font, TEXT_COL, 10, 35)
        draw_text(self, f"Current elem: {self.curr_element}", self.game.font, TEXT_COL, 350, 5)
        self.healthBar.draw()

    def level_up(self):
        if self.leveled_up == False:
            self.lvl += 1
            self.card_list.clear()
            selected_rand_elem_one = random.randrange(0, 4)
            selected_rand_elem_two = random.randrange(0, 4)
            self.card_list.append(UICard(self.game, 150, 100, self.level_up_card_dict[selected_rand_elem_one], GLOBAL_ELEM_DICT[selected_rand_elem_one]))
            self.card_list.append(UICard(self.game, 850, 100, self.level_up_card_dict[selected_rand_elem_two], GLOBAL_ELEM_DICT[selected_rand_elem_two]))

    #loops through the list containing amount of points in each element and sets the current element to the element with the most points
    def update_elem(self):
        for i in range (4):
            if (self.elems_rank[i] > self.curr_max_elem):
                self.nextElem = i
                self.curr_max_elem = self.elems_rank[i]
            print("value to check is: ", self.elems_rank[i], " and current max is: ", self.curr_max_elem, " : nextElem = ", GLOBAL_ELEM_DICT[self.nextElem])
        self.curr_element = GLOBAL_ELEM_DICT[self.nextElem]
        print(self.elems_rank)
        print("curr_element: ", self.curr_element)
                    

    def update(self):
        self.old_rect = self.player_rect.copy()
        self.movement()
        self.healthBar.update(self.hp, self.player_rect.x, self.player_rect.y)
        mousePress = pygame.mouse.get_pressed() #gets pressed mouse keys
        if mousePress[0] == True: #check if left mouse button is pressed
            if pygame.time.get_ticks() - self.attack_interval >= self.attack_speed:
                self.attack()
                self.attack_interval = pygame.time.get_ticks()
        for attack in self.attack_group.sprites(): # call update for each attack thrown by player
            attack.update()
        if self.exp == 100: #maybe make this a better check for level up
            self.level_up()
            self.leveled_up = True
        #print(self.elems_rank)
