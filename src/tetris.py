import pygame

from pygame import Rect

from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN, BLUE, BLACK, YELLOW
from tetromino import LINE, SQUARE, L_SHAPE, J_SHAPE, T_SHAPE, SKEW, ZKEW, move_rotate, Direction
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

def check_valid_coords(tetromino):
    valid_x = TETRIS_PLAYGROUND_SIZE_X - 1
    valid_y = TETRIS_PLAYGROUND_SIZE_Y - 1
    for r in tetromino:
        if r[0] < 0 or r[0] > valid_x:
            return False
        if r[1] < 0 or r[1] > valid_y:
            return False
    return True

def draw_tetromino(screen, tetromino):
    for rect_pos in tetromino:
        rect_pos_draw = (rect_pos[0] * TETRONIMO_RECT_SIZE + SCREEN_WIDTH * TETRIS_PLAYGROUND_DRAW_START_POINT[0],
                         rect_pos[1] * TETRONIMO_RECT_SIZE + SCREEN_HEIGHT * TETRIS_PLAYGROUND_DRAW_START_POINT[1])
        pygame.draw.rect(screen,
                         BLUE,
                         Rect(rect_pos_draw[0], rect_pos_draw[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE))

def main_game_loop():
    # Initialize the pygame
    pygame.init()

    # Init some variables
    test_tetromino = LINE
    tetris_playground_top_left = (TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH,
                                  TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT)
    test_start_rect = Rect(tetris_playground_top_left[0], tetris_playground_top_left[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE)

    # Game border values
    top_left = [TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH,
                TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT]
    bottom_left = [TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH,
                   TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT + TETRONIMO_RECT_SIZE * TETRIS_PLAYGROUND_SIZE_Y]
    bottom_right = [TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH + TETRONIMO_RECT_SIZE * TETRIS_PLAYGROUND_SIZE_X,
                    TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT + TETRONIMO_RECT_SIZE * TETRIS_PLAYGROUND_SIZE_Y]
    top_right = [TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH + TETRONIMO_RECT_SIZE * TETRIS_PLAYGROUND_SIZE_X,
                 TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT]
    playground_borders = [top_left, bottom_left, bottom_right, top_right]

    print("DEBUG! playground values")
    print(top_left)
    print(bottom_left)
    print(bottom_right)
    print(top_right)

    # Create screen handler
    print("Display values: {} by {} pixels".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    # TODO: prepare proper OPENGL display context
    flags = 0 # pygame.OPENGL # | pygame.FULLSCREEN
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)

    # Main game loop
    GAME_RUNNING = True
    frame_counter = 0

    while GAME_RUNNING:
        # Frame counter
        frame_counter += 1

        # Event loop
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    GAME_RUNNING = False

                if event.key == K_w:
                    print("Rotating")
                    move_rotate(test_tetromino, (0, 0), Direction.UP)
                if event.key == K_s:
                    print("Moving down")
                    move_rotate(test_tetromino, (0, 0), Direction.DOWN)
                if event.key == K_a:
                    print("Moving left")
                    move_rotate(test_tetromino, (0, 0), Direction.LEFT)
                if event.key == K_d:
                    print("Moving right")
                    move_rotate(test_tetromino, (0, 0), Direction.RIGHT)

                elif event.type == QUIT:
                    GAME_RUNNING = False

        # Frame-by-frame logic
        valid_coords = check_valid_coords(test_tetromino)

        # Frame drawing

        # Erase the screen
        screen.fill(BLACK)

        # Draw tetromino
        draw_tetromino(screen, test_tetromino)

        # Draw playground
        pygame.draw.lines(screen, YELLOW, True, playground_borders, width=2)

        # Draw UI

        # Draw debug strings
        debug_strings_spacing = 11
        frame_counter_font = pygame.font.SysFont("monospace", debug_strings_spacing)
        frame_counter_label = frame_counter_font.render("Frame counter: " + str(frame_counter), 1, WHITE)
        valid_coords_font = pygame.font.SysFont("monospace", debug_strings_spacing)
        valid_coords_label = valid_coords_font.render("Valid coords: " + str(valid_coords), 1, WHITE)
        screen.blit(frame_counter_label, (5, 5 + debug_strings_spacing * 0))
        screen.blit(valid_coords_label, (5, 5 + debug_strings_spacing * 1))

        # Update the screen
        pygame.display.update()



if __name__ == "__main__":
    main_game_loop()
