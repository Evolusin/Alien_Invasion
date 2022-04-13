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
            #Watch for keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Set up filling screen
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Draw screen visable
            pygame.display.flip()

if __name__ == '__main__':
    # Make instance and run game
    ai = AlienInvasion()
    ai.run_game()