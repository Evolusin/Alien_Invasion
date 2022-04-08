import sys
import pygame

class AlienInvasion:
    """Menage game assets and behavior"""

    def __init__(self):
        """Intialize game"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        # Set BG Color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start game"""
        while True:
            #Watch for keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Set up filling screen
            self.screen.fill(self.bg_color)
            # Draw screen visable
            pygame.display.flip()
if __name__ == '__main__':
    # Make instance and run game
    ai = AlienInvasion()
    ai.run_game()