# Definitions of tetrominos
# Top left rect is 0, 0
# X -> left to right coordinate
# Y -> top to bottom coordinate
from enum import Enum


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


LINE    = [[0,  0], [1,  0], [2,  0], [3,  0]] #, Rotation]
SQUARE  = [[0,  0], [0,  1], [1,  0], [1,  1]] #, Rotation]
L_SHAPE = [[0,  0], [0,  1], [0,  2], [1,  2]] #, Rotation]
J_SHAPE = [[0,  0], [0,  1], [0,  2], [-1, 2]] #, Rotation]
T_SHAPE = [[0,  0], [1,  0], [2,  0], [1,  1]] #, Rotation]
SKEW    = [[1,  0], [2,  0], [0,  1], [1,  1]] #, Rotation]
ZKEW    = [[0,  0], [1,  0], [1,  1], [1,  2]] #, Rotation]

def rotate(tetromino, rot_center):
    # Assuming clockwise rotation
    
    pass


def move_rotate(tetromino, rot_center, direction):
    if direction == Direction.LEFT:  # left
        print("Moving left!")
        for i in range(0, 4):
            tetromino[i][0] -= 1
    elif direction == Direction.RIGHT:  # right
        print("Moving right!")
        for i in range(0, 4):
            tetromino[i][0] += 1
    elif direction == Direction.DOWN:  # down
        for i in range(0, 4):
            tetromino[i][1] += 1
    elif direction == Direction.UP:  # up - rotate
        rotate(tetromino, rot_center)
