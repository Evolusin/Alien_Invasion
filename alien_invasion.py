import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Menage game assets and behavior"""

    def __init__(self):
        """Intialize game"""
        pygame.init()
        # Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """Start game"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
    def _check_events(self):
        """Responds to keypresses and mouse events"""
        # Watch for keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left= False
    def _update_screen(self):
        """Update and refresh screen"""
        # Set up filling screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Draw screen visable
        pygame.display.flip()

if __name__ == '__main__':
    # Make instance and run game
    ai = AlienInvasion()
    ai.run_game()