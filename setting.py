from random import randint, random


class Settings:
    """存储游戏《外星人游戏》所有设定类"""

    def __init__(self) -> None:
        """初始化游戏设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_height = 15
        self.bullet_width = 5
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 10

        # 外星人的设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 0.1
        # 向右为1，左为-1
        self.fleet_direction = randint(-1, 1)