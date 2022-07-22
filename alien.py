import pygame
from pygame.sprite import Sprite
from random import randint


class Alien(Sprite):
    """表示单个alien的类"""

    def __init__(self, ai_game) -> None:
        """模仿外星人，并设置起点"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        # 外星人的位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 存储外星人的方向
        self.fleet_direction = randint(-1, 1)

    def update(self) -> None:
        """随机移动外星人"""
        self.x += (self.settings.alien_speed * self.fleet_direction)

        """
        x = randint(-5, 5)
        if x and self.rect.right < self.screen_rect.right :
            self.x += x
        elif x and self.rect.left > self.screen_rect.left :
            self.x -= x
        """

        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """如果外星人在边缘，就返回ture"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
            