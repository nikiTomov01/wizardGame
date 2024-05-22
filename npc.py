import pygame

class NPC():
    def __init__(self, game, x, y, image):
        self.game = game
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (126, 126))
        self.npcRect = self.image.get_rect(topleft = (self.x, self.y))


    def draw(self):
        self.game.screen.blit(self.image, self.npcRect)