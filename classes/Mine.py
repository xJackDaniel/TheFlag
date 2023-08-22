from consts import *
import random


# TODO: Add notes to class
class Mine:
    def __init__(self):
        self.x = random.randint(MIN_X, MAX_X)
        self.y = random.randint(MIN_Y, MAX_Y)

    def draw_mine(self, screen):
        """The function draws a mine on the screen"""
        pass
