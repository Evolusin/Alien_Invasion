class Settings:
    """Holding all game settings"""

    def __init__(self):
        """Initilize game settings"""
        # Screen settings
        self.screen_width = 1111
        self.screen_height = 700
        self.bg_color = (100, 100, 255)
        # Ship speed
        self.ship_speed = 0.2
        # Bullet settings
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 60)
        self.bullet_allowed = 3
        # Alien settings
        self.alien_speed = 0.1
        self.fleet_drop_speed = 14
        # Fleet direction 1 represents right; -1 represents left
        self.fleet_direction = 1