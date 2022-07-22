import imp
from re import T
import sys
import pygame
from setting import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randint



class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_height = self.screen.get_rect().width
        self.settings.screen_width = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """开始游戏的循环"""
        while True:
            self._check_events_()
            self.ship.update()
            self._update_bullets()
            self._update_alien()
            self._update_screen_()

            # 每次循环都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()


    def _check_events_(self):
        """响应按键和鼠标"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._check_keydown_event_(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event_(event)

    def _check_keydown_event_(self, event):
        """响应按键"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.type == pygame.K_Q: # 退出程序
            sys.exit()

    def _check_keyup_event_(self, event):
        """响应松开"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一个新的子弹，并添加到类里"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """更新子弹位置，并删除出屏的子弹"""
        self.bullets.update()

        # 删除出屏的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # 检查是否击中外星人
        collsions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_alien(self):
        """
        检查是否有外星人在屏幕边缘
        并更新外星人群的位置
        """
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen_(self):
        """更新图像"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

    def _create_fleet(self):
        """创建外星人群"""
        # 创建一个外星人并计算一行有几个外星人
        # 外星人的间距为外星人的宽度
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        #计算屏幕容纳的外星人
        
        available_space_x = self.settings.screen_width - 500 - (2 * alien_width)
        number_aliens_x = available_space_x // (1 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (15 * alien_height) - ship_height)
        number_rows = available_space_y // (3 * alien_height)
        """
        number_rows = 5
        number_aliens_x = 4
        """
        for row_number in range(1, number_rows):
            for alien_number in range(1, number_aliens_x):
                if randint(0, 1):
                    self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        # 创建一个外星人并且加入
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x =  alien_width + alien_number * 2 * alien_width
        alien.rect.x = alien.x

        alien.y = row_number * alien_height 
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """如果外星人到边缘采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                alien.fleet_direction *= -1
            alien.y += self.settings.fleet_drop_speed





if __name__ == '__main__':
    #创建实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()