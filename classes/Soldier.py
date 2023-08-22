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
