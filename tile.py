import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)

    # updates x and y position of tiles with a offset parameter
    def update(self, x_shift, y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift