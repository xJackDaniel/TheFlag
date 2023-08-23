from consts import *


def display_regular_screen(screenObj, soldier, img):
    """Creates the regular display screen"""
    # Set background color
    screenObj.set_background_color(GREEN)
    # Draw random bushes
    screenObj.draw_rnd_bushes()
    # Draw the flag
    screenObj.draw_flag()
    # Draw the welcome text
    location_welcome = (WELCOME_X, WELCOME_Y)
    screenObj.draw_text(text=WELCOME_MESSAGE, location=location_welcome,
                        size=WELCOME_SIZE, font=WELCOME_FONT, color=WHITE)
    # Draw the soldier
    soldier.change_soldier_image(img)
    soldier.draw_soldier(screenObj)


def display_mine_screen(screenObj, soldier, game_field):
    """crate mine showing screen on
     top of the original screen"""
    # change the screen color to white
    screenObj.set_background_color(BLACK)
    # Draw lines
    for col in range(COLS_COUNT):
        screenObj.draw_line_vertical((col + 1) * SQUARE_SIZE)
    for row in range(ROWS_COUNT):
        screenObj.draw_line_horizontal((row + 1) * SQUARE_SIZE)
    # Draw the soldier
    soldier.change_soldier_image(SOLDIER_MINE_SCREEN_IMG_PATH)
    soldier.draw_soldier(screenObj)
    # Draw the mines
    screenObj.draw_mines(game_field)
