import pygame
from consts import *
import random

# TODO: Add notes to class
class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.set_window_caption()
        self.set_background_color(GREEN)
        self.bushes = []
        self.insert_rnd_bushes()
        pygame.font.init()

    def get_screen(self):
        """Returns the pygame screen"""
        return self.screen

    def get_bushes(self):
        """Returns the bushes list"""
        return self.bushes

    def set_window_caption(self):
        """Sets a caption to game window"""
        pygame.display.set_caption(WINDOW_CAPTION)

    def set_background_color(self, color):
        """Sets a background color"""
        self.screen.fill(color)

    def draw_object(self, img_path, location, size):
        """Draws an object to screen"""
        original_img = pygame.image.load(img_path)
        img = pygame.transform.scale(original_img, size)
        self.screen.blit(img, location)

    def draw_text(self, text, color, size, font, location):
        """Draw text to screen"""
        txt_font = pygame.font.SysFont(font, size)
        text_surface = txt_font.render(text, False, color)
        self.screen.blit(text_surface, location)

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

    def draw_flag(self):
        """Draws the flag"""
        location = (FLAG_X, FLAG_Y)
        size = (FLAG_WIDTH, FLAG_HEIGHT)
        self.draw_object(FLAG_IMG_PATH, location, size)

    def draw_line_horizontal(self, y):
        """Draws a horizontal line"""
        pygame.draw.line(self.screen, GREEN, (MIN_X, y), (MAX_X, y), LINE_WIDTH)

    def draw_line_vertical(self, x):
        """Draws a vertical line"""
        pygame.draw.line(self.screen, GREEN, (x, MIN_Y), (x, MAX_Y), LINE_WIDTH)

    def draw_mines(self, game_field):
        """Draws the mines on the screen"""
        # Get the mines location list
        mines = game_field.get_mines()
        size = (MINE_WIDTH, MINE_HEIGHT)
        for mine_location in mines:
            # Display each mine
            self.draw_object(MINE_IMG_PATH, mine_location, size)

