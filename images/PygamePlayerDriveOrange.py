import pygame
from images.Colors import BLACK, WHITE, RED, GREEN, BLUE, YELLOW, ORANGE
from src.GameConfig import GRID_BLOCK_DIMENSIONS


n = None
o = ORANGE
w = WHITE
g = GREEN

player_orange_drive_img_pixel_array = [
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, w, w, w, w, w, w, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, w, w, w, o, w, w, w, w, o, w, w, w, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, w, o, o, o, o, w, w, w, w, o, o, o, o, w, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, w, o, o, o, o, o, w, w, w, w, o, o, o, o, o, w, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, w, o, o, o, o, o, o, o, w, w, o, o, o, o, o, o, o, w, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, w, n, n, n, n, n, n],
    [n, n, n, n, n, w, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, w, n, n, n, n, n],
    [n, n, n, n, n, w, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, w, n, n, n, n, n],
    [n, n, n, n, w, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, w, n, n, n, n],
    [n, n, n, n, w, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, w, n, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, w, w, o, o, o, o, w, n, n, n],
    [n, n, n, w, o, o, o, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, w, w, o, o, o, o, w, n, n, n],
    [n, n, n, n, w, o, o, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, w, w, o, o, o, w, n, n, n, n],
    [n, n, n, n, w, o, o, o, w, w, w, o, o, o, o, o, o, o, o, o, o, w, w, w, o, o, o, w, n, n, n, n],
    [n, n, n, n, n, w, o, o, o, w, w, o, o, o, o, o, o, o, o, o, o, w, w, o, o, o, w, n, n, n, n, n],
    [n, n, n, n, n, w, o, o, o, w, w, w, o, o, o, o, o, o, o, o, w, w, w, o, o, o, w, n, n, n, n, n],
    [n, n, n, n, n, n, w, o, o, o, w, w, w, o, o, o, o, o, o, w, w, w, o, o, o, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, w, o, o, o, o, w, w, w, w, w, w, w, w, w, w, o, o, o, o, w, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, w, o, o, o, o, w, w, w, w, w, w, w, w, o, o, o, o, w, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, w, o, o, o, o, o, o, o, o, o, o, o, o, w, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, w, w, w, o, o, o, o, o, o, w, w, w, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, w, w, w, w, w, w, n, n, n, n, n, n, n, n, n, n, n, n, n],
    [n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n, n]
]

player_orange_drive_img = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
for i in range(len(player_orange_drive_img_pixel_array)):
    for j in range(len(player_orange_drive_img_pixel_array[0])):
        if player_orange_drive_img_pixel_array[i][j] != None:
            player_orange_drive_img.set_at((j, i), player_orange_drive_img_pixel_array[i][j])

player_orange_drive_img = pygame.transform.scale(player_orange_drive_img, (GRID_BLOCK_DIMENSIONS[0], GRID_BLOCK_DIMENSIONS[1]))
