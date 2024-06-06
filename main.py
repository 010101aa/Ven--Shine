import pygame, sys, math, time

from game import Game

'''
Story:
ein licht elementar hat seine familie verloren bei einem elementar krieg. es muss sie wiederfinden
du hast 50 jahre geschlafen
'''

GAME_SCALE = 2.0

class MainMenu():

    def __init__(self) -> None:
        pygame.init()

        self.title = "Ven - Shine"
        self.size = (850, 700)

        self.screen = pygame.display.set_mode((self.size[0], self.size[1]))
        pygame.display.set_caption(self.title)

        #  defining all diferent layer such as the ui or the game layer
        self.game_layer = pygame.surface.Surface((self.size[0] // GAME_SCALE,
                                                  self.size[1] // GAME_SCALE))
        self.ui_layer = pygame.surface.Surface((self.size[0] // GAME_SCALE,
                                                  self.size[1] // GAME_SCALE))

        self.fps = 120
        self.clock = pygame.time.Clock()

        self.game = Game(self)
        self.current = "game"

        self.font = pygame.font.Font(None, 30)
        self.current_fps = self.fps
        
    def mainloop(self) -> None:
        last_time = time.time()
        f_counter = 0

        while True:
            #  delta time calculation
            self.dt = time.time() - last_time

            if f_counter + 1 % (self.fps / 2) == 0:
                self.current_fps = (1000 / self.dt) / 1000

            self.dt *= self.fps

            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.render()
            self.update()

            f_counter += 1

            self.clock.tick(self.fps)

    def render(self) -> None:
        if self.current == "game":
            self.game.render(self.game_layer)
            self.screen.blit(pygame.transform.scale_by(self.game_layer, GAME_SCALE), (0, 0))

        self.screen.blit(self.font.render("FPS: " + str(round(self.current_fps)), True, (255, 255, 255), (0, 0, 0)), (20, 20))

        pygame.display.update()

    def update(self) -> None:
        if self.current == "game":
            self.game.update(self.dt)

if __name__ == "__main__":
    main = MainMenu()
    main.mainloop()
