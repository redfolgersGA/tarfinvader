import pygame
# Create a class ship and initialize an instance of the Ship also set its starting point
class Ship():

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect. rect is a rectangle. pygame treats
        # game elements like rectangles. a very powerful tool
        self.image = pygame.image.load('images/ship2.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # this starts each new ship object at the bottm center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center
        # draws the ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx




















