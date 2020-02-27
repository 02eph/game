class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 2
        self.ship_limit = 3

        self.bullet_speed_factor = 3.5
        self.bullet_width = 4
        self.bullet_height = 20
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 5

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #движение вправо, -1 влево
        self.fleet_direction = 1
