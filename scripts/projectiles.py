import pygame

from scripts.animations import Animation

class Projectile():

    def __init__(self, pos: list[int], vel: list[int], live_span: int, game) -> None:
        self.game = game

        self.velocity = list(vel)
        self.alive_counter = int(live_span)

        self.pos = list(pos)

    def update(self) -> None:
        self.pos[0] += self.velocity[0]
        self.pos[1] += self.velocity[1]

class FireBall(Projectile):

    def __init__(self, pos: list[int], vel: list[int], live_span: int, game) -> None:
        self.size = [6, 8]
        pos = [pos[0] - self.size[0] // 2 + game.player.size[0] // 2, pos[1] - self.size[1] // 2 + game.player.size[1] // 2]

        super().__init__(pos, vel, live_span, game)

        self.animation = self.game.assets["projectiles/fireball"].copy()

        #  calculate rotation and rotate the image

    def update(self) -> bool:
        super().update()

        self.animation.update()

        print(self.alive_counter, self.animation.frame)
        if self.animation.frame > self.alive_counter:
            return True
        
        return False

    def render(self, surf: pygame.Surface, offset: list[int] = [0, 0]):
        surf.blit(self.animation.get_img(), (self.pos[0] + offset[0], self.pos[1] + offset[1]))
