# coding:utf-8
import sys
import pygame
import random
from pygame.sprite import Group

pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

timer_interval2 = 100 # m seconds
timer_event2 = pygame.USEREVENT + 2
pygame.time.set_timer(timer_event2, timer_interval2)

expl_massiv = []

explos1 = pygame.image.load('expl/expl1.png')  #1048 224   6 obj
explos1 = pygame.transform.scale(explos1, (524, 112))
explos1.set_colorkey((0, 128, 0))
explos2 = pygame.image.load('expl/expl2.png')    #1048 203   6 obj
explos2 = pygame.transform.scale(explos2, (524, 101))
explos2.set_colorkey((0, 128, 0))
explos3 = pygame.image.load('expl/expl3.png')  # 680 171  4 obj
explos3 = pygame.transform.scale(explos3, (340, 85))
explos3.set_colorkey((0, 128, 0))

color = (100, 250, 250)

for i in range(0, 522, 87):
    surf = pygame.Surface((87, 112))
    surf.fill(color)
    surf.blit(explos1, (0, 0), (i, 0, 87, 112))
    expl_massiv.append(surf)
for i in range(0, 522, 87):
    surf = pygame.Surface((87, 101))
    surf.fill(color)
    surf.blit(explos2, (0, 0), (i, 0, 87, 101))
    expl_massiv.append(surf)
for i in range(0, 340, 85):
    surf = pygame.Surface((85, 85))
    surf.fill(color)
    surf.blit(explos3, (0, 0), (i, 0, 85, 85))
    expl_massiv.append(surf)


x = 500
y = 200

count = 0
def update_explos(count, flag):
    if event.type == timer_event2 and flag:
        count += 1
        if count == 16:
            flag = False



flag = False
while True:
    clock.tick(50)
    screen.fill(color)
    if flag:
        screen.blit(expl_massiv[count], (100, 100))

    for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    flag = True
                    count = 0

            if event.type == timer_event2 and flag:
                count +=1
                if count == 16:
                    flag = False







    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()



