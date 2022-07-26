from pickle import TRUE
from turtle import width
import pygame

WIDTH, HEIGHT = 700, 500

#SIZING
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Caption
pygame.display.set_caption("PONG")

def main():
    run = True

    while run:
        for event in pygame.event.get(): #All of the events that will occur
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


