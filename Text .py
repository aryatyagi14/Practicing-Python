import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Shapes!!")
font = pygame.font.Font('freesansbold.ttf', 32)
score = 0
while True:
    screen.fill((0,0,0))
    string = "Player 1: " + str(score)
    text = font.render(string, True, (255,0,0), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (320, 240)

    screen.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    score += 1
