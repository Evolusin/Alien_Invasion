import pygame

class Ship:
    """Class representing ship"""
    def __init__(self,ai_game):
        """Initialize ship and set his position"""
        self.screen = ai_game.sceen
        self.screen_rect = ai_game.sceen.get_rect()

        #load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start ship on bottom screem
        self.rect.midbottom = self.screen_rect.midbottom