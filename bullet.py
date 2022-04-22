import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from ship"""
    def __init__(self,ai_game):
        """Create bullet object on ship current loacation"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # self.color = self.settings.bullet_color
        self.screen_rect = ai_game.screen.get_rect()

        # Create a bullet rect at (0.0) and then set correct position
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.image_load = pygame.image.load('images/knopers.png').convert_alpha()
        self.image = pygame.transform.scale(self.image_load, (64, 48))
        self.rect = self.image.get_rect()
        self.rect.midtop = ai_game.ship.rect.midtop
        # Store bullet position in decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet to screen"""
        # Update bullet position
        self.y -= self.settings.bullet_speed
        # Update rect y position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to the screen"""
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)