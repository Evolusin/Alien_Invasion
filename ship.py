import pygame

class Ship:
    """Class representing ship"""
    def __init__(self,ai_game):
        """Initialize ship and set his position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load ship
        self.image_load = pygame.image.load('images/Szafa.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image_load,(100,120))
        self.rect = self.image.get_rect()
        # Start ship on bottom screem
        self.rect.midbottom = self.screen_rect.midbottom
        # Store decimal number for ship horizontal position
        self.x = float(self.rect.x)
        # Store decimal number for ship Y position
        self.y = float(self.rect.y)
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw ship at current location"""
        self.screen.blit(self.image,self.rect)

    def update(self):
        """Update ship position based on moving flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_ship(self):
        """Centre the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        # self.x = float(self.rect.x)