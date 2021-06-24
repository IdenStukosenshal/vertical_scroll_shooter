import pygame
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self, al_settings, screen):
        super().__init__()
        self.screen = screen
        self.al_settings = al_settings
        self.image = pygame.image.load('images/aircraft_3.png')
        self.image = pygame.transform.scale(self.image, (162, 110)) #растянуть картинку в 4 раза по S
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        #self.rect.x
        self.rect.y = (self.rect.height)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.center = self.rect.center

        self.speed_factor_w = al_settings.enemy_w_speed
        self.speed_factor_h = al_settings.enemy_h_speed
        self.vector = 1

    def update(self):
        screen_rect = self.screen.get_rect()
        if  self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            self.vector *= -1
        self.x += self.speed_factor_w * self.vector
        self.rect.x = self.x
        self.y += self.speed_factor_h
        self.rect.y = self.y

