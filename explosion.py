import pygame
from pygame.sprite import Sprite
class Explosion(Sprite):
    def __init__(self, screen, center):
        super().__init__()
        self.screen = screen
        self.explos1 = pygame.image.load('expl/expl1.png')  # 1048 224   6 obj
        self.explos1 = pygame.transform.scale(self.explos1, (524, 112))
        self.explos1.set_colorkey((0, 128, 0))
        self.center = center
        self.explos2 = pygame.image.load('expl/expl2.png')  # 1048 203   6 obj
        self.explos2 = pygame.transform.scale(self.explos2, (524, 101))
        self.explos2.set_colorkey((0, 128, 0))
        self.explos3 = pygame.image.load('expl/expl3.png')  # 680 171  4 obj
        self.explos3 = pygame.transform.scale(self.explos3, (340, 85))
        self.explos3.set_colorkey((0, 128, 0))
        self.count = -1 # чтобы не пропустить первый кадр анимации
        self.flag = False
        self.expl_massiv = []
        for i in range(0, 522, 87):
            surf = pygame.Surface((87, 112))
            surf.fill((0, 255, 0))     # создаётся поверхность с любым цветом,
            surf.blit(self.explos1, (0, 0), (i, 0, 87, 112))  #  на неё выводится image,
            surf.set_colorkey((0, 255, 0))     # убирается цвет поверхности
            self.expl_massiv.append(surf)
        for i in range(0, 522, 87):
            surf = pygame.Surface((87, 101))
            surf.fill((0, 255, 0))
            surf.blit(self.explos2, (0, 0), (i, 0, 87, 101))
            surf.set_colorkey((0, 255, 0))
            self.expl_massiv.append(surf)
        for i in range(0, 340, 85):
            surf = pygame.Surface((85, 85))
            surf.fill((0, 255, 0))
            surf.blit(self.explos3, (0, 0), (i, 0, 85, 85))
            surf.set_colorkey((0, 255, 0))
            self.expl_massiv.append(surf)

    def update(self):
        if self.count == 15:
            self.flag = False
        if self.flag:
            self.screen.blit(self.expl_massiv[self.count], (self.center))


