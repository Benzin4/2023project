import pygame
from settings import *
from player import Player
from player import PlayerBullet
from enemy import SkeletonEnemy
from menu import Menu

pygame.init()
window = pygame.display.set_mode((WIDHT, HEIGHT))
clock = pygame.time.Clock()
player = Player()

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, enemy_time_spawn)

icon = pygame.image.load("images/icon.png").convert_alpha()
bg1 = pygame.image.load("images/backgrounds/background1.png").convert_alpha()
bg2 = pygame.image.load("images/backgrounds/background2.png").convert_alpha()
bg3 = pygame.image.load("images/backgrounds/background3.png").convert_alpha()
player_walk = [pygame.image.load("images/tank_player/tank_down.png").convert_alpha(), pygame.image.load("images/tank_player/tank_top.png").convert_alpha(),
               pygame.image.load("images/tank_player/tank_left.png").convert_alpha(), pygame.image.load("images/tank_player/tank_right.png").convert_alpha()]
player_weapon = pygame.image.load("images/tank_player/tank_head.png").convert_alpha()
main_font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 52)
text_font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 64)

pygame.display.set_caption("Skull crusher")
pygame.display.set_icon(icon)

game_name_text = text_font.render("SKULL CRUSHER", True, WHITE)
you_win_text = text_font.render("YOU WIN!", True, WHITE)
you_lose_text = text_font.render("YOU LOSE!", True, WHITE)
pause_text = text_font.render("PAUSE", True, WHITE)

player_bullets = []
enemy_list = []
enemy_counter = 0

in_game = False
in_menu = True
select_level = False
restart_level = False
select_about = False
choose_level1 = False
choose_level2 = False
choose_level3 = False
lose = False
win = False

main_menu = Menu()
main_menu.append_option(main_font, "START", lambda: print("Выбран 'START'"))
main_menu.append_option(main_font, "ABOUT", lambda: print(about_text))
main_menu.append_option(main_font, "QUIT", exit)

level_menu = Menu()
level_menu.append_option(main_font, "LEVEL 1", lambda: print("Выбран 'LEVEL 1'"))
level_menu.append_option(main_font, "LEVEL 2", lambda: print("Выбран 'LEVEL 2'"))
level_menu.append_option(main_font, "LEVEL 3", lambda: print("Выбран 'LEVEL 3'"))
level_menu.append_option(main_font, "BACK", lambda: print("Выбран 'BACK'"))

lose_menu = Menu()
lose_menu.append_option(main_font, "RESTART", lambda: print("Выбран 'RESTART'"))
lose_menu.append_option(main_font, "CHOOSE LEVEL", lambda: print("Выбран 'CHOOSE LEVEL'"))
lose_menu.append_option(main_font, "MAIN MENU", lambda: print("Выбран 'MAIN MENU'"))
lose_menu.append_option(main_font, "QUIT FROM GAME", exit)

win_menu = Menu()
win_menu.append_option(main_font, "RESTART", lambda: print("Выбран 'RESTART'"))
win_menu.append_option(main_font, "CHOOSE LEVEL", lambda: print("Выбран 'CHOOSE LEVEL'"))
win_menu.append_option(main_font, "MAIN MENU", lambda: print("Выбран 'MAIN MENU'"))
win_menu.append_option(main_font, "QUIT FROM GAME", exit)

while True:

    while in_menu:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    main_menu.switch(-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    main_menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    main_menu.select()
                    if main_menu.curent_option_index == 0:
                        select_level = True
                        in_menu = False

        window.fill(DARK_GRAY)
        window.blit(game_name_text, (20, 20))
        main_menu.draw_menu(window, 20, 150, 60)

        pygame.display.flip()
        clock.tick(FPS)

    while select_level:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    level_menu.switch(-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    level_menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    level_menu.select()
                    if level_menu.curent_option_index == 0:
                        choose_level1 = True
                        select_level = False
                    elif level_menu.curent_option_index == 1:
                        choose_level2 = True
                        select_level = False
                    elif level_menu.curent_option_index == 2:
                        choose_level3 = True
                        select_level = False
                    elif level_menu.curent_option_index == 3:
                        in_menu = True
                        select_level = False

        window.fill(DARK_GRAY)
        window.blit(game_name_text, (20, 20))
        level_menu.draw_menu(window, 20, 150, 60)

        pygame.display.flip()
        clock.tick(FPS)

    while choose_level1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_bullets.append(PlayerBullet())
            if event.type == enemy_timer and enemy_counter != enemy_counter_l1:
                enemy_list.append(SkeletonEnemy())
                enemy_counter += 1

        player.display_movement()
        window.fill(DARK_GRAY)
        window.blit(bg1, (player.pos))

        player.draw_player(window, player_walk)
        player.draw_head(window, player_weapon)

        if player_bullets:
            for bullet in (player_bullets):
                bullet.draw_bullet(window)

        if enemy_list:
            for (index, enemy) in enumerate(enemy_list):
                enemy.main(player.x, player.y, window)
                if player.player_rect.colliderect(enemy.enemy_rect):
                    lose = True
                    level = 1
                    enemy_list = []
                    player_bullets = []
                    player.reset_player_pos()
                    choose_level1 = False
                for (i, bullet) in enumerate(player_bullets):
                    if bullet.bullet_rect.colliderect(enemy.enemy_rect):
                        enemy_list.pop(index)
                        player_bullets.pop(i)
        elif enemy_counter == enemy_counter_l1:
            win = True
            level = 1
            enemy_list = []
            player_bullets = []
            player.reset_player_pos()
            choose_level1 = False

        pygame.display.flip()
        clock.tick(FPS)

    while choose_level2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_bullets.append(PlayerBullet())
            if event.type == enemy_timer and enemy_counter != enemy_counter_l2:
                enemy_list.append(SkeletonEnemy())
                enemy_counter += 1

        player.display_movement()
        window.fill(DARK_GRAY)
        window.blit(bg2, (player.pos))

        player.draw_player(window, player_walk)
        player.draw_head(window, player_weapon)

        if player_bullets:
            for bullet in (player_bullets):
                bullet.draw_bullet(window)

        if enemy_list:
            for (index, enemy) in enumerate(enemy_list):
                enemy.main(player.x, player.y, window)
                if player.player_rect.colliderect(enemy.enemy_rect):
                    lose = True
                    level = 2
                    enemy_list = []
                    player_bullets = []
                    player.reset_player_pos()
                    choose_level2 = False
                for (i, bullet) in enumerate(player_bullets):
                    if bullet.bullet_rect.colliderect(enemy.enemy_rect):
                        enemy_list.pop(index)
                        player_bullets.pop(i)
        elif enemy_counter == enemy_counter_l2:
            win = True
            level = 2
            enemy_list = []
            player_bullets = []
            player.reset_player_pos()
            choose_level2 = False

        pygame.display.flip()
        clock.tick(FPS)

    while choose_level3:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_bullets.append(PlayerBullet())
            if event.type == enemy_timer and enemy_counter != enemy_counter_l3:
                enemy_list.append(SkeletonEnemy())
                enemy_counter += 1

        player.display_movement()
        window.fill(DARK_GRAY)
        window.blit(bg3, (player.pos))

        player.draw_player(window, player_walk)
        player.draw_head(window, player_weapon)

        if player_bullets:
            for bullet in (player_bullets):
                bullet.draw_bullet(window)

        if enemy_list:
            for (index, enemy) in enumerate(enemy_list):
                enemy.main(player.x, player.y, window)
                if player.player_rect.colliderect(enemy.enemy_rect):
                    lose = True
                    level = 3
                    enemy_list = []
                    player_bullets = []
                    player.reset_player_pos()
                    choose_level3 = False
                for (i, bullet) in enumerate(player_bullets):
                    if bullet.bullet_rect.colliderect(enemy.enemy_rect):
                        enemy_list.pop(index)
                        player_bullets.pop(i)
        elif enemy_counter == enemy_counter_l3:
            win = True
            level = 3
            enemy_list = []
            player_bullets = []
            player.reset_player_pos()
            choose_level3 = False

        pygame.display.flip()
        clock.tick(FPS)

    while lose:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    lose_menu.switch(-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    lose_menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    lose_menu.select()
                    if lose_menu.curent_option_index == 0:
                        if level == 1:
                            choose_level1 = True
                            lose = False
                        if level == 2:
                            choose_level2 = True
                            lose = False
                        if level == 3:
                            choose_level3 = True
                            lose = False
                    if lose_menu.curent_option_index == 1:
                        select_level = True
                        lose = False
                    if lose_menu.curent_option_index == 2:
                        in_menu = True
                        lose = False

        window.fill(DARK_GRAY)
        window.blit(you_lose_text, (20, 20))
        lose_menu.draw_menu(window, 20, 150, 60)

        pygame.display.flip()
        clock.tick(FPS)

    while win:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    win_menu.switch(-1)
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    win_menu.switch(1)
                elif event.key == pygame.K_SPACE:
                    win_menu.select()
                    if win_menu.curent_option_index == 0:
                        if level == 1:
                            choose_level1 = True
                            win = False
                        if level == 2:
                            choose_level2 = True
                            win = False
                        if level == 3:
                            choose_level3 = True
                            win = False
                    if win_menu.curent_option_index == 1:
                        select_level = True
                        win = False
                    if win_menu.curent_option_index == 2:
                        in_menu = True
                        win = False

        window.fill(DARK_GRAY)
        window.blit(you_win_text, (20, 20))
        win_menu.draw_menu(window, 20, 150, 60)

        pygame.display.flip()
        clock.tick(FPS)
