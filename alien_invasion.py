import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Menage game assets and behavior"""

    def __init__(self):
        """Intialize game"""
        pygame.init()
        # Settings
        self.settings = Settings()
        self.screen = pygame.display.set_mode\
            ((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        """Start game"""
        while True:
            self._check_events()
            self._update_bullets()
            self._update_screen()
            self.ship.update()
    def _check_events(self):
        """Responds to keypresses and mouse events"""
        # Watch for keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _create_fleet(self):
        """Create fleet of aliens"""
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create first row of aliens
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)
    def _update_screen(self):
        """Update and refresh screen"""
        # Set up filling screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Alien creation
        self.aliens.draw(self.screen)
        # Draw screen visable
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        # get rid of bullets
        for i in self.bullets.copy():
            if i.rect.bottom <= 0:
                self.bullets.remove(i)

    def _check_keydown_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self,event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    def _fire_bullets(self):
        """Create bullet and it to bullets Group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
if __name__ == '__main__':
    # Make instance and run game
    ai = AlienInvasion()
    ai.run_game()