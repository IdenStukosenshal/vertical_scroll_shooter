import pygame
from pygame.sprite import Sprite
#import random
class Enemy2(Sprite):
    def __init__(self, al_settings, screen):
        super().__init__()
        self.screen = screen
        self.al_settings = al_settings
        self.image = pygame.image.load('images/aircraft_1e.png')
        self.image = pygame.transform.scale(self.image, (114, 84)) #растянуть картинку в 4 раза по S
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        #self.rect.x
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.speed_factor_h = al_settings.enemy2_h_speed
        self.center = self.rect.center

    def update(self):

        self.y += self.speed_factor_h
        self.rect.y = self.y

