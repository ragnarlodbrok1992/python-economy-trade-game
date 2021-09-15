import pygame
import random

from pygame import Rect

from enum import Enum
from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN, BLUE, BLACK, YELLOW
from tetromino import get_tetromino, move_rotate, Direction, Rotation
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

def update_playground_when_tetronimo_gets_stuck(tetronimo, playground):
    pass
    # Do something nice here TODO
    # Playground should be updated with every move
    # There should be distinguishibility (is that even a word)
    # from active tetronimo that is moving
    # to all that are stuck and cannot be moved
    # maybe different values?

def check_if_tetronimo_can_move_in_playground(tetronimo, playground):
    pass
    # This might obsolete check_where_can_move
    # Or we can use this function here

def check_valid_coords(tetromino):
    valid_x = TETRIS_PLAYGROUND_SIZE_X - 1
    valid_y = TETRIS_PLAYGROUND_SIZE_Y - 1
    for r in tetromino:
        if r[0] < 0 or r[0] > valid_x:
            return False
        if r[1] < 0 or r[1] > valid_y:
            return False
    return True

def check_where_can_move(playground, tetromino):
    # 0 - can move left
    # 1 - can move down
    # 2 - can move right
    valid_x = TETRIS_PLAYGROUND_SIZE_X - 1
    valid_y = TETRIS_PLAYGROUND_SIZE_Y - 1
    movable = [True, True, True]
    # Checking bounds
    for r in tetromino:
        if r[0] < 1:
            movable[0] = False
        if r[0] > valid_x - 1:
            movable[2] = False
        if r[1] > valid_y - 1:
            movable[1] = False

    # Checking playground
    for r in tetromino:
        print("DEBUG! checking r in tetromino")
        if r[1] < valid_y:
            print("DEBUG! We are here, we will check")
            print("DEBUG! r[0] and r[1]: {} {}".format(r[0], r[1]))
            print("DEBUG! playground[r[0]][r[1] + 1]: {}".format(playground[r[0]][r[1] + 1]))
            if playground[r[0]][r[1] + 1] == 1:
                print("DEBUG! MADAFAKIN STUCK!")
                movable[1] = False
    return movable

def is_tetromino_going_to_be_stuck(playground, tetromino):
    for rect in tetromino:
        rect_check = (rect[0], rect[1] + 1)
        if rect_check[1] > 20 - 1:
            return True
        elif playground[rect_check[1]][rect_check[0]] == 1:
            return True
    return False

def stuck_tetromino_and_prepare_new(playground, tetromino):
    # Stucking tetromino
    for rect in tetromino:
        playground[rect[1]][rect[0]] = 1
    tetromino = get_tetromino()
    return tetromino

def draw_tetromino(screen, tetromino):
    for rect_pos in tetromino:
        lines = []
        rect_pos_draw = (rect_pos[0] * TETRONIMO_RECT_SIZE + SCREEN_WIDTH * TETRIS_PLAYGROUND_DRAW_START_POINT[0],
                         rect_pos[1] * TETRONIMO_RECT_SIZE + SCREEN_HEIGHT * TETRIS_PLAYGROUND_DRAW_START_POINT[1])
        pygame.draw.rect(screen,
                         BLUE,
                         Rect(rect_pos_draw[0], rect_pos_draw[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE))
        lines.append(rect_pos_draw)
        lines.append((rect_pos_draw[0],
                      rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
        lines.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                      rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
        lines.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                      rect_pos_draw[1]))

        pygame.draw.lines(screen, GREEN, True, lines, width=1)

def draw_debug_playground(screen, playground):
    for x in range(0, TETRIS_PLAYGROUND_SIZE_X):
        for y in range(0, TETRIS_PLAYGROUND_SIZE_Y):
            rect_pos_draw = (x * TETRONIMO_RECT_SIZE + SCREEN_WIDTH * TETRIS_PLAYGROUND_DRAW_START_POINT[0],
                             y * TETRONIMO_RECT_SIZE + SCREEN_HEIGHT * TETRIS_PLAYGROUND_DRAW_START_POINT[1])
            lines_line_1 = []
            lines_line_2 = []
            lines_line_1.append(rect_pos_draw)
            lines_line_2.append((rect_pos_draw[0],
                          rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
            lines_line_1.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                          rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
            lines_line_2.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                          rect_pos_draw[1]))

            # For now, DEBUG
            if playground[y][x] == 0:
                pygame.draw.line(screen, GREEN, lines_line_1[0], lines_line_1[1], width=1)
                pygame.draw.line(screen, GREEN, lines_line_2[0], lines_line_2[1], width=1)
            elif playground[y][x] == 1:
                pygame.draw.line(screen, RED, lines_line_1[0], lines_line_1[1], width=1)
                pygame.draw.line(screen, RED, lines_line_2[0], lines_line_2[1], width=1)

            '''
    # TODO fix this function
    for idy, row in enumerate(playground):
        print("Debug! row: {}".format(row))
        break
        for idx, field in enumerate(row):
            rect_pos_draw = (idx * TETRONIMO_RECT_SIZE + SCREEN_WIDTH * TETRIS_PLAYGROUND_DRAW_START_POINT[0],
                             idy * TETRONIMO_RECT_SIZE + SCREEN_HEIGHT * TETRIS_PLAYGROUND_DRAW_START_POINT[1])
            lines_line_1 = []
            lines_line_2 = []
            lines_line_1.append(rect_pos_draw)
            lines_line_2.append((rect_pos_draw[0],
                          rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
            lines_line_1.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                          rect_pos_draw[1] + TETRONIMO_RECT_SIZE))
            lines_line_2.append((rect_pos_draw[0] + TETRONIMO_RECT_SIZE,
                          rect_pos_draw[1]))
            # print("Debug! field: {}".format(field))
            if field == 0:
                pygame.draw.line(screen, GREEN, lines_line_1[0], lines_line_1[1], width=1)
                pygame.draw.line(screen, GREEN, lines_line_2[0], lines_line_2[1], width=1)
            elif field == 1:
                pygame.draw.line(screen, RED, lines_line_1[0], lines_line_1[1], width=1)
                pygame.draw.line(screen, RED, lines_line_2[0], lines_line_2[1], width=1)
            '''

class Difficulty(Enum):
    SUPER_EASY = 300
    EASY = 240
    MEDIUM = 180
    SOMEWHAT_HARD = 120
    HARD = 60
    UBER_HARD = 30

def main_game_loop():
    # Initialize the pygame
    pygame.init()

    # Init some variables
    # TODO make sure if rotation is correct (prepare right rotated tetrominos at start)
    test_tetromino = get_tetromino()
    tetris_playground_top_left = (TETRIS_PLAYGROUND_DRAW_START_POINT[0] * SCREEN_WIDTH,
                                  TETRIS_PLAYGROUND_DRAW_START_POINT[1] * SCREEN_HEIGHT)
    test_start_rect = Rect(tetris_playground_top_left[0], tetris_playground_top_left[1], TETRONIMO_RECT_SIZE, TETRONIMO_RECT_SIZE)
    test_tetromino_rotation = Rotation.RIGHT

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

    # Playground backend - for storing rects from tetronimos
    playground = [[0 for x in range(0, TETRIS_PLAYGROUND_SIZE_X)] for x in range(0, TETRIS_PLAYGROUND_SIZE_Y)]

    # DEBUG!
    # playground[7][7] = 1  # This puts 1 in whole column...

    # Create screen handler
    print("Display values: {} by {} pixels".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    # TODO: prepare proper OPENGL display context
    # flags = 0 # pygame.OPENGL # | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    # flags = pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE
    flags = pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)

    # Main game loop
    GAME_RUNNING = True
    GAME_CLOCK = pygame.time.Clock()
    FPS_LIMIT = 60

    current_difficulty = Difficulty.HARD

    frame_counter = 0

    DEBUG = True

    while GAME_RUNNING:
        # Frame counter
        frame_counter += 1
        GAME_CLOCK.tick(FPS_LIMIT)

        # Frame-by-frame logic
        valid_coords = check_valid_coords(test_tetromino)
        movable = check_where_can_move(playground, test_tetromino)
        is_tetromino_almost_stuck = is_tetromino_going_to_be_stuck(playground, test_tetromino)

        # Event loop
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    GAME_RUNNING = False

                if event.key == K_w:
                    move_rotate(test_tetromino, (0, 0), Direction.UP)
                if event.key == K_s and movable[1]:
                    move_rotate(test_tetromino, (0, 0), Direction.DOWN)
                if event.key == K_a and movable[0]:
                    move_rotate(test_tetromino, (0, 0), Direction.LEFT)
                if event.key == K_d and movable[2]:
                    move_rotate(test_tetromino, (0, 0), Direction.RIGHT)

                elif event.type == QUIT:
                    GAME_RUNNING = False

        # Moving tetromino on it's own
        if frame_counter % current_difficulty.value == 0:
            print("Difficulty is " + str(current_difficulty))
            # FIXME here is a bug that moves tetromino because it is wrongly checkec if it can move
            if movable[1]:
                print("Moving tetromino down!")
                move_rotate(test_tetromino, (0, 0), Direction.DOWN)
            if is_tetromino_almost_stuck:
                print("Stucking tetromino!")
                test_tetromino = stuck_tetromino_and_prepare_new(playground, test_tetromino)

            # TODO apply changing difficulty, right now set to HARD

        # Frame drawing
        # Erase the screen
        screen.fill(BLACK)

        # Debug draws
        if DEBUG:
            draw_debug_playground(screen, playground)

        # Draw tetromino
        draw_tetromino(screen, test_tetromino)

        # Draw playground
        pygame.draw.lines(screen, YELLOW, True, playground_borders, width=2)

        # Draw UI

        # Draw debug strings
        debug_strings_spacing = 11
        debug_font = pygame.font.SysFont("monospace", debug_strings_spacing)
        frame_counter_label = debug_font.render("Frame counter: " + str(frame_counter), 1, WHITE)
        valid_coords_label = debug_font.render("Valid coords: " + str(valid_coords), 1, WHITE)
        movable_label = debug_font.render("Is movable: " + str(movable), 1, WHITE)
        tetromino_almost_stuck = debug_font.render("Tetromino almost stuck: " + str(is_tetromino_almost_stuck), 1, WHITE)
        game_clock_label = debug_font.render("Game clock FPS: " + str(GAME_CLOCK.get_fps()), 1, WHITE)
        difficulty_label = debug_font.render("Difficulty: " + str(current_difficulty), 1, WHITE)
        screen.blit(frame_counter_label, (5, 5 + debug_strings_spacing * 0))
        screen.blit(valid_coords_label, (5, 5 + debug_strings_spacing * 1))
        screen.blit(movable_label, (5, 5 + debug_strings_spacing * 2))
        screen.blit(game_clock_label, (5, 5 + debug_strings_spacing * 3))
        screen.blit(difficulty_label, (5, 5 + debug_strings_spacing * 4))
        screen.blit(tetromino_almost_stuck, (5, 5 + debug_strings_spacing * 5))

        # Update the screen
        # TODO: lets try to run it with opengl
        pygame.display.update()
        # pygame.display.flip()



if __name__ == "__main__":
    main_game_loop()
