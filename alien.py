import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a alien"""

    def __init__(self, ai_game):
        """Initialize  alien and its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load alien image
        self.image_load = pygame.image.load('images/Maciej_v3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_load, (80, 60))
        self.rect = self.image.get_rect()

        # Start new alien and top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien at horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Make alien go right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """Returns True if alien touches edge"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
