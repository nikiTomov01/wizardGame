import pygame, sys
from pytmx.util_pygame import load_pygame
from tile import Tile
from enemy import Enemy
from settings import *
import random


class Level:
    def __init__(self, game):
        self.game = game
        self.tmx_data = load_pygame("./map/levelTwo/levelTwo.tmx")
        self.bg_sprite_group = pygame.sprite.Group()
        self.collidable_sprite_group = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.drops_list = pygame.sprite.Group()
        self.populate_sprite_group()
        self.world_shift_x = 0
        self.world_shift_y = 0
        #self.populate_level()

    def populate_sprite_group(self):
        #cycle through all layers
        for layer in self.tmx_data.layers:
            if layer.name == "ground" or layer.name == "stones": # could be done with id but name is easier to read and track
                for x, y, surf in layer.tiles():
                    pos = (x * 32, y * 32)
                    if layer.name == "ground":
                        Tile(pos = pos, surf = surf, groups = self.bg_sprite_group)
                    else:
                        Tile(pos = pos, surf = surf, groups = self.collidable_sprite_group)
            if layer.name == "trees":
                for x, y, surf in layer.tiles():
                    pos = (x * 32, y * 32 - (77 - 32))         
                    Tile(pos = pos, surf = surf, groups = self.collidable_sprite_group)

    def spawn_enemy(self):
        rand_pos_x = random.randrange(0, 800)
        rand_pos_y = random.randrange(0, 600)
        Enemy(self.game, rand_pos_x, rand_pos_y, self.enemy_list)

    def populate_level(self):
        self.enemy_list.empty()
        for i in range(0, 5):
            self.spawn_enemy()
            
    # checks for player direction and adds world offset
    def camera_movement(self):
        if self.game.player.direction.x < 0:
            self.world_shift_x = 4
        elif self.game.player.direction.x > 0:
            self.world_shift_x = -4
        else:
            self.world_shift_x = 0

        if self.game.player.direction.y < 0:
            self.world_shift_y = 4
        elif self.game.player.direction.y > 0:
            self.world_shift_y = -4
        else:
            self.world_shift_y = 0

    def draw(self):
        self.bg_sprite_group.draw(self.game.screen)
        self.collidable_sprite_group.draw(self.game.screen)
        for enemy in self.enemy_list.sprites():
            enemy.draw()
        for drop in self.drops_list.sprites():
            drop.draw()

    # used for camera
    def update(self):
        #for sprite in self.bg_sprite_group: #loops through sprites in world tile group and offsets them based on player direction (used with camera_movement)
        #    sprite.update(self.world_shift_x, self.world_shift_y)
        for enemy in self.enemy_list.sprites():
            enemy.update()
        for drop in self.drops_list.sprites():
            drop.update()
        self.camera_movement()