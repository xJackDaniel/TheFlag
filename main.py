import pygame
from consts import *
from classes.Screen import Screen
from classes.GameField import GameField
from classes.Guard import Guard
from classes.Soldier import Soldier
import modules.Database as db
import modules.Helpers as helpers
import screens
import time

# Create board matrix
game_field = GameField()
board = game_field.get_board()
# Create screen
screenObj = Screen()
screen = screenObj.get_screen()
# Create soldier
soldier = Soldier(game_field)
# Create guard
guard = Guard(game_field)


def main():
    clock = pygame.time.Clock()
    mine_screen = False
    save_key_pressed = False

    running = True
    while running:
        clock.tick(FPS)

        # Get soldier status
        status = soldier.get_status()

        for event in pygame.event.get():
            # Handling all the events
            if event.type == pygame.QUIT:
                running = False
            elif soldier.get_status() != NOT_RUNNING_STATUS:
                if not mine_screen:
                    if event.type == pygame.KEYDOWN:
                        key_input = pygame.key.get_pressed()
                        # Check if one of the save keys pressed
                        if event.key in SAVE_KEYS.keys():
                            t = time.time()
                            save_key_pressed = True
                        # If enter - mine screen
                        elif key_input[pygame.K_RETURN]:
                            mine_screen = True
                            # Display the mine screen for x seconds
                            screens.display_mine_screen(screenObj, soldier, game_field)
                            # Update the display
                            pygame.display.update()
                            # Delay the mine screen
                            pygame.time.wait(MINE_SCREEN_DELAY)
                            # Return to regular screen
                            mine_screen = False
                    elif event.type == pygame.KEYUP and save_key_pressed:
                        t = time.time() - t;
                        t = str(t);
                        t = t[:5];
                        t = float(t)
                        key = SAVE_KEYS.get(event.key)
                        if t <= CHECK_DELAY:
                            # Save the game
                            db.write_to_csv(key, game_field.get_board(), screenObj.get_bushes(),
                                            game_field.get_mines(), soldier, game_field.get_teleports(), guard)
                            # Show a message
                            screenObj.draw_text(SAVED_MESSAGE.format(number=key), BLACK, SAVED_SIZE,
                                                SAVED_FONT,
                                                (SAVED_X, SAVED_Y))
                        else:
                            # Load the game
                            data, response = db.read_csv(key)
                            # Check if there is a saved game with this key - show a message
                            if response == KEY_ERROR:
                                screenObj.draw_text(NOT_FOUND_MESSAGE.format(number=key), BLACK, NOT_FOUND_SIZE,
                                                    NOT_FOUND_FONT,
                                                    (NOT_FOUND_X, NOT_FOUND_Y))
                            else:
                                # Load save
                                game_field.load_save(data, screenObj, soldier, guard)
                                screenObj.draw_text(LOADING_SAVE_MESSAGE.format(number=key), BLACK, LOADING_SAVE_SIZE,
                                                    LOADING_SAVE_FONT,
                                                    (LOADING_SAVE_X, LOADING_SAVE_Y))
                        pygame.display.update()
                        # Delay the message
                        pygame.time.wait(MESSAGE_DELAY)

                        save_key_pressed = False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos
                    # Check if play button pressed
                    if helpers.mouse_in_object(mouse_pos=pos, obj_x=HOME_PLAY_BUTTON_X, obj_y=HOME_PLAY_BUTTON_Y,
                                               obj_width=HOME_PLAY_BUTTON_WIDTH, obj_height=HOME_PLAY_BUTTON_HEIGHT):
                        # Start playing
                        soldier.set_status(RUNNING_STATUS)

        # Handle movement
        if status != NOT_RUNNING_STATUS:
            key_input = pygame.key.get_pressed()
            if key_input[pygame.K_LEFT]:
                soldier.move_x(right=False, game_field=game_field, screenObj=screenObj)
            elif key_input[pygame.K_RIGHT]:
                soldier.move_x(right=True, game_field=game_field, screenObj=screenObj)
            elif key_input[pygame.K_DOWN]:
                soldier.move_y(up=False, game_field=game_field, screenObj=screenObj)
            elif key_input[pygame.K_UP]:
                soldier.move_y(up=True, game_field=game_field, screenObj=screenObj)

            # Move the guard
            guard.move_guard(soldier)
            # Display the regular screen
            screens.display_regular_screen(screenObj, soldier, SOLDIER_IMG_PATH, guard)

            # Check lose
            guard_lose = False
            if guard.get_status() == LOSE_STATUS:
                guard_lose = True
                status = LOSE_STATUS
            if status == LOSE_STATUS or status == WIN_STATUS:
                if status == LOSE_STATUS:
                    # Update image to exploding
                    img = SOLDIER_EXPLODED_IMG_PATH
                    if guard_lose:
                        img = SOLDIER_GUARD_LOSE_IMG_PATH
                    screens.display_regular_screen(screenObj, soldier, img, guard)
                    # Draw defeat message
                    screenObj.draw_text(LOSE_MESSAGE, BLACK, LOSE_SIZE, LOSE_FONT, (LOSE_X, LOSE_Y))
                else:
                    # Update image to exploding
                    screens.display_regular_screen(screenObj, soldier, SOLDIER_WIN_IMG_PATH, guard)
                    # Draw the win img
                    screenObj.draw_object(WIN_IMG_PATH, (WIN_IMG_X, WIN_IMG_Y), (WIN_IMG_WIDTH, WIN_IMG_HEIGHT))
                    # Draw win message
                    screenObj.draw_text(WIN_MESSAGE, BLACK, WIN_SIZE, WIN_FONT, (WIN_X, WIN_Y))

                pygame.display.update()
                # Delay to end game
                pygame.time.wait(END_GAME_DELAY)
                running = False
            elif status == TELEPORT_STATUS:
                # Blink the soldier
                soldier.blink(screens, screenObj, guard)
        else:
            # Display home screen
            screens.display_home_screen(screenObj, soldier, SOLDIER_IMG_PATH, guard)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
