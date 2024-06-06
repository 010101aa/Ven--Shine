import pygame, os

from scripts.animations import Animation
from scripts.player import Player
from scripts.utils import load_image, Vektor
from scripts.projectiles import FireBall

GAME_SCALE = 2.0

class Game():

    def __init__(self, main) -> None:
        self.main = main
        self.display = pygame.Surface((self.main.size[0] // GAME_SCALE, self.main.size[1] // GAME_SCALE))

        self.assets = {
            "player/idle" : Animation("player/idle/", dur=18, anim_offset=[-6, -10]),
            "bg" : load_image("bg/bg.png"),
            "projectiles/fireball" : Animation("/Users/acc/Desktop/test_topdown/projectiles/fireball/")
        }

        self.player = Player(self)
        self.render_offset = [0, 0]

        self.camera_easing = [100, 100]

        self.particles = []
        self.fire_cool = 0

    def render(self, surf: pygame.Surface) -> None:
        self.display.fill((0, 0, 0))
        self.display.blit(self.assets["bg"], (self.render_offset[0], self.render_offset[1]))

        self.player.render(self.display, offset=self.render_offset)

        for particle in self.particles:
            particle.render(self.display, self.render_offset)

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

        if pygame.mouse.get_pressed()[0] and self.fire_cool <= 0:
            self.particles.append(FireBall(self.player.pos, (Vektor(pygame.mouse.get_pos()) / GAME_SCALE / 20 - (Vektor(self.player.rect.center) + Vektor(self.render_offset)) / 20).pos, 60, self))
            self.fire_cool = 0

        else:
            self.fire_cool -= 1

        self.player.update(dt)

        for particle in self.particles:
            if particle.update():
                self.particles.remove(particle)

        print(self.particles)
