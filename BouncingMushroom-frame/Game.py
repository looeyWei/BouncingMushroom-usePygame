import pygame
from Window import *


class Game:
    def __init__(self):
        self.window = Window()
        
        self.mushroom = pygame.image.load(r"F:\workspace\BouncingMushroom-usePygame\BouncingMushroom-frame\Assets\Mushroom.png")

        self.mushroom_rect = self.mushroom.get_rect()

        self.increment = [1, 1]


    def HandleInput(self):
        pass


    def Update(self):
        self.window.Update()
        self.MoveMushroom()


    def Render(self):
        self.window.BeginDraw()
        # draw
        self.window.Draw(self.mushroom, self.mushroom_rect.topleft)
        self.window.EndDraw()

    def MoveMushroom(self):
        if (self.mushroom_rect.topright[0] > 640 and self.increment[0] > 0) or \
            (self.mushroom_rect.x < 0 and self.increment[0]<0): 
            self.increment[0] = -self.increment[0]

        if (self.mushroom_rect.bottomleft[1] > 480 and self.increment[1] > 0) or \
            (self.mushroom_rect.y < 0 and self.increment[1]<0):
            self.increment[1] = -self.increment[1]
        
        self.mushroom_rect.x += self.increment[0]
        self.mushroom_rect.y += self.increment[1]

    # get set methods
    def GetWindow(self):
        return self.window