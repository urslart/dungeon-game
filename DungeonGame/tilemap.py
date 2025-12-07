import pygame

def load_map(filename, tile_size):
    walls = []
    floor = []
    with open(filename, 'r') as f:
        for y, line in enumerate(f):
            for x, char in enumerate(line.strip()):
                rect = pygame.Rect(x * tile_size, y * tile_size, tile_size, tile_size)
                if char == '#':
                    walls.append(rect)
                else:
                    floor.append(rect)
    return walls, floor

def draw_map(screen, floor, walls, wall_img, floor_img, camera):
    for tile in floor:
        screen.blit(floor_img, camera.apply(tile))
    for tile in walls:
        screen.blit(wall_img, camera.apply(tile))
