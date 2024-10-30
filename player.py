from settings import *
import pygame
import math

class Player:
    def __init__(self):
        self.x, self.y = cam_pos
        self.moving_top = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    @property
    def pos(self):
        return(self.x, self.y)

    def display_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.y < HALF_HEIHGT-25:
                self.y += display_sroll_speed
            self.moving_top =True
        if keys[pygame.K_s]:
            if self.y > -reg_pos_y+125:
                self.y -= display_sroll_speed
            self.moving_down = True
        if keys[pygame.K_a]:
            if self.x < HALF_WIDTH-25:
                self.x += display_sroll_speed
            self.moving_left = True
        if keys[pygame.K_d]:
            if self.x > -reg_pos_x+100:
                self.x -= display_sroll_speed
            self.moving_right = True

    def draw_head(self, window, player_weapon):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        rel_x, rel_y = mouse_x - HALF_WIDTH, mouse_y - HALF_HEIHGT
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        
        player_weapon = pygame.transform.scale(player_weapon, (63, 48))
        player_weapon_copy = pygame.transform.rotate(player_weapon, angle)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            window.blit(player_weapon_copy, (HALF_WIDTH + 60 - int(player_weapon_copy.get_width()/2), 
                                         HALF_HEIHGT + 38 - int(player_weapon_copy.get_height()/2)))
        elif keys[pygame.K_w]:
            window.blit(player_weapon_copy, (HALF_WIDTH + 38 - int(player_weapon_copy.get_width()/2), 
                                         HALF_HEIHGT + 60 - int(player_weapon_copy.get_height()/2)))
        else:
            window.blit(player_weapon_copy, (HALF_WIDTH + 38 - int(player_weapon_copy.get_width()/2), 
                                         HALF_HEIHGT + 38 - int(player_weapon_copy.get_height()/2)))

    def draw_player(self, window, player_walk):
        if self.moving_down:
            window.blit(pygame.transform.scale(player_walk[0],(75, 100)), (player_pos))
            self.player_rect = pygame.transform.scale(player_walk[0],(75, 100)).get_rect(topleft=(player_pos))
        elif self.moving_top:
            window.blit(pygame.transform.scale(player_walk[1],(75, 100)), (player_pos))
            self.player_rect = pygame.transform.scale(player_walk[0],(75, 100)).get_rect(topleft=(player_pos))
        elif self.moving_left:
            window.blit(pygame.transform.scale(player_walk[2],(100, 75)), (player_pos))
            self.player_rect = pygame.transform.scale(player_walk[2],(100, 75)).get_rect(topleft=(player_pos))
        elif self.moving_right:
            window.blit(pygame.transform.scale(player_walk[3],(100, 75)), (player_pos))
            self.player_rect = pygame.transform.scale(player_walk[2],(100, 75)).get_rect(topleft=(player_pos))
        else:
            window.blit(pygame.transform.scale(player_walk[0],(75, 100)), (player_pos))
            self.player_rect = pygame.transform.scale(player_walk[0],(75, 100)).get_rect(topleft=(player_pos))

        self.moving_top = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def reset_player_pos(self):
        self.x, self.y = cam_pos

class PlayerBullet:
    def __init__(self):
        self.x, self.y = HALF_WIDTH + 38, HALF_HEIHGT + 38
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.speed = bullet_speed
        self.angle = math.atan2(self.y - mouse_y, self.x - mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def draw_bullet(self, window):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y += display_sroll_speed
        if keys[pygame.K_s]:
            self.y -= display_sroll_speed
        if keys[pygame.K_a]:
            self.x += display_sroll_speed
        if keys[pygame.K_d]:
            self.x -= display_sroll_speed

        surf_bullet = pygame.Surface((4, 4))
        surf_bullet.set_alpha(0)
        pygame.draw.circle(window, BLACK, (self.x, self.y), 4)
        self.bullet_rect = surf_bullet.get_rect(topleft=(self.x, self.y))
