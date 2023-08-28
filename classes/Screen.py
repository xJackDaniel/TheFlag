import pygame
from consts import *
import random


def set_window_caption():
    """Sets a caption to game window"""
    pygame.display.set_caption(WINDOW_CAPTION)


class Screen:
    """Class that represents the pygame screen"""
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        set_window_caption()
        self.set_background_color(GREEN)
        self.bushes = []
        self.insert_rnd_bushes()
        pygame.font.init()

    def get_screen(self):
        """
            Returns the pygame screen
            :rtype: Screen Object
        """
        return self.screen

    def get_bushes(self):
        """
            Returns the bushes list
            :rtype: list
        """
        return self.bushes

    def set_background_color(self, color):
        """
            Sets a background color
            :param color: tuple (r,g,b)
        """
        self.screen.fill(color)

    def draw_object(self, img_path, location, size, transparent=False):
        """
            Draws an object to screen
            :param img_path: str
            :param location: tuple (x, y)
            :param size: tuple (width, height)
            :param transparent: bool (optional)
        """
        original_img = pygame.image.load(img_path)
        if transparent:
            original_img.set_alpha(TRANSPARENT_ALPHA_NUM)
        img = pygame.transform.scale(original_img, size)
        self.screen.blit(img, location)

    def draw_text(self, text, color, size, font, location):
        """
            Draw text to screen
            :param text: str
            :param color: tuple (r,g,b)
            :param size: tuple (width, height)
            :param font: str
            :param location: tuple (x, y)
        """
        txt_font = pygame.font.SysFont(font, size)
        text_surface = txt_font.render(text, False, color)
        self.screen.blit(text_surface, location)

    def insert_rnd_bushes(self):
        """Creates the random bushes dict"""
        for bush in range(BUSH_COUNT):
            rnd_x = random.randint(MIN_X, MAX_X - BUSH_SIZE[BUSH_WIDTH_INDEX])
            rnd_y = random.randint(MIN_Y, MAX_Y - BUSH_SIZE[BUSH_HEIGHT_INDEX])
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
        """
            Draws a horizontal line
            :param y: int
        """
        pygame.draw.line(self.screen, GREEN, (MIN_X, y), (MAX_X, y), LINE_WIDTH)

    def draw_line_vertical(self, x):
        """
            Draws a vertical line
            :param x: int
        """
        pygame.draw.line(self.screen, GREEN, (x, MIN_Y), (x, MAX_Y), LINE_WIDTH)

    def draw_mines(self, game_field):
        """
            Draws the mines on the screen
            :param game_field: GameField Object
        """
        # Get the mines location list
        mines = game_field.get_mines()
        size = (MINE_WIDTH, MINE_HEIGHT)
        for mine_location in mines:
            # Display each mine
            self.draw_object(MINE_IMG_PATH, mine_location, size)

    def draw_teleports(self, game_field):
        """
            Draws the teleports on the screen
            :param game_field: GameField Object
        """
        # Get the mines location list
        teleports = game_field.get_teleports()
        size = (TELEPORT_WIDTH, TELEPORT_HEIGHT)
        for teleport_location in teleports:
            # Display each mine
            self.draw_object(TELEPORT_IMG_PATH, teleport_location, size)

    def update_bushes(self, new_bushes_lst):
        """
            Updates the bushes list - Used to load saves
            :param new_bushes_lst: list
        """
        self.bushes = new_bushes_lst
