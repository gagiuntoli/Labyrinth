import pygame
from math import pi, cos, sin

from constants import CELL_SIZE
from raycasting import add_vector, compute_rays
from map import get_cell

map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

FPS   = 24
DT    = 1.0
SPEED = 10.0
SPEED_ROT = 0.2
COLS  = len(map[0])
ROWS  = len(map)
VISION_ANGLE = pi / 4

BLACK  = (0x00, 0x00, 0x00)
ORANGE = (0xFF, 0x8C, 0x00)
WHITE  = (0xFF, 0xFF, 0xFF)
RED    = (0xFF, 0x00, 0x00)
GREEN  = (0xAA, 0xFF, 0x00)
BLUE   = (0x00, 0xFF, 0xFF)

position = (110.0, 110.0)
vision_angle   = 0.0

pygame.init()

screen = pygame.display.set_mode((COLS * CELL_SIZE, ROWS * CELL_SIZE)) 
clock = pygame.time.Clock()

pygame.display.set_caption("Labyrinth") 
exit = False

def draw_map(screen, map):
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            if val != 0:
                pygame.draw.rect(screen, RED, pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), width=1)
                pygame.draw.rect(screen, BLACK, pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE-1e-3, CELL_SIZE-1e-3), width=0)


def draw_player(screen, position, rays):
    pygame.draw.circle(screen, GREEN, position, 10)
    for ray in rays:
        (angle, depth) = ray
        vector = polar_to_cartesian(depth, angle)
        position_end = add_vector(position, vector)
        pygame.draw.line(screen, BLUE, position, position_end, 1)

def polar_to_cartesian(module, angle):
    return (module * cos(angle), module * sin(angle))

def has_collided(map, position):
    (i, j) = get_cell(position, CELL_SIZE)
    return True if map[i][j] != 0 else False

def update_position(old_position):
    keys = pygame.key.get_pressed()

    position = list(old_position)

    if keys[pygame.K_RIGHT]:
        position[0] += SPEED * DT
    if keys[pygame.K_LEFT]:
        position[0] -= SPEED * DT
    if keys[pygame.K_DOWN]:
        position[1] += SPEED * DT
    if keys[pygame.K_UP]:
        position[1] -= SPEED * DT

    if has_collided(map, position):
        return old_position
    else:
        return tuple(position)

def update_vision_angle(vision_angle):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_z]:
        vision_angle += SPEED_ROT * DT
    if keys[pygame.K_x]:
        vision_angle -= SPEED_ROT * DT

    return vision_angle % (2 * pi)
  
while not exit: 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    position = update_position(position)
    vision_angle = update_vision_angle(vision_angle)
    rays = compute_rays(map, position, vision_angle, 60, pi/6)

    screen.fill(BLACK)
    draw_map(screen, map)
    draw_player(screen, position, rays)

    pygame.display.flip()
    clock.tick(FPS)
