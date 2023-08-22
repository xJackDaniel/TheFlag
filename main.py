import pygame
from consts import *
from classes.Screen import Screen

screenObj = Screen()
screen = screenObj.get_screen()


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

    pygame.quit()


if __name__ == "__main__":
    main()

