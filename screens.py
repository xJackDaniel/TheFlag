from classes.Screen import Screen
from consts import *

screenObj = Screen()

def display_regular_screen(soldier):
    """Creates the regular display screen"""
    # Set background color
    screenObj.set_background_color()
    # Draw random bushes
    screenObj.draw_rnd_bushes()
    # Draw the flag
    screenObj.draw_flag()
    # Draw the welcome text
    location_welcome = (WELCOME_X, WELCOME_Y)
    screenObj.draw_text(text=WELCOME_MESSAGE, location=location_welcome,
                        size=WELCOME_SIZE, font=WELCOME_FONT, color=WHITE)  # Draw the soldier
    soldier.draw_soldier()

