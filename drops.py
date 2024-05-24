import pygame

class Drops(pygame.sprite.Sprite): #the list for drops is in level.py
    def __init__(self, game, x, y, image, groups):
        super().__init__(groups)
        self.game = game
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def check_if_picked_up(self):
        if self.rect.colliderect(self.game.player.player_rect): #checks if the player is colliding with the drop and does something
            print("picked up!!!")

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.check_if_picked_up()