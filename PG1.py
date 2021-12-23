import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
red = (255,0,0)
pygame.display.set_caption("Shapes!!")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.circle(screen, (240,100,0), (320, 240), 50, 50)
    pygame.draw.circle(screen, (240,100,0), (0,0), 50,50)
    pygame.draw.circle(screen, (240,100,0), (0,480), 50,50)
    pygame.draw.circle(screen, (240,100,0), (640,480), 50,50)
    pygame.draw.circle(screen, (240,100,0), (640,0), 50,50)
    pygame.display.update()
