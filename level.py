import pygame, sys
from pytmx.util_pygame import load_pygame
from tile import Tile
from enemy import Enemy
from settings import *
import random


class Level:
    def __init__(self, game):
        self.game = game
        self.tmx_data = load_pygame("./map/map.tmx")
        self.sprite_group = pygame.sprite.Group()
        self.enemy_list = []
        self.populate_sprite_group()
        self.world_shift_x = 0
        self.world_shift_y = 0
        for i in range(0, 5):
            self.spawn_enemy()

    def populate_sprite_group(self):
        #cycle through all layers
        for layer in self.tmx_data.layers:
            if layer.name == "ground" or layer.name == "stones": # could be done with id but name is easier to read and track
                for x, y, surf in layer.tiles():
                    pos = (x * 32, y * 32)
                    Tile(pos = pos, surf = surf, groups = self.sprite_group)
            if layer.name == "trees":
                for x, y, surf in layer.tiles():
                    pos = (x * 32, y * 32 - (77 - 32))         
                    Tile(pos = pos, surf = surf, groups = self.sprite_group)

    def spawn_enemy(self):
        rand_pos_x = random.randrange(0, 800)
        rand_pos_y = random.randrange(0, 600)
        self.enemy_list.append(Enemy(self.game, rand_pos_x, rand_pos_y))
            
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
        self.sprite_group.draw(self.game.screen)
        for enemy in self.enemy_list:
            enemy.draw()

    # used for camera
    def update(self):
        for sprite in self.sprite_group: #loops through sprites in world tile group and offsets them based on player direction
            sprite.update(self.world_shift_x, self.world_shift_y)
        #self.camera_movement()