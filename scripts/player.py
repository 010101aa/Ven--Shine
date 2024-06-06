import pygame, math

from scripts.utils import draw_rect

class Player():

    def __init__(self, game) -> None:
        self.pos = [0, 0]
        self.game = game

        self.action = ""
        self.set_action("idle")

        self.size = [20, 19]

        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def set_action(self, action: str) -> None:
        if action != self.action:
            self.action = action
            self.animation = self.game.assets["player/" + action]

    def update(self, dt: float) -> None:
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

        keys = pygame.key.get_pressed()

        self.movement = [0, 0]
        if keys[pygame.K_d]:
            self.movement[0] += 2

        if keys[pygame.K_a]:
            self.movement[0] -= 2

        if keys[pygame.K_s]:
            self.movement[1] += 2

        if keys[pygame.K_w]:
            self.movement[1] -= 2

        self.pos[0] += self.movement[0] * dt
        self.pos[1] += self.movement[1] * dt

        self.animation.update()

    def render(self, surf: pygame.Surface, offset: list[int] = [0, 0]):
        draw_rect(surf, (255, 0, 0, 100), pygame.Rect(self.rect.x + offset[0], self.rect.y + offset[1], self.rect.width, self.rect.height))
        self.animation.render(surf, self.pos, offset=offset)
