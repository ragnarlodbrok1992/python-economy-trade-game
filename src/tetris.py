import pygame

from pygame import Rect

from consts import SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN, BLUE, BLACK, YELLOW
from tetromino import LINE, SQUARE, L_SHAPE, J_SHAPE, T_SHAPE, SKEW, ZKEW, move_rotate, Direction, Rotation
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

def check_where_can_move(tetromino):
    # 0 - can move left
    # 1 - can move down
    # 2 - can move right
    valid_x = TETRIS_PLAYGROUND_SIZE_X - 1
    valid_y = TETRIS_PLAYGROUND_SIZE_Y - 1
    movable = [True, True, True]
    for r in tetromino:
        if r[0] < 1:
            movable[0] = False
        if r[0] > valid_x - 1:
            movable[2] = False
        if r[1] > valid_y - 1:
            movable[1] = False
    return movable

def is_tetronimo_stuck(playground, tetronimo):
    pass

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

def main_game_loop():
    # Initialize the pygame
    pygame.init()

    # Init some variables
    test_tetromino = LINE
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
    playground = [[0] * TETRIS_PLAYGROUND_SIZE_X]  * TETRIS_PLAYGROUND_SIZE_Y

    # Create screen handler
    print("Display values: {} by {} pixels".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    # TODO: prepare proper OPENGL display context
    flags = 0 # pygame.OPENGL # | pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE
    # flags = pygame.FULLSCREEN | pygame.OPENGL | pygame.DOUBLEBUF | pygame.HWSURFACE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags, vsync=1)

    # Main game loop
    GAME_RUNNING = True
    GAME_CLOCK = pygame.time.Clock()
    FPS_LIMIT = 60

    frame_counter = 0

    while GAME_RUNNING:
        # Frame counter
        frame_counter += 1
        GAME_CLOCK.tick(FPS_LIMIT)

        # Frame-by-frame logic
        valid_coords = check_valid_coords(test_tetromino)
        movable = check_where_can_move(test_tetromino)

        # Event loop
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_q:
                    GAME_RUNNING = False

                if event.key == K_w:
                    print("Rotating")
                    move_rotate(test_tetromino, (0, 0), Direction.UP)
                if event.key == K_s and movable[1]:
                    print("Moving down")
                    move_rotate(test_tetromino, (0, 0), Direction.DOWN)
                if event.key == K_a and movable[0]:
                    print("Moving left")
                    move_rotate(test_tetromino, (0, 0), Direction.LEFT)
                if event.key == K_d and movable[2]:
                    print("Moving right")
                    move_rotate(test_tetromino, (0, 0), Direction.RIGHT)

                elif event.type == QUIT:
                    GAME_RUNNING = False

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
        debug_font = pygame.font.SysFont("monospace", debug_strings_spacing)
        frame_counter_label = debug_font.render("Frame counter: " + str(frame_counter), 1, WHITE)
        valid_coords_label = debug_font.render("Valid coords: " + str(valid_coords), 1, WHITE)
        movable_label = debug_font.render("Is movable: " + str(movable), 1, WHITE)
        game_clock_label = debug_font.render("Game clock FPS: " + str(GAME_CLOCK.get_fps()), 1, WHITE)
        screen.blit(frame_counter_label, (5, 5 + debug_strings_spacing * 0))
        screen.blit(valid_coords_label, (5, 5 + debug_strings_spacing * 1))
        screen.blit(movable_label, (5, 5 + debug_strings_spacing * 2))
        screen.blit(game_clock_label, (5, 5 + debug_strings_spacing * 3))

        # Update the screen
        # TODO: lets try to run it with opengl
        pygame.display.update()
        # pygame.display.flip()



if __name__ == "__main__":
    main_game_loop()
