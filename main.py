import pygame
from consts import *
from classes.Screen import Screen
from classes.GameField import GameField
from classes.Soldier import Soldier
import screens


# Create board matrix
game_field = GameField()
board = game_field.get_board()
# Create screen
screenObj = Screen()
screen = screenObj.get_screen()
# Create soldier
soldier = Soldier(game_field)


def main():
    clock = pygame.time.Clock()
    mine_screen = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Handling all the events
            if event.type == pygame.QUIT:
                running = False
            elif not mine_screen:
                key_input = pygame.key.get_pressed()
                # If enter - mine screen
                if key_input[pygame.K_RETURN]:
                    mine_screen = True
                    # Display the mine screen for x seconds
                    screens.display_mine_screen(soldier, game_field)
                    # Update the display
                    pygame.display.update()
                    # Delay the mine screen
                    pygame.time.wait(MINE_SCREEN_DELAY)
                    # Return to regular screen
                    mine_screen = False
                elif key_input[pygame.K_LEFT]:
                    soldier.move_x(right=False, game_field=game_field)
                elif key_input[pygame.K_RIGHT]:
                    soldier.move_x(right=True, game_field=game_field)
                elif key_input[pygame.K_DOWN]:
                    soldier.move_y(up=False, game_field=game_field)
                elif key_input[pygame.K_UP]:
                    soldier.move_y(up=True, game_field=game_field)

        # Display the regular screen
        screens.display_regular_screen(soldier, SOLDIER_IMG_PATH)

        # Check lose
        status = soldier.get_status()
        if status == LOSE_STATUS or status == WIN_STATUS:
            if status == LOSE_STATUS:
                # Update image to exploding
                screens.display_regular_screen(soldier, SOLDIER_EXPLODED_IMG_PATH)
                # Draw defeat message
                screenObj.draw_text(LOSE_MESSAGE, BLACK, LOSE_SIZE, LOSE_FONT, (LOSE_X, LOSE_Y))
            else:
                # Draw win message
                screenObj.draw_text(WIN_MESSAGE, BLACK, WIN_SIZE, WIN_FONT, (WIN_X, WIN_Y))

            pygame.display.update()
            # Delay to end game
            pygame.time.wait(END_GAME_DELAY)
            running = False

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
