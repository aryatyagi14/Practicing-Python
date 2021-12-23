import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Simple Ball")
red = (255,0,0)
class Ball():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y), 20)
    def update(self):
        screen.blit(screen,(self.x,self.y))
    def changeColor(self):
        rand1 = random.randint(0,255)
        rand2 = random.randint(0,255)
        rand3 = random.randint(0,255)
        self.color = (rand1,rand2,rand3)
    def isClicked(self, mouse_pos):
        if self.x-20< mouse_pos[0]< self.x+20 and self.y-20< mouse_pos[1]< self.y+20:
            print("Ball was clicked")
            return True
        else:
            return False
counter = 0        
balls = []      
ball0 = Ball(320,240,red)
balls.append(ball0)
counter+= 1
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key== K_SPACE:
                name = "ball" + str(counter)
                randx = random.randint(0,640)
                randy = random.randint(0,480)
                name = Ball(randx, randy, red)
                balls.append(name)
                counter += 1
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print( "You pressed the left mouse button at",event.pos)
            for i in balls:
                if(i.isClicked(event.pos)):
                    i.changeColor()
    for i in balls:
        i.draw()
    pygame.display.update()

        
