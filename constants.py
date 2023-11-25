from math import pi, tan

CELL_SIZE = 100
NUM_RAYS = 1000

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

COLS  = len(map[0])
ROWS  = len(map)

FPS   = 24
DT    = 1.0
SPEED = 10.0
SPEED_ROT = 0.1
VISION_ANGLE = pi / 4
WALL_HEIGHT = 20.0
PLAYER_SIZE = 1.2

SCREEN_WIDTH = COLS * CELL_SIZE
SCREEN_HEIGHT = ROWS * CELL_SIZE
DIST_TO_SCREEN = SCREEN_WIDTH / 2 / tan(VISION_ANGLE / 2)

BLACK  = (0x00, 0x00, 0x00)
ORANGE = (0xFF, 0x8C, 0x00)
WHITE  = (0xFF, 0xFF, 0xFF)
RED    = (0xFF, 0x00, 0x00)
GREEN  = (0xAA, 0xFF, 0x00)
BLUE   = (0x00, 0xFF, 0xFF)
