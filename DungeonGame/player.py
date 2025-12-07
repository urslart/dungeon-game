import pygame

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 4

    def handle_input(self, keys, walls):
        dx, dy = 0, 0
        if keys[pygame.K_a]: dx -= self.speed
        if keys[pygame.K_d]: dx += self.speed
        if keys[pygame.K_w]: dy -= self.speed
        if keys[pygame.K_s]: dy += self.speed

        # Collision
        self.rect.x += dx
        for wall in walls:
            if self.rect.colliderect(wall):
                if dx > 0:
                    self.rect.right = wall.left
                if dx < 0:
                    self.rect.left = wall.right

        self.rect.y += dy
        for wall in walls:
            if self.rect.colliderect(wall):
                if dy > 0:
                    self.rect.bottom = wall.top
                if dy < 0:
                    self.rect.top = wall.bottom

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))
