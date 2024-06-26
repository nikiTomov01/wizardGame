import pygame
import math
from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self, game, x, y, image):
        self.game = game
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.npcRect = self.image.get_rect(topleft = (self.x, self.y))
        self.collideRect = pygame.Rect(self.x, self.y, 64, 64)

    def draw(self):
        self.game.screen.blit(self.image, self.npcRect)

    def check_for_player(self):
        intDistance = 128
        #if math.hypot(self.x - self.game.player.x, self.y - self.game.player.y) < float(intDistance):
        #    self.interact()
        if self.collideRect.colliderect(self.game.player.player_rect):
            self.interact()
            
    @abstractmethod
    def interact(self):
        pass

    def update(self):
        self.check_for_player()