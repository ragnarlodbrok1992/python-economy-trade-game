import pygame

from consts import SCREEN_WIDTH, SCREEN_HEIGHT

from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_q,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

def main_game_loop():
    # Initialize the pygame
    pygame.init()

    # Create screen handler
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    GAME_RUNNING = True

    while GAME_RUNNING:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    GAME_RUNNING = False

                elif event.type == QUIT:
                    GAME_RUNNING = False

if __name__ == "__main__":
    main_game_loop()
