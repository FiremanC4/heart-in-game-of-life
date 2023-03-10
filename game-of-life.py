import pygame
import time
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1500, 900
TILE = 100
W, H = WIDTH // TILE, HEIGHT // TILE
FPS = 2

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

text_field = """000000000000000
000000000000000
000001101100000
000010010010000
000010000010000
000001000100000
000000101000000
000000010000000
000000000000000
"""

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [list(map(int,row)) for row in text_field.split('\n')]


def check_cell(current_field, x, y):
    count = 0
    for j in range(y - 1, y + 2):
        for i in range(x - 1, x + 2):
            if current_field[j][i]:
                count += 1

    if current_field[y][x]:
        count -= 1
        if count == 2 or count == 3:
            return 1
        return 0
    else:
        if count == 3:
            return 1
        return 0

surface.fill(pygame.Color('indigo'))
[pygame.draw.line(surface, pygame.Color('darkorchid4'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
[pygame.draw.line(surface, pygame.Color('darkorchid4'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
# draw life
for x in range(1, W - 1):
    for y in range(1, H - 1):
        if current_field[y][x]:
            pygame.draw.rect(surface, pygame.Color('deeppink1'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
        next_field[y][x] = check_cell(current_field, x, y)
current_field = deepcopy(next_field)
# print(clock.get_fps())
pygame.display.flip()

state = True
while True:

    surface.fill(pygame.Color('indigo'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if state:
                state = False
            else:
                exit()
    if not state:
        [pygame.draw.line(surface, pygame.Color('darkorchid4'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TILE)]
        [pygame.draw.line(surface, pygame.Color('darkorchid4'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TILE)]
        # draw life
        for x in range(1, W - 1):
            for y in range(1, H - 1):
                if current_field[y][x]:
                    pygame.draw.rect(surface, pygame.Color('deeppink1'), (x * TILE + 2, y * TILE + 2, TILE - 2, TILE - 2))
                next_field[y][x] = check_cell(current_field, x, y)

        current_field = deepcopy(next_field)

        # print(clock.get_fps())
        clock.tick(FPS)
        pygame.display.flip()