import pygame
from math import pi, cos, sin, tan

from constants import CELL_SIZE, NUM_RAYS, \
    SCREEN_HEIGHT, SCREEN_WIDTH, DIST_TO_SCREEN, WALL_HEIGHT, \
    BLUE, GREEN, WHITE, BLACK, RED, \
    DT, SPEED, SPEED_ROT, \
    PLAYER_SIZE, VISION_ANGLE, FPS, map

from raycasting import compute_rays
from map import get_cell
from vector import normalize, polar_to_cartesian

position = (110.0, 110.0)
vision_angle = 0.0

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
clock = pygame.time.Clock()

pygame.display.set_caption("Labyrinth") 
exit = False

def draw_map(screen, map, position, rays, scale=1.0, xoffset=0.0, yoffset=0.0):
    for i, row in enumerate(map):
        for j, val in enumerate(row):
            x = j*CELL_SIZE*scale + xoffset
            y = i*CELL_SIZE*scale + yoffset
            width = CELL_SIZE*scale
            height = CELL_SIZE*scale
            if val != 0:
                pygame.draw.rect(screen, RED, pygame.Rect(x, y, width, height))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, width, height), width=1)
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, width*0.99, height*0.99))

    draw_player(screen, position, rays, scale, xoffset, yoffset)

def draw_player(screen, position, rays, scale=1.0, xoffset=0.0, yoffset=0.0):
    (x, y) = position
    (x, y) = (x*scale+xoffset, y*scale+yoffset)
    pygame.draw.circle(screen, GREEN, (x, y), int(2*10*scale))
    for ray in rays:
        (angle, depth) = ray
        (vx, vy) = polar_to_cartesian(depth*scale, angle)
        position_end = (x+vx, y+vy)
        pygame.draw.line(screen, BLUE, (x,y), position_end, 1)

def draw_3d_view(screen, rays, vision_angle):
    for (angle, depth) in rays:

        # remove fishbowl effect
        depth *= cos(angle - vision_angle)

        x = DIST_TO_SCREEN * tan(angle - vision_angle) + SCREEN_WIDTH / 2
        height = WALL_HEIGHT / (depth + 1e-4) * DIST_TO_SCREEN
        y = SCREEN_HEIGHT / 2 - height / 2
        width = SCREEN_WIDTH / NUM_RAYS
        color = [255 / (1 + depth * 1e-2)]*3
        pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))


def has_collided(map, position):
    (i, j) = get_cell(position, CELL_SIZE)
    return True if map[i][j] != 0 else False

def update_position(position, vision_angle):
    keys = pygame.key.get_pressed()

    (x, y) = list(position)
    sin_a = sin(vision_angle)
    cos_a = cos(vision_angle)

    (dx, dy) = (0,0)

    if keys[pygame.K_RIGHT]:
        normal = normalize((-sin_a, cos_a), SPEED * DT)
        dx = normal[0]
        dy = normal[1]
    if keys[pygame.K_LEFT]:
        normal = normalize((sin_a, -cos_a), SPEED * DT)
        dx = normal[0]
        dy = normal[1]
    if keys[pygame.K_DOWN]:
        dx = -SPEED * DT * cos_a
        dy = -SPEED * DT * sin_a
    if keys[pygame.K_UP]:
        dx = SPEED * DT * cos_a
        dy = SPEED * DT * sin_a

    if has_collided(map, (x+dx*PLAYER_SIZE,y+dy*PLAYER_SIZE)):
        return (x, y)
    else:
        return (x+dx, y+dy)

def update_vision_angle(vision_angle):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
        vision_angle += SPEED_ROT * DT
    if keys[pygame.K_z]:
        vision_angle -= SPEED_ROT * DT

    return vision_angle % (2 * pi)
  
while not exit: 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    position = update_position(position, vision_angle)
    vision_angle = update_vision_angle(vision_angle)
    rays = compute_rays(map, position, vision_angle, NUM_RAYS, VISION_ANGLE)

    screen.fill(BLACK)
    draw_3d_view(screen, rays, vision_angle)
    draw_map(screen, map, position, rays, scale=0.25)

    pygame.display.flip()
    clock.tick(FPS)
