# game settings

WIDHT = 1000 #1200
HEIGHT = 600 #800
HALF_WIDTH = WIDHT // 2
HALF_HEIHGT = HEIGHT // 2
FPS = 60

# map settings
MAP_WIDHT = 1200
MAP_HEIGHT = 800
MAP_HALF_WIDTH = MAP_WIDHT // 2
MAP_HALF_HEIHGT = MAP_HEIGHT // 2

# player settings

player_pos = (HALF_WIDTH, HALF_HEIHGT) 
cam_pos = (HALF_WIDTH-100, HALF_HEIHGT-100)
reg_pos_x = MAP_WIDHT - WIDHT + HALF_WIDTH
reg_pos_y = MAP_HEIGHT - HEIGHT + HALF_HEIHGT 
display_sroll_speed = 4
bullet_speed = 15


# enemy settings

enemy_pos = (HALF_WIDTH-100, HALF_HEIHGT-100)
enemy_speed = 2
enemy_time_spawn = 2500
enemy_counter_l1 = 25
enemy_counter_l2 = 40
enemy_counter_l3 = 60

# colors

WHITE = (255, 255, 255)
DARK_GRAY = (110, 110, 110)
BLACK = (0 , 0, 0)
RED = (220, 0, 0)
DARK_RED = (110, 0 , 0)
GREEN =(0, 220, 0)
BLUE = (0, 0, 220)
PURPLE = (120, 0, 120)