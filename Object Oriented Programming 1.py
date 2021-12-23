import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Shapes!!")
red=(255,0,0)
blue = (0,0,255)
class Ball:
    def __init__(self, x,y,color, radius):
        self.x=x
        self.y=y
        self.color=color
        self.radius = radius

    def show(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius,self.radius)

    def changeColor(self, color):
        self.color = color
        pygame.draw.circle(screen, self.color,(self.x, self.y), self.radius,self.radius)
        
while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
   

    b1=Ball(320,240, red, 30)
    b1.changeColor(blue)
    b1.show()
    print(b1.x, b1.y, b1.color)
    
    b2=Ball(100,100, red, 30)
    b2.show()
    pygame.display.update()
    
