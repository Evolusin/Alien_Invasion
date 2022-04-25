import pygame.font
import json

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
        self.prep_high_score()

    def prep_score(self):
        """Turn the score to image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                                            self.text_color, self.settings.bg_color)

        # Display score in top right place of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def read_high_score(self):
        with open('highscore.json') as outfile:
            new_high = json.load(outfile)
            self.stats.high_score = new_high
        self.prep_high_score()


    def save_high_score(self):
            with open('highscore.json') as outfile:
                f_highscore = json.load(outfile)
                if f_highscore < self.stats.high_score:
                    with open('highscore.json', 'w') as outfile:
                        json.dump(self.stats.high_score, outfile)

    def show_score(self):
        """Draw scoreboard to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Turn the high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Centre the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def check_high_score(self):
        """Check if there is new high score"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()