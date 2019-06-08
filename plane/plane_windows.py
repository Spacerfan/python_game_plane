import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from plane import Plane
import game_func as gf



def run_game():
    # 初始化屏幕大小
    pygame.init()
    auto_settings = Settings()

    screen = pygame.display.set_mode((auto_settings.screen_weith, auto_settings.screen_height))
    pygame.display.set_caption("飞机大战——beta 0.0.1")
    plane = Plane(auto_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 游戏主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(auto_settings, screen, plane, bullets)
        plane.update()
        bullets.update()
        gf.update_screen(auto_settings, screen, plane, bullets)


run_game()