import pygame

# Game settings
RES = (1376, 768)
FPS = 60

#Player settings
SPEED = 0.25

# text stuff
TEXT_COL = (255, 255, 255)

#game functions
def draw_stats(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.game.screen.blit(img, (x, y))