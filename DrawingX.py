import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    pygame.draw.line(screen, (255,0,0), (0, 0), (600, 600), 3)
    pygame.draw.line(screen, (255,0,0), (0, 600), (600, 0), 3)
