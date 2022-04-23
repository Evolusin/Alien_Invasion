import sys
from time import sleep
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


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

        # Store game stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self, "Play")



    def run_game(self):
        """Start game"""
        while True:
            self._check_events()
            if self.stats.game_active == True:
                self._update_bullets()
                self._update_aliens()
                self.ship.update()
            self._update_screen()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _update_aliens(self):
        """Update position of aliens in fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        self._check_aliens_bottom()

        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """Respond to ship being hit by alien"""
        if self.stats.ships_left > 0:
            # Lower value of ships
            self.stats.ships_left -= 1
            # Remove bullets and aliens
            self.aliens.empty()
            self.bullets.empty()

            # Create new ship and fleet
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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
        # Draw button
        if self.stats.game_active == False:
            self.play_button.draw_button()
        # Draw screen visable
        pygame.display.flip()

    def _check_aliens_bottom(self):
        """Check if any aleins have reachd the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # if aliens touch bottom screen -> act as hit
                self._ship_hit()
                break

    def _update_bullets(self):
        self.bullets.update()
        # get rid of bullets
        for i in self.bullets.copy():
            if i.rect.bottom <= 0:
                self.bullets.remove(i)
        # Check any bullets that have hit aliens
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        """Respond to alien-bullet collison"""
        collisons = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

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
        elif event.key == pygame.K_p:
            self._check_play_button()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_play_button(self,mouse_pos):
        """Start the new game when play is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            # Reset aliens/bullets
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            # Hide mouse cursor
            pygame.mouse.set_visible(False)
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