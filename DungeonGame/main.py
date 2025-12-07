import pygame
from player import Player
from enemy import Enemy
from item import Item
from tilemap import load_map, draw_map
from camera import Camera

pygame.init()

WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dungeon Game")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)

# Load images
wall_img = pygame.image.load("assets/images/wall.png").convert()
floor_img = pygame.image.load("assets/images/floor.png").convert()

def game_loop():
    player = Player(100, 100)
    enemies = [Enemy(400, 300), Enemy(600, 400)]
    items = [Item(300, 200), Item(700, 500)]

    walls, floor = load_map("map_layout.txt", TILE_SIZE)
    camera = Camera(WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.handle_input(keys, walls)

        # Update camera to follow player
        camera.update(player)

        # Update enemies
        for enemy in enemies:
            enemy.update(player)

        # Drawing
        screen.fill(BLACK)
        draw_map(screen, floor, walls, wall_img, floor_img, camera)

        for item in items:
            item.draw(screen, camera)
        for enemy in enemies:
            enemy.draw(screen, camera)
        player.draw(screen, camera)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
