import pygame


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接图像
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # 对于每一艘新飞船，都将其放在屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 飞船的位置
        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据标志移动飞船"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left :
            self.x -= self.settings.ship_speed

        # 更新rect_x
        self.rect.x = self.x

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
