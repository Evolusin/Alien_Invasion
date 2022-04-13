import pygame

class Ship:
    """Class representing ship"""
    def __init__(self,ai_game):
        """Initialize ship and set his position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship
        self.image_load = pygame.image.load('images/ship_v2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_load,(100,74))
        self.rect = self.image.get_rect()
        # Start ship on bottom screem
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image,self.rect)