import pygame.font

class Scoreboard:
    """Class that represents scoreboard"""

    def __init__(self, ai_game):
        """Atributes of scorekeeping"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats =ai_game.stats

        # Font settings
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()

    def prep_score(self):
        """Turn the score to image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Display score in top right place of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw scoreboard to the screen"""
        self.screen.blit(self.score_image, self.score_rect)