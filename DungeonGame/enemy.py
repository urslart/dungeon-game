import pygame
import random

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2

    def update(self, player):
        # Simple chase AI
        if player.rect.x > self.rect.x:
            self.rect.x += self.speed
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        if player.rect.y > self.rect.y:
            self.rect.y += self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))
