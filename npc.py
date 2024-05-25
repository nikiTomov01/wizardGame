import pygame
import math
from abc import ABC, abstractmethod

class NPC(ABC):
    def __init__(self, game, x, y, image):
        self.game = game
        self.x = x
        self.y = y
        self.image = image
        self.image = pygame.transform.scale(self.image, (126, 126))
        self.npcRect = self.image.get_rect(topleft = (self.x, self.y))

    def draw(self):
        self.game.screen.blit(self.image, self.npcRect)

    def check_for_player(self):
        intDistance = 128
        if math.hypot(self.x - self.game.player.x, self.y - self.game.player.y) < float(intDistance):
            self.interact()
            
    @abstractmethod
    def interact(self):
        pass

    def update(self):
        self.check_for_player()