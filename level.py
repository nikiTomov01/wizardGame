import pygame, sys
from pytmx.util_pygame import load_pygame
from tile import Tile


class Level:
    def __init__(self, game):
        self.game = game
        self.tmx_data = load_pygame("./map/map.tmx")
        self.sprite_group = pygame.sprite.Group()
        self.populate_sprite_group()

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


    def draw(self):
        self.sprite_group.draw(self.game.screen)
        