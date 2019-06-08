import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # 一个对飞机子弹管理的类

    def __init__(self, auto_settings, screen, plane):

        super().__init__()
        self.screen = screen

        # 在（0，0）出创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, auto_settings.bullet_width, auto_settings.bullet_height)
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = auto_settings.bullet_color
        self.speed_factor = auto_settings.bullet_speed_factor



    def update(self):
        # x向上移动子弹
        self.y -= self.speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        # 再屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)

