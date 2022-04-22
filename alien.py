import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Class to represent a alien"""

    def __init__(self, ai_game):
        """Initialize  alien and its starting position"""
        super().__init__()
        self.screen = ai_game.screen

        #load alien image
        self.image_load = pygame.image.load('images/Maciej.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_load, (80, 60))
        self.rect = self.image.get_rect()

        # Start new alien and top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien at horizontal position
        self.x = float(self.rect.x)