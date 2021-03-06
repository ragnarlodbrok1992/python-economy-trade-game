# Definitions of tetrominos
# Top left rect is 0, 0
# X -> left to right coordinate
# Y -> top to bottom coordinate
import random

from enum import Enum
from tetris_const import TETRIS_PLAYGROUND_SIZE_X


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    DOWN = 2
    UP = 3

class Rotation(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

START_X = int(TETRIS_PLAYGROUND_SIZE_X / 2) - 2


def rotate(tetromino, rotation):
    # Assuming clockwise rotation
    if rotation == Rotation.UP:
        pass
    elif rotation == Rotation.RIGHT:
        pass
    elif rotation == Rotation.DOWN:
        pass
    elif rotation == Rotation.LEFT:
        pass

def get_tetromino():
    LINE    = [[START_X + 0, 0], [START_X + 1, 0], [START_X + 2, 0], [START_X + 3, 0]] #, Rotation]
    SQUARE  = [[START_X + 0, 0], [START_X + 0, 1], [START_X + 1, 0], [START_X + 1, 1]] #, Rotation]
    L_SHAPE = [[START_X + 0, 0], [START_X + 0, 1], [START_X + 0, 2], [START_X + 1, 2]] #, Rotation]
    J_SHAPE = [[START_X + 0, 0], [START_X + 0, 1], [START_X + 0, 2], [START_X - 1, 2]] #, Rotation]
    T_SHAPE = [[START_X + 0, 0], [START_X + 1, 0], [START_X + 2, 0], [START_X + 1, 1]] #, Rotation]
    SKEW    = [[START_X + 1, 0], [START_X + 2, 0], [START_X + 0, 1], [START_X + 1, 1]] #, Rotation]
    ZKEW    = [[START_X + 0, 0], [START_X + 1, 0], [START_X + 1, 1], [START_X + 1, 2]] #, Rotation]
    return random.choice([LINE, SQUARE, L_SHAPE, J_SHAPE, T_SHAPE, SKEW, ZKEW])

def move_rotate(tetromino, rot_center, direction):
    if direction == Direction.LEFT:  # left
        for i in range(0, 4):
            tetromino[i][0] -= 1
    elif direction == Direction.RIGHT:  # right
        for i in range(0, 4):
            tetromino[i][0] += 1
    elif direction == Direction.DOWN:  # down
        for i in range(0, 4):
            tetromino[i][1] += 1
    elif direction == Direction.UP:  # up - rotate
        rotate(tetromino, rot_center)

