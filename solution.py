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

#Paddle variables for height and width
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100  

#Object class Paddle
class Paddle:
    COLOR = WHITE

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

#Draw the objects
def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles: 
        paddle.draw(win)
    
    pygame.display.update()


#Main class
def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle]) #Redraws 60 time a second

        for event in pygame.event.get(): #All of the events that will occur
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == '__main__':
    main()

