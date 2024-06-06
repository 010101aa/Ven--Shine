import pygame, os

from scripts.utils import load_image

class Animation():

    def __init__(self, dir_path: str, dur: int = 5, anim_offset: list[int] = [0, 0]) -> None:
        self.dir_path = dir_path

        self.img_dur = dur

        self.anim_offset = anim_offset

        self.anim_index = 0
        self.images = []

        self.frame = 0

        for image in os.listdir(self.dir_path):
            if image.endswith(".png"):
                self.images.append(load_image(os.path.abspath(os.path.join(self.dir_path, image))))

    def update(self) -> None:
        self.frame += 1

        self.anim_index = self.frame // self.img_dur % len(self.images)

    def get_img(self) -> pygame.Surface:
        return self.images[self.anim_index]

    def render(self, surf: pygame.Surface, pos: list[int], offset: list[int] = [0, 0]) -> None:
        surf.blit(self.get_img(),
                  (pos[0] + offset[0] + self.anim_offset[0], pos[1] + offset[1] + self.anim_offset[1]))
        
    def copy(self):
        return Animation(self.dir_path, self.img_dur, self.anim_offset)
        