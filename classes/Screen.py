import pygame
from consts import *


# TODO: Add notes to class
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.set_window_caption()
        self.set_background_color()

    def get_screen(self):
        """Returns the pygame screen"""
        return self.screen

    def set_window_caption(self):
        """Sets a caption to game window"""
        pygame.display.set_caption(WINDOW_CAPTION)

    def set_background_color(self):
        """Sets a background color"""
        self.screen.fill(GREEN)

