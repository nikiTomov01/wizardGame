import pygame
from npc import NPC

class shopNPC(NPC):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, image)
    
    def interact(self):
        print("shop is ready to open")