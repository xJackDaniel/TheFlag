import pygame
from consts import *
from classes.Screen import Screen
from classes.GameField import GameField


ScreenObj = Screen()
game_field = GameField()

# TODO: Add notes to class
class Soldier:
    def __init__(self):
        self.img_path = SOLDIER_IMG_PATH
        self.x = START_SOLDIER_X
        self.y = START_SOLDIER_Y
        self.width = SOLDIER_WIDTH
        self.height = SOLDIER_HEIGHT
        # Insert the soldier to board
        game_field.update_soldier_location(self)


    def get_x(self):
        """Returns the x of the soldier"""
        return self.x

    def get_y(self):
        """Returns the y of the soldier"""
        return self.y

    def change_soldier_mine_screen(self):
        """"""
        self.img_path = SOLDIER_MINE_SCREEN_IMG_PATH

    def draw_soldier(self):
        """Draws the soldier to the screen"""
        location = (self.x, self.y)
        size = (self.width, self.height)
        ScreenObj.draw_object(self.img_path, location, size)

    def move_x(self, right: bool):
        """updating soldier position - only right and left """
        moved = False
        if right:
            # Make sure that the soldier is not crossing the screen size
            if not (self.x+STEP_SIZE > WINDOW_WIDTH-SOLDIER_WIDTH):
                self.x += STEP_SIZE
                moved = True
        else:
            if not self.x == MIN_X:
                self.x -= STEP_SIZE
                moved = True
        if moved:
            game_field.update_soldier_location(self)

    def move_y(self, up: bool):
        """updating soldier position - only up and down """
        moved = False
        if up:
            if not self.y == MIN_Y:
                self.y -= STEP_SIZE
                moved = True
        else:
            # Make sure that the soldier is not crossing the screen size
            if not (self.y + STEP_SIZE > WINDOW_HEIGHT - SOLDIER_HEIGHT):
                self.y += STEP_SIZE
                moved = True
        if moved:
            game_field.update_soldier_location(self)
