import pygame, math

class Player():

    def __init__(self, game) -> None:
        self.pos = [0, 0]
        self.game = game

        self.action = ""
        self.set_action("idle")

        self.size = [20, 20]

    def set_action(self, action: str) -> None:
        if action != self.action:
            self.action = action
            self.animation = self.game.assets["player/" + action]

    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        self.movement = [0, 0]
        if keys[pygame.K_d]:
            self.movement[0] += 1

        if keys[pygame.K_a]:
            self.movement[0] -= 1

        if keys[pygame.K_s]:
            self.movement[1] += 1

        if keys[pygame.K_w]:
            self.movement[1] -= 1

        self.pos[0] += self.movement[0] * dt
        self.pos[1] += self.movement[1] * dt

        self.animation.update()

    def render(self, surf: pygame.Surface, offset: list[int] = [0, 0]):
        self.animation.render(surf, self.pos, offset=offset)
