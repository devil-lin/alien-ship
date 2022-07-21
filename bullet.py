import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理子弹发的类"""

    def __init__(self, ai_game) -> None:
        """在飞船当前位置创建一个类"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # 设置子弹位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 用小数保存子弹位置
        self.y = float(self.rect.y)

    def update(self):
        """向上移动的子弹"""
        # 更新子弹的位置
        self.y -= self.settings.bullet_speed
        # 更新子弹的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

        