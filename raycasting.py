
from math import pi, sin, cos, sqrt

from map import get_cell
from constants import CELL_SIZE

NUM_RAYS = 20
RAY_ANGLE = pi / 4
MAX_ITERS = 2000

def add_vector(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

def get_norm(vector):
    return sqrt(vector[0]**2 + vector[1]**2)

def normalize(vector, new_norm):
    norm = get_norm(vector)
    factor = new_norm/norm
    return (vector[0]*factor, vector[1]*factor)

def add_vectors(v1, v2):
    return (v1[0]+v2[0], v1[1]+v2[1])

# Returns the deep of every ray
def compute_rays(map, position, vision_angle, num_rays=NUM_RAYS, ray_angle=RAY_ANGLE):
    rays = []
    delta_angle = 0 if num_rays == 1 else ray_angle / (num_rays - 1)

    for ray in range(num_rays):

        angle = vision_angle - ray_angle / 2 + delta_angle * ray

        (x, y) = position
        (i, j) = get_cell((x, y), CELL_SIZE)
        y_map = i * CELL_SIZE
        x_map = j * CELL_SIZE

        sin_a = sin(angle)
        cos_a = cos(angle)

        dir_o = (cos_a, sin_a)

        # vertical lines
        delta_depth = abs(CELL_SIZE * cos_a)

        ver_depth = 1e6
        if delta_depth > 1e-6:
            print("verticals", delta_depth, "cos_a", cos_a)
            dir = normalize(dir_o, delta_depth)

            if cos_a > 0:
                ver_depth = (x_map + CELL_SIZE - x) if cos_a < 1e-6 else (x_map + CELL_SIZE - x) / cos_a
            else:
                ver_depth = (x_map - x) if cos_a < 1e-6 else (x_map - x) / cos_a

            print("ver_depth", ver_depth)
            (x, y) = add_vector((x, y), normalize(dir_o, ver_depth+1e-6))

            iters = 0
            while iters < MAX_ITERS:
                (i, j) = get_cell((x, y), CELL_SIZE)
                if map[i][j] != 0:
                    break
                ver_depth += delta_depth
                (x, y) = add_vectors(dir, (x, y))
                iters += 1

        # horizontal lines
        (x, y) = position
        delta_depth = abs(CELL_SIZE * sin_a)

        hor_depth = 1e6
        if delta_depth > 1e-6:
            dir = normalize(dir_o, delta_depth)

            if sin_a > 0:
                hor_depth = (y_map + CELL_SIZE - y) if sin_a < 1e-6 else (y_map + CELL_SIZE - y) / sin_a
            else:
                hor_depth = (y - y_map) if sin_a < 1e-6 else (y_map - y) / sin_a

            (x, y) = add_vector((x, y), normalize(dir_o, hor_depth+1e-6))

            iters = 0
            while iters < MAX_ITERS:
                (i, j) = get_cell((x, y), CELL_SIZE)
                if map[i][j] != 0:
                    break
                hor_depth += delta_depth
                (x, y) = add_vectors(dir, (x, y))
                iters += 1

        print("ver_depth", ver_depth, "hor_depth", hor_depth)

        rays.append((angle, min(ver_depth, hor_depth)))

    return rays


