import pygame
from consts import *
import random


# TODO: Add notes to class
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.set_window_caption()
        self.set_background_color()
        self.bushes = []
        self.insert_rnd_bushes()

    def get_screen(self):
        """Returns the pygame screen"""
        return self.screen

    def set_window_caption(self):
        """Sets a caption to game window"""
        pygame.display.set_caption(WINDOW_CAPTION)

    def set_background_color(self):
        """Sets a background color"""
        self.screen.fill(GREEN)

    def draw_object(self, img_path, location, size):
        """Draws an object to screen"""
        original_img = pygame.image.load(img_path)
        img = pygame.transform.scale(original_img, size)
        self.screen.blit(img, location)

    def insert_rnd_bushes(self):
        """Creates the random bushes dict"""
        for bush in range(BUSH_COUNT):
            rnd_x = random.randint(MIN_X, MAX_X)
            rnd_y = random.randint(MIN_Y, MAX_Y)
            # Bush size and location
            location = (rnd_x, rnd_y)
            size = BUSH_SIZE
            # Create the bush dict
            bush_dict = {BUSH_LOCATION_KEY: location, BUSH_SIZE_KEY: size}
            self.bushes.append(bush_dict)

    def draw_rnd_bushes(self):
        """Draws bushes on random locations"""
        for bush in self.bushes:
            self.draw_object(BUSH_IMG_PATH, bush.get(BUSH_LOCATION_KEY), bush.get(BUSH_SIZE_KEY))

