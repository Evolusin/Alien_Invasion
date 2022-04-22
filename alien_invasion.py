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
            self._update_aliens()
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

    def _update_aliens(self):
        """Update position of aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        """Create fleet of aliens"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows for aliens
        ship_height = self.ship.rect.height
        available_space_y = (
                self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create full fleet of aliens
        for row_number in range (number_rows):
            # Create first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
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

    def _check_fleet_edges(self):
        """Respond to alien touch edges"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop enteire fleet down and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in row"""
        alien = Alien(self)
        alien_width, alien.height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

if __name__ == '__main__':
    # Make instance and run game
    ai = AlienInvasion()
    ai.run_game()