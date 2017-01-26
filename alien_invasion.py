# IMPORT SYS AND PYGAME MODULES


import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Score
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

# INITIALIZE GAME AND CREATE A SCREEN OBJECT
def run_game():
    # initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("GA Invasion")

    play_button = Button(ai_settings, screen, "Play")

    # stores game stats
    stats = GameStats(ai_settings)
    sb = Score(ai_settings, screen, stats)

    # making a ship
    ship = Ship(ai_settings, screen)
    # making a group to store bullets in
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

# SET BG COLOR
    bg_color = (230, 230, 230)
# START THE MAIN LOOP FOR THE GAME
    while True:
# WATCH FOR KEYBOARD AND MOUSE EVENTS
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
            aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
            bullets, play_button)

run_game()
