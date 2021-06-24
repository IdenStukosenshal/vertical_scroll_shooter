class Settings():
    def __init__(self):
        self.screen_w = 900
        self.screen_h = 900
        self.bg_color = (5, 30, 60)
        self.bullet_allowed = 10
        self.hitpoints = 2
        self.plane_limit = 2

        self.speed_scale = 1.01
        self.enemy_points  = 5

        self.initial_dynamic_settings()

    def initial_dynamic_settings(self):
        self.star_speed = 10
        self.plane_speed_f = 5.5
        self.bullet_speed = 13
        self.enemy_w_speed = 2
        self.enemy_h_speed = 1

        self.enemy2_h_speed = 2

    def increase_speed(self):
        self.star_speed *= self.speed_scale
        self.plane_speed_f *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.enemy_w_speed *= self.speed_scale
        self.enemy_h_speed *= self.speed_scale

        self.enemy2_h_speed *= self.speed_scale




