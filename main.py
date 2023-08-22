import pygame
from consts import *
from classes.Screen import Screen
from classes.GameField import GameField
from classes.Soldier import Soldier
import screens

# Create screen
screenObj = Screen()
screen = screenObj.get_screen()
# Create board matrix
game_field = GameField()
board = game_field.get_board()
# Create soldier
soldier = Soldier()


def main():
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            # Handling all the events
            if event.type == pygame.QUIT:
                running = False

        # Display the regular screen
        screens.display_regular_screen(soldier)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
