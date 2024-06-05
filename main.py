import pygame, sys, math

GAME_SCALE = 2.0

class MainMenu():

    def __init__(self) -> None:
        self.title = ""
        self.size = ()

        self.screen = pygame.display.set_mode((self.size[0], self.size[1]))

        #  defining all diferent layer such as the ui or the game layer
        self.game_layer = pygame.surface.Surface((self.size[0] // (1 // GAME_SCALE),
                                                  self.size[1] // (1 // GAME_SCALE)))
        self.ui_layer = pygame.surface.Surface((self.size[0] // (1 // GAME_SCALE),
                                                  self.size[1] // (1 // GAME_SCALE)))
        
    def mainloop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
