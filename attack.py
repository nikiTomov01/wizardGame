import pygame
import math

class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y, groups):
        super().__init__(groups)
        self.game = game
        self.pos = (x - 32, y - 32)
        self.image = pygame.image.load("./character/fireBallPixel.png").convert_alpha()
        self.speed = 5
        self.rect = self.image.get_rect(topleft = self.pos)

        mx, my = pygame.mouse.get_pos()
        self.dir = (mx - x, my - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[0], -self.dir[1]))
        self.image = pygame.transform.rotate(self.image, angle)

        #set timer to kill sprite after some time to clear it
        self.time = pygame.time.get_ticks()

    # if camera simulation is removed fireballs look normal and not stuck to screen
    #def draw(self):
    #    self.game.screen.blit(self.image, self.rect)

    def check_enemy_hit(self):
        for enemy in self.game.level.enemy_list:
            #print(enemy.rect.x, enemy.rect.y)
            if self.rect.colliderect(enemy.rect):
                self.kill()
                enemy.kill()

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.speed, self.pos[1] + self.dir[1] * self.speed)
        # self.rect.x = self.pos[0] + self.dir[0] * self.speed
        # self.rect.y = self.pos[1] + self.dir[1] * self.speed
        self.rect.x, self.rect.y = self.pos

        #check for enemy hits
        self.check_enemy_hit()

        # kill attack sprite after 5 seconds(5000ms)
        if self.time is not None:
            if pygame.time.get_ticks() - self.time >= 5000:
                self.kill()