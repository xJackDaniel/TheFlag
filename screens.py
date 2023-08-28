from consts import *

def display_home_screen(screenObj, soldier, soldier_img, guard):
    """Displays Home screen"""
    # Set background color
    screenObj.set_background_color(GREEN)
    # Draw random bushes
    screenObj.draw_rnd_bushes()
    # Draw the flag
    screenObj.draw_flag()
    # Draw the text
    screenObj.draw_text(text=HOME_WELCOME_MESSAGE, location=(HOME_WELCOME_X, HOME_WELCOME_Y),
                        size=HOME_WELCOME_SIZE, font=HOME_WELCOME_FONT, color=WHITE)
    screenObj.draw_text(text=HOME_CREATORS_MESSAGE, location=(HOME_CREATORS_X, HOME_CREATORS_Y),
                        size=HOME_CREATORS_SIZE, font=HOME_CREATORS_FONT, color=WHITE)
    # Draw the play button
    screenObj.draw_object(img_path=HOME_PLAY_BUTTON_IMG_PATH, location=(HOME_PLAY_BUTTON_X, HOME_PLAY_BUTTON_Y),
                          size=(HOME_PLAY_BUTTON_WIDTH, HOME_PLAY_BUTTON_HEIGHT))
    # Display the frame of the rectange
    pygame.draw.rect(screenObj.get_screen(), BLACK, pygame.Rect(HOME_HELP_FRAME_X, HOME_HELP_FRAME_Y,
                                                                HOME_HELP_FRAME_WIDTH, HOME_HELP_FRAME_HEIGHT))
    # Display the "help" rectangle
    pygame.draw.rect(screenObj.get_screen(), WHITE, pygame.Rect(HOME_HELP_X, HOME_HELP_Y,
                                                                HOME_HELP_WIDTH, HOME_HELP_HEIGHT))
    # Draw the keyboard arrows
    screenObj.draw_object(img_path=HOME_KEYBOARD_ARROWS_IMG_PATH, location=(HOME_KEYBOARD_ARROWS_X, HOME_KEYBOARD_ARROWS_Y),
                          size=(HOME_KEYBOARD_ARROWS_WIDTH, HOME_KEYBOARD_ARROWS_HEIGHT))
    # Draw the explanation to the keyboard arrows
    screenObj.draw_text(text=HOME_KEYBOARD_EXPLAIN_TITLE_MESSAGE, location=(HOME_KEYBOARD_EXPLAIN_TITLE_X, HOME_KEYBOARD_EXPLAIN_TITLE_Y),
                        size=HOME_KEYBOARD_EXPLAIN_TITLE_SIZE, font=HOME_KEYBOARD_EXPLAIN_TITLE_FONT, color=BLACK)
    screenObj.draw_text(text=HOME_KEYBOARD_EXPLAIN_MESSAGE, location=(HOME_KEYBOARD_EXPLAIN_X, HOME_KEYBOARD_EXPLAIN_Y),
                        size=HOME_KEYBOARD_EXPLAIN_SIZE, font=HOME_KEYBOARD_EXPLAIN_FONT, color=BLACK)
    # Draw the soldier
    soldier.change_image(soldier_img)
    soldier.draw_soldier(screenObj)
    # Draw the guard
    guard.draw_guard(screenObj)



def display_regular_screen(screenObj, soldier, soldier_img, guard, soldier_transparent=False):
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
    soldier.change_image(soldier_img)
    soldier.draw_soldier(screenObj, soldier_transparent)
    # Draw the guard
    guard.draw_guard(screenObj)


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
    soldier.change_image(SOLDIER_MINE_SCREEN_IMG_PATH)
    soldier.draw_soldier(screenObj)
    # Draw the mines
    screenObj.draw_mines(game_field)
    # Draw the teleports
    screenObj.draw_teleports(game_field)
