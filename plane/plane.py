import pygame

class Plane():
    def __init__(self, auto_settings, screen):

        self.screen = screen

        self.auto_settings = auto_settings

        # 加载飞机图像并获取其外形
        image = pygame.image.load('images/plane.png')
        self.image = pygame.transform.smoothscale(image,(60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每架飞机放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 在飞船的属性中center中储存小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # 根据移动标志移动飞机位置
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.auto_settings.plane_speed_factor
        if self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.auto_settings.plane_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center


    def blitme(self):
        self.screen.blit(self.image, self.rect)
