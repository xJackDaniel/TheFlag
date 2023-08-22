import pygame
from consts import *
from classes.Screen import Screen
from classes.GameField import GameField
import screens

# Create screen
screenObj = Screen()
screen = screenObj.get_screen()
# Create board matrix
game_field = GameField()
board = game_field.get_board()


def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Handling all the events
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    # Display the regular screen
    screens.display_regualr_screen()

    pygame.quit()


if __name__ == "__main__":
    main()
