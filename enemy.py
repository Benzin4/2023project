from settings import *
import pygame
import random


class SkeletonEnemy:
    def __init__(self):
        x = random.randrange(HALF_WIDTH+100, MAP_WIDHT)
        y = random.randrange(HALF_HEIHGT+100, MAP_HEIGHT)
        self.x, self.y = x, y


        self.animation_images = [pygame.image.load("images/skeleton_enemy/skeleton_down0.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down1.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down2.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down3.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down4.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down5.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down6.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down7.png").convert_alpha(),
                               pygame.image.load("images/skeleton_enemy/skeleton_down8.png").convert_alpha()]
        self.animation_count = 0

    def main(self, cam_x, cam_y, window):
        self.player_x = HALF_WIDTH
        self.player_y = HALF_HEIHGT
        self.cam_x = cam_x
        self.cam_y = cam_y
        if self.animation_count + 1 == 36:
            self.animation_count = 0
        self.animation_count += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.cam_y < HALF_HEIHGT-25:
                self.y += display_sroll_speed
        if keys[pygame.K_s]:
            if self.cam_y > -reg_pos_y+125:
                self.y -= display_sroll_speed
        if keys[pygame.K_a]:
            if self.cam_x < HALF_WIDTH-25:
                self.x += display_sroll_speed
        if keys[pygame.K_d]:
            if self.cam_x > -reg_pos_x+100:
                self.x -= display_sroll_speed
        if self.x < self.player_x:
            self.x += enemy_speed
        elif self.x > self.player_x:
            self.x -= enemy_speed
        if self.y < self.player_y:
            self.y += enemy_speed
        elif self.y > self.player_y:
            self.y -= enemy_speed
        
        window.blit(self.animation_images[self.animation_count // 4], (self.x, self.y))
        self.enemy_rect = self.animation_images[0].get_rect(topleft=(self.x, self.y))
    