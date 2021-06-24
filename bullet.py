import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, al_settings, screen, plane):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bullet2.png')
        #self.image = pygame.Surface((900, 500))
        #self.image.fill((0, 250, 0))
        self.image.set_colorkey((32, 0, 74))  # вырезать цвет фона
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        self.b_y = float(self.rect.y)
        self.speed_factor = al_settings.bullet_speed


    def update(self):
        self.b_y -= self.speed_factor
        self.rect.y = self.b_y



