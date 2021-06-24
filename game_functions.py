# coding:utf-8
import sys
import pygame
import random
from bullet import Bullet
from enemy import Enemy
from enemy2 import Enemy2
from explosion import Explosion

def create_flt(al_settings, screen, enemys):
    enemy = Enemy(al_settings, screen)
    enemy_w = enemy.rect.width
    available_space_x = al_settings.screen_w - enemy_w
    number_enemy_x = int(available_space_x / (2 * enemy_w))
    for enemy_num in range(number_enemy_x):
        enemy = Enemy(al_settings, screen)
        enemy.x = enemy_w + 2.5 * enemy_w * enemy_num
        enemy.rect.x = enemy.x
        enemys.add(enemy)

def create_flt2(al_settings, screen, enemys):
    enemy2 = Enemy2(al_settings, screen)
    x =  random.randrange(enemy2.rect.width, al_settings.screen_w - enemy2.rect.width)
    for enemy_num in range(3):
        enemy2 = Enemy2(al_settings, screen)
        enemy2.rect.x = x
        enemy2.y = enemy2.rect.height - 2 * enemy2.rect.height * enemy_num
        enemy2.rect.y = enemy2.y
        enemys.add(enemy2)

def stars(star_list, screen, al_settings):
    for i in range(len(star_list)):
        pygame.draw.circle(screen, (250, 250, 250), star_list[i], 2)
        star_list[i][1] += al_settings.star_speed # увеличиваем вторую координату
        if i % 2 == 0:
            star_list[i][1] -= al_settings.star_speed // 3
        if star_list[i][1] > al_settings.screen_h:
            y = random.randrange(-50, 0)
            star_list[i][1] = y
            x = random.randrange(0, al_settings.screen_w)
            star_list[i][0] = x

def fire_bullet(al_settings, screen, plane, bullets):
    """Выпускает пулю, если максимум еще не достигнут."""
    if len(bullets) <= al_settings.bullet_allowed:
        new_bullet = Bullet(al_settings, screen, plane) # создание нов пули и включение в группу
        bullets.add(new_bullet)

def check_play_button(stats, play_button, mouse_x, mouse_y, al_settings, screen, plane, enemys, bullets, scb):
    bt_cl = play_button.rect.collidepoint(mouse_x, mouse_y)
    if bt_cl and not stats.game_active:
        stats.reset_stats()
        al_settings.initial_dynamic_settings()
        stats.game_active = True
        enemys.empty()
        bullets.empty()
        create_flt(al_settings, screen, enemys)
        create_flt2(al_settings, screen, enemys)
        plane.center_plane()

        scb.prep_score() # для того, чтобы старое значение не висело на экране
        scb.prep_plane()



def check_events(al_settings, screen, plane, bullets, timer_event, stats, play_button, enemys, scb):
    for event in pygame.event.get():
        if event.type == timer_event and plane.space_down == True:
            fire_bullet(al_settings, screen, plane, bullets)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, al_settings, screen, plane, enemys, bullets, scb)
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, plane, al_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, plane)

def check_key_down_events(event, plane, al_settings, screen, bullets):
    if event.key == pygame.K_RIGHT:
        plane.mov_right = True
    if event.key == pygame.K_LEFT:
        plane.mov_left = True
    if event.key == pygame.K_UP:
        plane.mov_up = True
    if event.key == pygame.K_DOWN:
        plane.mov_down = True
    if event.key == pygame.K_SPACE:
        plane.space_down = True
        fire_bullet(al_settings, screen, plane, bullets)
    if event.key == pygame.K_q:
        sys.exit()

def check_key_up_events(event, plane):
    if event.key == pygame.K_RIGHT:
        plane.mov_right = False
    if event.key == pygame.K_LEFT:
        plane.mov_left = False
    if event.key == pygame.K_UP:
        plane.mov_up = False
    if event.key == pygame.K_DOWN:
        plane.mov_down = False
    if event.key == pygame.K_SPACE:
        plane.space_down = False

#def create_explosion(screen, enemys, bullets, explosions, plane):

def plane_hit(plane, enemys, screen, al_settings, explosions, bullets, stats, scb):
    hits = pygame.sprite.spritecollide(plane, enemys, True)  #hits список enemy

    for hit in hits:
        stats.score += al_settings.enemy_points
        plane.hitpoints -= 1
        new_explosion = Explosion(screen, hit.rect.center)  # explosion в центр enemy
        new_explosion.flag = True
        explosions.add(new_explosion)
        scb.prep_score()
    if plane.hitpoints == 0:
        plane.hitpoints = al_settings.hitpoints
        stats.plane_limit -=1
        enemys.empty()
        bullets.empty()
        plane.center_plane()
        scb.prep_plane()

        if stats.plane_limit ==0:
            stats.game_active = False



def check_collision(screen, enemys, bullets, explosions, al_settings, stats, scb):

    collisions = pygame.sprite.groupcollide(enemys, bullets, True, True)  # словарь
    for enem in collisions.keys():
        stats.score += al_settings.enemy_points
        scb.prep_score()
        new_explosion = Explosion(screen, enem.rect.center)
        new_explosion.flag = True
        explosions.add(new_explosion)

    update_explosions(explosions)


def update_explosions(explosions):
    for expl in explosions.copy():
        if not expl.flag:
            explosions.remove(expl)

def update_bullets(bullets, enemys, al_settings, screen, explosions, plane, stats, scb):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    bullets.update()
    plane_hit(plane, enemys, screen, al_settings, explosions, bullets, stats, scb)
    check_collision(screen, enemys, bullets, explosions, al_settings, stats, scb)

    if len(enemys) == 0:
        al_settings.increase_speed()
        create_flt(al_settings, screen, enemys)
        create_flt2(al_settings, screen, enemys)
    for enem in enemys.copy():
        if enem.rect.top > al_settings.screen_h:
            enemys.remove(enem)


def update_enemys(enemys):
    enemys.update()

def update_screen(al_settings, screen, plane, bullets, enemys, explosions, anim_strelba, stats, play_button, star_list, scb):
    screen.fill(al_settings.bg_color)
    if stats.game_active:
        stars(star_list, screen, al_settings)
        plane.blitme()
        enemys.draw(screen)
        bullets.draw(screen)

    for expl in explosions:
        if anim_strelba == 5: # кадр анимации взрыва сменяется каждые 60/5 sec
            expl.count += 1
        expl.update()
    if not stats.game_active:
        play_button.draw_button()
    pygame.mouse.set_visible(not stats.game_active) # когда игра, курсор не виден
    scb.show_score()
    pygame.display.flip()
