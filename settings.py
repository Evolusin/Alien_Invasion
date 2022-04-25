class Settings:
    """Holding all game settings"""

    def __init__(self):
        """Initilize game settings"""
        # Screen settings
        self.screen_width = 1111
        self.screen_height = 700
        self.bg_color = (100, 100, 255)
        # Ship settings
        self.ship_speed = 0.2
        self.ship_limit = 1
        # Bullet settings
        self.bullet_speed = 0.2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 60)
        self.bullet_allowed = 3
        # Alien settings
        self.alien_speed = 0.12
        self.fleet_drop_speed = 20
        # Fleet direction 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Point values scale
        self.score_scale = 1.5

        # Speed-up scale
        self.speedup_scale = 1.3
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Init settings that change"""
        self.ship_speed = 0.35
        self.bullet_speed = 0.2
        self.alien_speed = 0.12
        self.fleet_direction = 1
        # Scores
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed"""
        # self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)