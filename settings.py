import pygame

# Game settings
RES = (1376, 768)
FPS = 60

#Player settings
SPEED = 0.25

# text stuff
TEXT_COL = (255, 255, 255)

#game wide stuff
GLOBAL_ELEM_DICT = {0 : "fire", 1 : "water", 2 : "air", 3 : "earth"}

#game functions

#draws text in every class except main.
def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.game.screen.blit(img, (x, y))

#draws text in the game class.
def draw_text_main(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))