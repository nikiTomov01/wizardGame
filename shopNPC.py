import pygame
from npc import NPC

class ShopNPC(NPC):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, image)
        self.item_list = []
    
    def interact(self):
        self.draw_ui()

    def draw_ui(self):
        pygame.draw.rect(self.game.screen, ((0, 0, 0)), (10, 10, 650, 750))
        pygame.draw.rect(self.game.screen, "white", (25, 20, 300, 350))
        pygame.draw.rect(self.game.screen, "white", (345, 20, 300, 350))
        pygame.draw.rect(self.game.screen, "white", (25, 390, 300, 350))
        pygame.draw.rect(self.game.screen, "white", (345, 390, 300, 350))