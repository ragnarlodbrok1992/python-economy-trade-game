import pygame

from pygame import Rect
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN, BLUE, BLACK
from ui import Button

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

    # Init some variables
    rect_pos_x = 10
    rect_pos_y = 10
    rect = Rect((rect_pos_x, rect_pos_y), (100, 100))

    # Create screen handler
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    GAME_RUNNING = True

    while GAME_RUNNING:
        # Event loop
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    GAME_RUNNING = False

                if event.key == K_w:
                    print("Rect is moving!")
                    rect = rect.move(0, -10)
                if event.key == K_s:
                    print("Rect is moving!")
                    rect = rect.move(0, 10)
                if event.key == K_a:
                    print("Rect is moving!")
                    rect = rect.move(-10, 0)
                if event.key == K_d:
                    print("Rect is moving!")
                    rect = rect.move(10, 0)

                elif event.type == QUIT:
                    GAME_RUNNING = False

        # Frame drawing

        # Erase the screen
        screen.fill(WHITE)

        # Draw something
        pygame.draw.rect(screen, RED, rect)

        # Update the screen
        pygame.display.update()



if __name__ == "__main__":
    main_game_loop()
