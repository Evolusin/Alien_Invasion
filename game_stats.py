class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Init statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start and set status to active
        self.game_active = False

        # High score
        self.high_score = 0

    def reset_stats(self):
        """Init changing stats"""
        self.ships_left = self.settings.ship_limit
        self.score = 0