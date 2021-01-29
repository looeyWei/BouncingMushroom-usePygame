
from Game import *
import pygame


class main:
    def __init__(self):
        pygame.init()

        game = Game()
        while game.GetWindow().IsDone() == False:
            game.HandleInput()
            game.Update()
            game.Render()


if __name__ == "__main__":
    main()