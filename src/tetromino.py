# Definitions of tetrominos
# Top left rect is 0, 0
# X -> left to right coordinate
# Y -> top to bottom coordinate

LINE    = [(0,  0), (1,  0), (2,  0), (3,  0)]
SQUARE  = [(0,  0), (0,  1), (1,  0), (1,  1)]
L_SHAPE = [(0,  0), (0,  1), (0,  2), (1,  2)]
J_SHAPE = [(0,  0), (0,  1), (0,  2), (-1, 2)]
T_SHAPE = [(0,  0), (1,  0), (2,  0), (1,  1)]
SKEW    = [(1,  0), (2,  0), (0,  1), (1,  1)]
ZKEW    = [(0,  0), (1,  0), (1,  1), (1,  2)]


def rotate(tetromino, rot_center, direction):
    pass
