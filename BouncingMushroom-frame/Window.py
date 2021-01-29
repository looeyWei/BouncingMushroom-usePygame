
import pygame

class Window:
    def __init__(self):
        self.windowSize = (640, 480)

        self.window = pygame.display.set_mode(self.windowSize)
        
        self.done = False

    # 窗口事件
    def Update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    # 用黑色填充清屏
    def BeginDraw(self):
        self.window.fill((0,0,0))

    def Draw(self, drawable, topleft):
        self.window.blit(drawable, topleft)

    def EndDraw(self):
        pygame.display.update()

    # get set method
    def GetWindowSize(self):
        return self.windowSize
    
    def IsDone(self):
        return self.done