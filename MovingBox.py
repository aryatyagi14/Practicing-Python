import pygame
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("Moving Box")
counter = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.fill((0,0,0))
    
    s = pygame.display.get_surface()
    r = pygame.Rect(counter ,counter,100,100)
    s.fill(Color("red"), r)
    pygame.display.flip()
    
    #pygame.draw.rect(screen, (255,0,0), (counter,counter,100,100), 1)
    counter = counter +100
    if( counter == 700):
        counter = 0
    time.sleep(.1)
    pygame.display.update()
    
