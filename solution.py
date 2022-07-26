import pygame
pygame.init()

WIDTH, HEIGHT = 700, 500

#SIZING
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Caption
pygame.display.set_caption("PONG")

#Frames per second for the window
FPS = 60

#Variable names for the colors to be used -> enhances the coloring process
WHITE = (255,255,255)
BLACK = (0,0,0)



class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win):
    win.fill(BLACK)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw(WIN) #Redraws 60 time a second

        for event in pygame.event.get(): #All of the events that will occur
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()

