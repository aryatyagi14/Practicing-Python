import pygame
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))

pygame.display.set_caption("Shapes!!")
counter = 1
shrink = False
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if counter == 40:
        shrink = True
    if(shrink == False):
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255), (320,240), 10*counter,10*counter)
        pygame.display.update()
        counter = counter +1
    elif(shrink and counter >0):
        screen.fill((0,0,0))
        pygame.draw.circle(screen,(255,255,255), (320,240), 10*counter,10*counter)
        pygame.display.update()
        counter = counter -1
    

