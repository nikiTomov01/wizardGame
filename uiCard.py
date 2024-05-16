import pygame

class UICard:
    def __init__(self, game, x, y, image):
        self.game = game
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        # different way for implement image and get_rect check enemy.py for shorthand way
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False

        #get mouse position 
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw card on screen
        self.game.screen.blit(self.image, self.rect)

        if action == True:
            del self

        return action
        