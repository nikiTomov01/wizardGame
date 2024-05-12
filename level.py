import pygame, sys
from pytmx.util_pygame import load_pygame
from tile import Tile
from settings import *


class Level:
    def __init__(self, game):
        self.game = game
        self.tmx_data = load_pygame("./map/map.tmx")
        self.sprite_group = pygame.sprite.Group()
        self.populate_sprite_group()
        self.world_shift_x = 0
        self.world_shift_y = 0

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

        print(self.game.player.direction)


    def draw(self):
        self.sprite_group.draw(self.game.screen)

    # used for camera
    def update(self):
        for sprite in self.sprite_group:
            sprite.update(self.world_shift_x, self.world_shift_y)
        self.camera_movement()