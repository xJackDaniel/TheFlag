import pygame
from consts import *
from classes.Screen import Screen

ScreenObj = Screen()

# TODO: Add notes to class
class Soldier:
    def __init__(self):
        self.img_path = SOLDIER_IMG_PATH
        self.x = START_SOLDIER_X
        self.y = START_SOLDIER_Y
        self.width = SOLDIER_WIDTH
        self.height = SOLDIER_HEIGHT

    def draw_soldier(self):
        """Draws the soldier to the screen"""
        location = (self.x, self.y)
        size = (self.width, self.height)
        ScreenObj.draw_object(self.img_path, location, size)

    def move_x(self, right: bool):
        """updating soldier position - only right and left """
        if right:
            if not (self.x+STEP_SIZE > WINDOW_WIDTH-SOLDIER_WIDTH):
                self.x += STEP_SIZE
        else:
            if not self.x == MIN_X:
                self.x -= STEP_SIZE


    def move_y(self, up: bool):
        """updating soldier position - only up and down """
        if up:
            if not self.y == MIN_Y:
                self.y -= STEP_SIZE
        else:
            if not (self.y + STEP_SIZE > WINDOW_HEIGHT - SOLDIER_HEIGHT):
                self.y += STEP_SIZE
