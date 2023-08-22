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
            else:
                key_input = pygame.key.get_pressed()
                if key_input[pygame.K_LEFT]:
                    soldier.move_x(right=False)
                elif key_input[pygame.K_RIGHT]:
                    soldier.move_x(right=True)
                elif key_input[pygame.K_DOWN]:
                    soldier.move_y(up=False)
                elif key_input[pygame.K_UP]:
                    soldier.move_y(up=True)

        # Display the regular screen
        screens.display_regular_screen(soldier)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
