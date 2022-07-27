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

#Ball vars
BALL_RADIUS = 7

#Object class Paddle
class Paddle:
    COLOR = WHITE
    VEL =  4        #Class variables that exist for all instances of the object "Paddle"

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up = True): #If up = True, we can move the pedal up by the vel, otherwise, we move the pedal down
        if up:                 #Weird logic for the x-y coordinate system, needs brush-up with pygame documentation
            self.y -= self.VEL
        else:
            self.y += self.VEL

class Ball:
    COLOR = WHITE
    MAX_VAL = 5
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VAL
        self.y_vel = 0


    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel



        
#Draw the objects
def draw(win, paddles, ball):
    win.fill(BLACK)

    for paddle in paddles: 
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    
    ball.draw(win)

    pygame.display.update() #updates the model at a 60FPS pace


def handle_paddle_movement(keys, left_paddle, right_paddle):
    #Move the left paddle with w and s keys
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >= 0:
        left_paddle.move(up = True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up = False)

    #Move the right paddle with UP and DOWN keys
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >= 0:
        right_paddle.move(up = True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up = False)


#Main class
def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)



    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball) #Redraws 60 time a second

        for event in pygame.event.get(): #All of the events that will occur
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
    pygame.quit()

if __name__ == '__main__':
    main()

