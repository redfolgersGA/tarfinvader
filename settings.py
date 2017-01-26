# CREATING A CLASS THAT WILL STORE ALL SETTINGS FOR MY GAME
class Settings():
# Initialize game settings and Set screen settings
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        # ship settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 20

        self.score_scale = 1.5
        # set to 3
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # set to 20
        self.ship_speed_factor = 20
        # set to 25
        self.bullet_speed_factor = 25
        # set to 20
        self.alien_speed_factor = 10

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        # self.ship_speed_factor *= self.speedup_scale
        # self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


