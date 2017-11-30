import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    #init game and create screen
    pygame.init();
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建一艘飞船、一个子弹编组和一个外星人编组
    ship =  Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建一个用于存储外星人的编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen,ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        #gf.check_events(ship);
        gf.check_events(ai_settings, screen,stats,play_button, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens,bullets)
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        #每次循环时都重绘屏幕
        #gf.update_screen(ai_settings,screen,ship)
        gf.update_screen(ai_settings, screen, stats,ship,aliens,bullets,play_button)
run_game();
