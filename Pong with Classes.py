import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,420))
pygame.display.set_caption("Pong with Classes")
change1 = 0
change2 = 0
win = False
fontE = pygame.font.Font("freesansbold.ttf", 50)
class Ball():
    def __init__(self):
        self.x = 320
        self.y = 210
        self.color = (255, 255, 255)         
        self.radius = 15         
        self.xmovement = 5         
        self.ymovement = 5
    def draw(self):
        pygame.draw.circle(screen, self.color,(self.x, self.y),self.radius, self.radius)
    def bounceOffTopandBottom(self):
        if(self.y -15 == 0 or self.y + 15 == 420):
            self.ymovement = -self.ymovement
    def move(self):
        self.x += self.xmovement
        self.y += self.ymovement
    def reappear(self):
        if( self.x -15 > 640):
            self.x = 320
        if(self.x +15 <0):
            self.x = 320
    def checkCollision(self):
        if( self.x + 15 == p2.x and p2.y <= self.y <= p2.y +150  ):
            self.xmovement = -self.xmovement 
        if(self.x -15 == p1.x +30 and p1.y <= self.y <= p1.y+150):
            self.xmovement = -self.xmovement
    def changeScore(self):
        if(self.x -15 > 640):
            p1.score += 1
        if(self.x +15 <0):
            p2.score += 1
    def checkWin(self):
        if( p1.score == 5 or p2.score == 5):
            win = True
            screen.fill((255,255,255))
            if( p1.score == 5):
                s = "WINNER IS: Player 1"
                t = fontE.render(s, True, (0,0,0), (255,255,255))
                tr = t.get_rect()
                tr.center = (320, 210)
                screen.blit(t, tr)
            elif(p2.score == 5):
                s = "WINNER IS: Player 2"
                t = fontE.render(s, True, (0,0,0), (255,255,255))
                tr = t.get_rect()
                tr.center = (320, 210)
                screen.blit(t, tr)
            pygame.display.update()
            
class Paddle():     
    def __init__(self, color, x, y):         
        self.color = color         
        self.x = x         
        self.y = y         
        self.width = 30         
        self.height = 150 
        self.up = False         
        self.down = False         
        self.score = 0         
        self.speed = 10
    def draw(self):
        pygame.draw.rect(screen,self.color, (self.x, self.y, self.width,self.height))
    def showScore(self, text, xM,yM):
        self.text = text
        self.xM = xM
        self.yM = yM
        font= pygame.font.SysFont('freesans', 32)         
        msg = font.render(self.text, True, self.color)         
        screen.blit(msg, (xM,yM))
    def move(self, change):
        self.change = change
        if self.up and not self.down :
            self.change = -self.speed  
        elif not self.up and not self.down:
            self.change= 0
        elif self.down and not self.up:
            self.change = self.speed
        self.y = self.y + self.change
    def boundary(self):
        if(self.y <= 0):
            self.y = 0
        if(self.y >= 270):
            self.y = 270

p1 = Paddle((0,255,0), 10, 200)
p2 = Paddle((0,0,255), 600, 200)
ball = Ball()
while True:
    screen.fill((0,0,0))
    p1.draw()
    p2.draw()
    ball.draw()
    p2.showScore("Player 2: "+ str(p2.score), 500,10)
    p1.showScore("Player 1: "+ str(p1.score), 10,10 )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                p1.up = True
            elif event.key == K_s:
                p1.down = True
            elif event.key == K_UP:
                p2.up = True
            elif event.key == K_DOWN:
                p2.down = True
                
        elif event.type == KEYUP:
            if event.key == K_w:
                p1.up = False
            elif event.key == K_s:
                p1.down = False
            elif event.key == K_UP:
                p2.up = False
            elif event.key == K_DOWN:
                p2.down = False

    ball.reappear()
    ball.bounceOffTopandBottom()
    ball.move()
    ball.checkCollision()
    ball.changeScore()    
    p1.move(change1)
    p2.move(change2)
    p1.boundary()
    p2.boundary()
    ball.checkWin()
    pygame.display.update()
    if(win):
        break
    


