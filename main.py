import pygame, sys, math

'''
Story:
ein licht elementar hat seine familie verloren bei einem elementar krieg. es muss sie wiederfinden
du hast 50 jahre geschlafen
'''

GAME_SCALE = 2.0

class MainMenu():

    def __init__(self) -> None:
        self.title = "Ven - shine"
        self.size = (1100, 900)

        self.screen = pygame.display.set_mode((self.size[0], self.size[1]))
        pygame.display.set_caption(self.title)

        #  defining all diferent layer such as the ui or the game layer
        self.game_layer = pygame.surface.Surface((self.size[0] // GAME_SCALE,
                                                  self.size[1] // GAME_SCALE))
        self.ui_layer = pygame.surface.Surface((self.size[0] // GAME_SCALE,
                                                  self.size[1] // GAME_SCALE))
        
    def mainloop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.draw()
            self.update()

    def draw(self) -> None:
        pass

    def update(self) -> None:
        pass

if __name__ == "__main__":
    main = MainMenu()
    main.mainloop()
