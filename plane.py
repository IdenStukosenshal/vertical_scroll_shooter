import pygame
from pygame.sprite import Sprite
class Plane(Sprite):
    def __init__(self, al_settings, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/aircraft_1.png')
        self.image = pygame.transform.scale(self.image, (114, 84)) #растянуть картинку в 4 раза по S
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.al_settings = al_settings
        # Каждый новый plane появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.mov_right = False
        self.mov_left = False
        self.mov_up = False
        self.mov_down = False
        self.space_down = False

        self.hitpoints = al_settings.hitpoints

    def update(self):
        if self.mov_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.al_settings.plane_speed_f
        if self.mov_left and self.rect.left > 0:
            self.center_x -= self.al_settings.plane_speed_f
        if self.mov_up and self.rect.top > 0:
            self.center_y -= self.al_settings.plane_speed_f
        if self.mov_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.al_settings.plane_speed_f
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


    def blitme(self):
        """Рисует plane в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_plane(self):
        self.center_x = self.screen_rect.centerx
        self.center_y = self.screen_rect.bottom - 84/2-1

