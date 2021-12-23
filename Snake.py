import pygame
import random 
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("snake")
class Snake():
    def __init__(self):
        self.length = 1
        self.x = 20
        self.y = 20
        self.addLength = False
        self.md = False
        self.mu = False
        self.mr = False
        self.ml = False
    def draw(self):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 20))
    def movedown(self):
        self.y += 20
    def moveup(self):
        self.y -= 20
    def moveright(self):
        self.x += 20
    def moveleft(self):
        self.x -= 20
    def checkfood(self):
        if self.x == foodx and self.y == foody:
            self.addLength = True
            return True
def drawboard():
    i = 1
    for i in range(30):
        pygame.draw.line(screen, (255,255,255), (i*20, 0), (i*20, 600), 1)
        pygame.draw.line(screen, (255,255,255), (0, i*20), (600, i*20), 1)
foodx = (random.randint(0,600) // 20 ) * 20
foody = (random.randint(0,600) // 20 ) * 20
s = Snake()
def drawFood():
    global foodx
    global foody
    if(s.checkfood()):
        foodx = (random.randint(0,600) // 20 ) * 20
        foody = (random.randint(0,600) // 20 ) * 20
        s.length +=1
    pygame.draw.rect(screen, (0,255,0),(foodx, foody, 20, 20))
    

counter = 0

while True:
    screen.fill((0,0,0))
    drawFood()
    s.draw()
    drawboard()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                s.mu = False
                s.md = False
                s.ml = True
                s.mr = False
            elif event.key == K_RIGHT:
                s.mu = False
                s.md = False
                s.ml = False
                s.mr = True
            elif event.key == K_UP:
                s.mu = True
                s.md = False
                s.ml = False
                s.mr = False
            elif event.key == K_DOWN:
                s.md = True
                s.mu = False
                s.ml = False
                s.mr = False
    #MOVES Snake
    counter += 1
    if counter > 5:
        counter =0
    if s.md and counter == 5:
        s.movedown()
        counter = 0
    elif s.mu and counter == 5:
        s.moveup()
        counter= 0
    elif s.ml and counter == 5:
        s.moveleft()
        counter= 0
    elif s.mr and counter == 5:
        s.moveright()
        counter= 0
    s.checkfood()
    if s.addLength == True and counter == 5:
        s.length += 1
        s.addLength = False
    print(s.length)
    pygame.display.update()
