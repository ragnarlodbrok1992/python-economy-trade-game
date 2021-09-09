import pygame

from pygame import Rect
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN, BLUE, BLACK
from tetromino import LINE, SQUARE, L_SHAPE, J_SHAPE, T_SHAPE, SKEW, ZKEW
from tetris_const import TETRONIMO_RECT_SIZE, TETRIS_PLAYGROUND_SIZE_X, TETRIS_PLAYGROUND_SIZE_Y, TETRIS_PLAYGROUND_DRAW_START_POINT
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
    # rect_pos_x = 10
    # rect_pos_y = 10
    # rect = Rect((rect_pos_x, rect_pos_y), (100, 100))
    test_tetromino = LINE
    tetris_playground_top_left = (TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH,
                                  TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT)
    #print(tetris_playground_top_left)
    test_start_rect = Rect(tetris_playground_top_left[0], tetris_playground_top_left[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE)
    start_tetronimo_drawing = (tetris_playground_top_left[0], tetris_playground_top_left[1])
    #test_start_rect = Rect((tetris_playground_top_left[0],
    #                        tetris_playground_top_left[1]),
    #                       (TETRONIMO_RECT_SIZE,
    #                        TETRONIMO_RECT_SIZE))

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
                    print("Rotating")
                    # print("Rect is moving!")
                    # rect = rect.move(0, -10)
                if event.key == K_s:
                    print("Moving down")
                    # print("Rect is moving!")
                    # rect = rect.move(0, 10)
                if event.key == K_a:
                    print("Moving left")
                    # print("Rect is moving!")
                    # rect = rect.move(-10, 0)
                if event.key == K_d:
                    print("Moving right")
                    # print("Rect is moving!")
                    # rect = rect.move(10, 0)

                elif event.type == QUIT:
                    GAME_RUNNING = False

        # Frame drawing

        # Erase the screen
        screen.fill(BLACK)

        # Draw tetromino
        for rect_pos in test_tetromino:
            rect_pos_draw = (rect_pos[0] * TETRONIMO_RECT_SIZE + SCREEN_WIDTH * TETRIS_PLAYGROUND_DRAW_START_POINT[0],
                             rect_pos[1] * TETRONIMO_RECT_SIZE + SCREEN_HEIGHT * TETRIS_PLAYGROUND_DRAW_START_POINT[1])
            pygame.draw.rect(screen,
                             BLUE,
                             Rect(rect_pos_draw[0], rect_pos_draw[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE))
        # I think I can keep stuff here floats
        # pygame.draw.rect(screen, RED, test_start_rect)

        # Draw playground

        # Draw border

        # Update the screen
        pygame.display.update()



if __name__ == "__main__":
    main_game_loop()
