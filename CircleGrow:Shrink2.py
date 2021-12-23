import pygame
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))

pygame.display.set_caption("Shapes!!")
counter = 1
shrink = False
change=1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255), (300,300), 10*counter,10*counter)
    pygame.display.update()
    counter = counter +change
    if counter==30:
        change = -1
    if counter <1 :
        change = 1
    

