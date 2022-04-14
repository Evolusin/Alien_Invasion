class Settings:
    """Holding all game settings"""

    def __init__(self):
        """Initilize game settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (100, 100, 255)
        # Ship speed
        self.ship_speed = 0.2
        # Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 0, 60)