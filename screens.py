from classes.Screen import Screen

screenObj = Screen()
screen = screenObj.get_screen()


def display_regular_screen():
    """Creates the regular display screen"""
    # Set background color
    screenObj.set_background_color()
    # Draw random bushes
    screenObj.draw_rnd_bushes()
