import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Shapes!!")
edgeR = 30
edgeG = 610
counter = 1
backward = False
forward = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    xR = edgeR+ counter
    xG = edgeG- counter
    pygame.draw.circle(screen, (255,0,0),(xR,240),30,30)
    pygame.draw.circle(screen, (0,255,0),(xG,240),30,30)
    if(xR+30 == xG-30):
        edgeR = 290
        edgeG = 350
        counter = -1
        forward = False
        print("Backward")
    if(not forward):
        counter = counter -1
    if(forward):
        counter = counter + 1
    if((xR-30 == 0) and (xG +30 ==640)):
        forward = True
        edgeR = 30
        edgeG = 610
        counter = 1
        print("hello")
    pygame.display.update()
    

