import pygame

class Drops(pygame.sprite.Sprite): #the list for drops is in level.py
    def __init__(self, game, x, y, image, groups):
        super().__init__(groups)
        self.game = game
        self.x = x
        self.y = y
        self.float_dir = -1
        self.float_speed = 1
        self.image = image
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(topleft = (self.x, self.y))

    def check_if_picked_up(self):
        if self.rect.colliderect(self.game.player.player_rect): #checks if the player is colliding with the drop and does something
            self.game.player.elem_particles += 1
            self.game.player.hp += 2
            pygame.sprite.Sprite.kill(self)

    def float_anim(self):
        max_up = self.y - 32
        self.rect.y += self.float_dir * self.float_speed
        if (self.rect.y == max_up):
            self.float_dir = 1
        elif (self.rect.y == self.y):
            self.float_dir = -1

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def update(self):
        self.check_if_picked_up()
        self.float_anim()