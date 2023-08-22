from classes.Screen import Screen

screenObj = Screen()

def display_regular_screen(soldier):
    """Creates the regular display screen"""
    # Set background color
    screenObj.set_background_color()
    # Draw random bushes
    screenObj.draw_rnd_bushes()
    # Draw the flag
    screenObj.draw_flag()
    # Draw the soldier
    soldier.draw_soldier()

