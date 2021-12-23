import pygame, random, sys
#import pygame.freetype
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,420))
pygame.display.set_caption(("PONG"))
font = pygame.font.Font('freesansbold.ttf', 32)
fontE = pygame.font.Font("freesansbold.ttf", 50)
py1 = 10
py2 = 260
px1 = 10
px2 = 580
pw = False
ps = False
pu = False
pd = False
change1 = 0
change2 = 0
bx = 320
by = 210
speedx = 5
speedy =5
score1 = 0
score2 = 0
while True:
    screen.fill((0,0,0))
    string = "Player 1: " + str(score1)
    text = font.render(string, True, (255,255,255), (0,0,0))
    textRect = text.get_rect()
    textRect.center = (90, 20)
    screen.blit(text, textRect)

    string1 = "Player 2: " + str(score2)
    text1 = font.render(string1, True, (255,255,255), (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = (550, 20)
    screen.blit(text1, textRect1)
        #making the objects
    pygame.draw.rect(screen,(0,255,0), (px1,py1, 30,150))
    pygame.draw.rect(screen,(255,0,0),(px2,py2,30,150))

    pygame.draw.circle(screen, (255,255,255), (bx,by),15,15)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        elif event.type == KEYDOWN:
            if event.key == K_w:
                pw = True
            elif event.key == K_s:
                ps = True
            elif event.key == K_UP:
                pu = True
            elif event.key == K_DOWN:
                pd = True
                
        elif event.type == KEYUP:
            if event.key == K_w:
                pw = False
            elif event.key == K_s:
                ps = False
            elif event.key == K_UP:
                pu = False
            elif event.key == K_DOWN:
                pd = False
    #makes sure ball doesnt go off top and bottom
    if( by -15 == 0 or by + 15 == 420):
        speedy = -speedy
    #Moves Ball
    bx = bx+ speedx
    by += speedy
    #detects Collision with player 2
    if( bx + 15 == px2 and py2 <= by <= py2+150  ):
        speedx = -speedx 
    if(bx -15 == px1 +30 and py1 <= by <= py1+150):
        speedx = -speedx
    #makes ball keep reappearing
    if( bx -15 > 640):
        bx = 320
        score1 += 1
        print(score2)
    if(bx +15 <0):
        bx = 320
        score2 +=1
        print(score1)
    #makes the paddles move
    py1 =py1+change1 
    if pw and not ps :
        change1= -5  
    elif not pw and not ps:
        change1=0
    elif ps and not pw:
        change1 =5

    py2 = py2+change2
    if pu and not pd:
        change2 = -5
    elif not pu and not pd:
        change2 = 0
    elif pd and not pu:
        change2 = 5
    #paddles not able to go off screen
    if(py1 <= 0):
        py1 = 0
    if(py1 >= 270):
        py1 = 270

    if(py2 <= 0):
        py2 = 0
    if(py2 >= 270):
        py2 = 270
    #checks for a winner
    if( score1 == 5 or score2 == 5):
        screen.fill((255,255,255))
        if( score1 == 5):
            s = "WINNER IS: Player 1"
            t = fontE.render(s, True, (0,0,0), (255,255,255))
            tr = t.get_rect()
            tr.center = (320, 210)
            screen.blit(t, tr)
        elif(score2 == 5):
            s = "WINNER IS: Player 2"
            t = fontE.render(s, True, (0,0,0), (255,255,255))
            tr = t.get_rect()
            tr.center = (320, 210)
            screen.blit(t, tr)
        pygame.display.update()
        break 
    pygame.display.update()
    
        
    
