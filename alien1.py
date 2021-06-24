# coding:utf-8
import pygame
import game_functions as g_f
from settings import Settings
from plane import Plane
from pygame.sprite import Group
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard
import random

def run_game():
    '''Инициализирует игру, создает объект экрана'''
    pygame.init()
    pygame.mixer.init()  # для звука
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_w, al_settings.screen_h))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(al_settings, screen, 'Play')
    clock = pygame.time.Clock()

    stats = Game_stats(al_settings)
    scb = Scoreboard(al_settings, stats, screen)
    plane = Plane(al_settings, screen)
    bullets = Group()
    enemys = Group()
    explosions = Group()

    g_f.create_flt(al_settings, screen, enemys) #список врагов

    timer_interval = 200  # m seconds  промежуток между пулями. Идентификаторы событий должны находиться в диапазоне от
    timer_event = pygame.USEREVENT + 1 # pygame.USEREVENT (24) до pygame.NUMEVENTS (32). В этом случае pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, timer_interval) # - это идентификатор события таймера

    anim_strelba = 0

    star_list = []
    for i in range(50):
        x = random.randrange(0, al_settings.screen_w)
        y = random.randrange(0, al_settings.screen_h)
        star_list.append([x, y])

    '''Запуск основного цикла игры'''
    while True:
        clock.tick(60)

        anim_strelba += 1
        if anim_strelba == 6:
            anim_strelba = 0

        g_f.check_events(al_settings, screen, plane, bullets, timer_event, stats, play_button, enemys, scb)
        if stats.game_active:
            plane.update()
            g_f.update_bullets(bullets, enemys, al_settings, screen, explosions, plane, stats, scb)
            g_f.update_enemys(enemys)

        g_f.update_screen(al_settings, screen, plane, bullets, enemys, explosions, anim_strelba, stats, play_button, star_list, scb)

run_game()
