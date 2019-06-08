'''所有设置类'''
import pygame

class Settings(object):
    def __init__(self):
        # 屏幕设置
        self.screen_weith = 1440
        self.screen_height = 900
        self.background = pygame.image.load('./images/bg.jpg')

        self.plane_speed_factor = 13.8


        # 子弹设置
        self.bullet_speed_factor = 22
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60 ,120