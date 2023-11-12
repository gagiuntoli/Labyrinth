import pygame


CELL_SIZE = 100

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

FPS  = 24
COLS = len(map[0])
ROWS = len(map)

BLACK  = (0x00, 0x00, 0x00)
ORANGE = (0xFF, 0x8C, 0x00)
WHITE  = (0xFF, 0xFF, 0xFF)
RED    = (0xFF, 0x00, 0x00)
GREEN  = (0xAA, 0xFF, 0x00)

position = (110.0, 110.0)

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

def draw_player(screen, position):
    pygame.draw.circle(screen, GREEN, position, 10)
  
while not exit: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True

    draw_map(screen, map)

    draw_player(screen, position)

    pygame.display.flip()
    clock.tick(FPS)
