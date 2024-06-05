import pygame, os

def load_image(path: str) -> pygame.Surface:
    image = pygame.image.load(path).convert()

    return image
