
from math import pi, sin, cos, sqrt

from map import get_cell
from constants import CELL_SIZE, NUM_RAYS

RAY_ANGLE = pi / 4
MAX_ITERS = 2000
TOL = 1e-3

def get_norm(vector):
    return sqrt(vector[0]**2 + vector[1]**2)

def normalize(vector, new_norm):
    norm = get_norm(vector)
    factor = new_norm/norm
    return (vector[0]*factor, vector[1]*factor)

def is_inside_map(map, i, j):
    return i >= 0 and i < len(map) and j >= 0 and j < len(map[0])

def compute_depth(map, xi, yi, dx, dy, delta_depth, max_iters=MAX_ITERS):
    depth = 0
    for _ in range(max_iters):
        (i, j) = get_cell((xi, yi), CELL_SIZE)
        if is_inside_map(map, i, j):
            if map[i][j] != 0:
                return depth
        else:
            return depth
        xi += dx
        yi += dy
        depth += delta_depth

# Returns the deep of every ray
def compute_rays(map, position, vision_angle, num_rays=NUM_RAYS, ray_angle=RAY_ANGLE):
    rays = []
    delta_angle = 0 if num_rays == 1 else ray_angle / (num_rays - 1)

    for ray in range(num_rays):
        # add this small value to avoid division by 0
        angle = vision_angle - ray_angle / 2 + delta_angle * ray + 1e-4

        (x, y) = position
        (i, j) = get_cell((x, y), CELL_SIZE)

        y_map = i * CELL_SIZE
        x_map = j * CELL_SIZE

        sin_a = sin(angle)
        cos_a = cos(angle)
        tan_a = sin_a / cos_a

        # verticals 
        delta_depth = abs(CELL_SIZE / cos_a)
        dy = delta_depth * sin_a
        dx = CELL_SIZE if cos_a > 0 else -CELL_SIZE
        xi = x_map + CELL_SIZE + TOL if cos_a > 0 else x_map - TOL
        yi = y + (xi - x) * tan_a 
        ver_depth = get_norm((xi-x, yi-y)) + compute_depth(map, xi, yi, dx, dy, delta_depth)

        # horizontals
        delta_depth = abs(CELL_SIZE / sin_a)
        dx = delta_depth * cos_a
        dy = CELL_SIZE if sin_a > 0 else -CELL_SIZE
        yi = y_map + CELL_SIZE + TOL if sin_a > 0 else y_map - TOL
        xi = x + (yi - y) / tan_a 
        hor_depth = get_norm((xi-x, yi-y)) + compute_depth(map, xi, yi, dx, dy, delta_depth)

        rays.append((angle, min(hor_depth, ver_depth)))

    return rays




