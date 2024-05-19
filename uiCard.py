import pygame

class UICard:
    def __init__(self, game, x, y, image, cardFunc):
        self.game = game
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width), int(height)))
        self.cardFunc = cardFunc
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
            if self.cardFunc == "fire":
                self.game.player.base_dmg += 5
                self.game.player.elems_rank[0] += 1
                self.game.player.update_elem()
            if self.cardFunc == "earth":
                self.game.player.hp += 5
                self.game.player.elems_rank[3] += 1
                self.game.player.update_elem()
            if self.cardFunc == "air":
                self.game.player.attack_speed -= 250
                self.game.player.elems_rank[2] += 1
                self.game.player.update_elem()
            if self.cardFunc == "water":
                self.game.player.ms += 0.01
                self.game.player.elems_rank[1] += 1
                self.game.player.update_elem()

        return action
        