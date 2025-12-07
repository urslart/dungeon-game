import pygame

class Item:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/item.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self.rect))
