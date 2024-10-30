from settings import *
import pygame

class Menu:
    def __init__(self):
        self.option_surfaces = []
        self.callbacks = []
        self.curent_option_index = 0
    
    def append_option(self, font, option, callback):
        self.option_surfaces.append(font.render(option, True, WHITE))
        self.callbacks.append(callback)
    
    def switch(self, direction):
        self.curent_option_index = max(0, min(self.curent_option_index + direction, len(self.option_surfaces) - 1))

    def select(self):
        self.callbacks[self.curent_option_index]()
    
    def draw_menu(self, window, x, y, option_y_padding):
        for (i, option) in enumerate(self.option_surfaces):
            option_rect = option.get_rect(topleft = (x, y + i * option_y_padding))
            if i == self.curent_option_index:
                pygame.draw.rect(window, DARK_RED, option_rect)
            window.blit(option, option_rect)