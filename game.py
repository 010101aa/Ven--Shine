import pygame

from scripts.animations import Animation
from scripts.player import Player

GAME_SCALE = 2.0

class Game():

    def __init__(self, main) -> None:
        self.main = main
        self.display = pygame.Surface((self.main.size[0] // GAME_SCALE, self.main.size[1] // GAME_SCALE))

        self.assets = {
            "player/idle" : Animation("player/idle/")
        }

        self.player = Player(self)
        self.render_offset = [0, 0]

        self.camera_easing = [35, 35]

    def render(self, surf: pygame.Surface) -> None:
        self.display.fill((0, 0, 0))

        self.player.render(self.display, offset=self.render_offset)

        surf.blit(self.display, (0, 0))


    def update(self, dt: float) -> None:
        #  update kamera pos (render_offset)
        offset = [0, 0]
        offset[0] = self.main.size[0] // 2 // GAME_SCALE - (self.player.pos[0] + self.render_offset[0] + self.player.size[0] // 2)
        offset[1] = self.main.size[1] // 2 // GAME_SCALE - (self.player.pos[1] + self.render_offset[1] + self.player.size[1] // 2)

        if abs(offset[0] / (self.camera_easing[0] + 7)) > 0:
            self.render_offset[0] += offset[0] / self.camera_easing[0]

        if abs(offset[1] / (self.camera_easing[1] + 7)) > 0:
            self.render_offset[1] += offset[1] / self.camera_easing[1]

        self.player.update(dt)
