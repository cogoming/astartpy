import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    #init game and create screen
    pygame.init();
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship =  Ship(ai_settings,screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    #start game main
    while True:

        # 监视键盘和鼠标事件
        #gf.check_events(ship);
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        #每次循环时都重绘屏幕
        #gf.update_screen(ai_settings,screen,ship)
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game();
