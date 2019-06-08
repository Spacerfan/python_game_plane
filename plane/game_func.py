import sys

import pygame

from bullet import Bullet



def check_keydown_events(event, auto_settings, screen, plane, bullets):
    # 响应按键
    if event.key == pygame.K_RIGHT:
        # 向右移动飞机
        plane.moving_right = True

    elif event.key == pygame.K_LEFT:
        plane.moving_left = True

    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并加入到编组bullets中
        new_bullet = Bullet(auto_settings, screen, plane)
        bullets.add(new_bullet)


def check_keyup_events(event, plane):
    # 响应松开按键
    if event.key == pygame.K_RIGHT:
        plane.moving_right = False

    elif event.key == pygame.K_LEFT:
        plane.moving_left = False



# 管理事件
def check_events(auto_settings, screen, plane, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, auto_settings, screen, plane, bullets)


        elif event.type == pygame.KEYUP:
            check_keyup_events(event, plane)


# 更新屏幕
def update_screen(auto_settings, screen, plane, bullets):
    # 每次循环都会重绘屏幕
    # 插入背景图
    screen.blit(auto_settings.background, (0, 0))

    # z再飞机和外星人后重绘子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    plane.blitme()
    # 重绘屏幕
    pygame.display.flip()

