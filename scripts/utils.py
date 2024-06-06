import pygame, os

def load_image(path: str) -> pygame.Surface:
    image = pygame.image.load(path).convert_alpha()

    return image

def draw_rect(surf: pygame.Surface, color: list[int], rect: pygame.Rect) -> None:
    temp_surface = pygame.Surface((rect.width, rect.height))
    temp_surface.fill(color[:3])
    temp_surface.set_alpha(color[3])
    surf.blit(temp_surface, (rect.x, rect.y))

class Vektor():

    def __init__(self, pos: list[int]) -> None:
        self.pos = list(pos)

    def __sub__(self, other):
        return Vektor((self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]))
    
    def __add__(self, other):
        return Vektor((self.pos[0] + other.pos[0], self.pos[1] + other.pos[1]))
    
    def __div__(self, scale: float | int):
        return Vektor((self.pos[0] / scale, self.pos[1] / scale))
    
    def __truediv__(self, scale: int):
        return self.__div__(scale)
    
    def __mul__(self, scale: float | int):
        return Vektor((self.pos[0] * scale, self.pos[1] * scale))
