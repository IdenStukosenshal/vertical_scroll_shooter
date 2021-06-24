import pygame.font
from pygame.sprite import Group
from plane import Plane

class Scoreboard():
    def __init__(self, al_settings, stats, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.al_settings = al_settings
        self.stats = stats
        self.textcolor = (150, 250, 250)
        self.font = pygame.font.SysFont(None, 40)  #шрифт по умолчанию
        self.prep_score()
        self.prep_plane()

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_img  = self.font.render(score_str, True, self.textcolor, self.al_settings.bg_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.planes.draw(self.screen)

    def prep_plane(self):
        self.planes = Group()
        for plane_num in range(self.stats.plane_limit):
            plane = Plane(self.al_settings, self.screen)
            plane.rect.x = 10 + plane_num * plane.rect.width
            plane.rect.y = 10
            self.planes.add(plane)

