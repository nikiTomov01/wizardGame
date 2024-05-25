import pygame
from npc import NPC
from settings import draw_text

class SpawnerNPC(NPC):
    def __init__(self, game, x, y, image):
        super().__init__(game, x, y, image)

    def interact(self):
        keys = pygame.key.get_pressed()
        draw_text(self, "Press 'E' to spawn a wave of monsters", self.game.font, (255,255,255), self.x - 256, self.y - 32)
        if keys[pygame.K_e] and not self.game.level.enemy_list:
            self.game.level.populate_level()