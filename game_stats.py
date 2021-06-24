class Game_stats():
    def __init__(self, al_settings):
        self.al_settings = al_settings
        self.game_active = True
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.plane_limit = self.al_settings.plane_limit
        self.score = 0

