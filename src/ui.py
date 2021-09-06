from dataclasses import dataclass

# Something like a vector3
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

@dataclass
class Button:
    top_left_pos: Point
    width: float
    height: float
