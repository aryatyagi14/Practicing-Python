import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")
XTurn = True
taken1 = False
taken2 = False
taken3 = False
taken4 = False
taken5 = False
taken6 = False
taken7 = False
taken8 = False
taken9 = False
fontE = pygame.font.Font("freesansbold.ttf", 100)
b = ["","","","","","","","",""]
global XWin 
global OWin
XWin = False
OWin = False
def drawX(x,y): 
    pygame.draw.line(screen, (255,255,255), (x,y),(x+200,y+200), 1)
    pygame.draw.line(screen, (255,255,255),(x+200,y),(x,y+200),1)
def coverX(x,y):
    pygame.draw.line(screen, (0,0,0), (x,y),(x+200,y+200), 1)
    pygame.draw.line(screen, (0,0,0),(x+200,y),(x,y+200),1)
def drawO(x,y):
    pygame.draw.circle(screen,(255,255,255),(x+100,y+100),100,1)
def coverO(x,y):
    pygame.draw.circle(screen,(0,0,0),(x+100,y+100),100,1)
while True:
    pygame.draw.line(screen, (255,255,255),(200,0),(200,600),1)
    pygame.draw.line(screen, (255,255,255),(400,0),(400,600),1)
    pygame.draw.line(screen, (255,255,255),(0,200),(600,200),1)
    pygame.draw.line(screen,(255,255,255),(0,400),(600,400),1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if(0 <= x and x < 200 and 0 <=y and y < 200 and not taken1):
                taken1 = True
                if(XTurn):
                    drawX(0,0)
                    b[0] = "x"
                else:
                    drawO(0,0)
                    b[0] = "o"
            elif(200 <= x and x< 400 and 0 <=y and y < 200 and not taken2):
                taken2 = True
                if(XTurn):
                    drawX(200,0)
                    b[1] = "x"
                else:
                    drawO(200,0)
                    b[1] = "o"
            elif(400<= x and x < 600 and 0 <=y and y < 200 and not taken3):
                taken3 = True
                if(XTurn):
                    drawX(400,0)
                    b[2] = "x"
                else:
                    drawO(400,0)
                    b[2] = "o"
            elif(0<= x and x < 200 and 200 <=y and y < 400 and not taken4):
                taken4 = True
                if(XTurn):
                    drawX(0,200)
                    b[3] = "x"
                else:
                    drawO(0,200)
                    b[3] = "o"
            elif(200<= x and x < 400 and 200 <=y and y < 400 and not taken5):
                taken5 = True
                if(XTurn):
                    drawX(200,200)
                    b[4] = "x"
                else:
                    drawO(200,200)
                    b[4] = "o"
            elif(400<= x and x < 600 and 200 <=y and y < 400 and not taken6):
                taken6 = True
                if(XTurn):
                    drawX(400,200)
                    b[5] = "x"
                else:
                    drawO(400,200)
                    b[5] = "o"
            elif(0<= x and x < 200 and 400 <=y and y < 600 and not taken7):
                taken7 = True
                if(XTurn):
                    drawX(0,400)
                    b[6] = "x"
                else:
                    drawO(0,400)
                    b[6] = "o"
            elif(200<= x and x < 400 and 400 <=y and y < 600 and not taken8):
                taken8 = True
                if(XTurn):
                    drawX(200,400)
                    b[7] = "x"
                else:
                    drawO(200,400)
                    b[7] = "o"
            elif(400<= x and x < 600 and 400 <=y and y < 600 and not taken9):
                taken9 = True
                if(XTurn):
                    drawX(400,400)
                    b[8] = "x"
                else:
                    drawO(400,400)
                    b[8] = "o"
            XTurn = not XTurn
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print ("You released the left mouse button at",event.pos)
    if(XWin):
        screen.fill((0,0,0))
        text = fontE.render("X WINS", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    elif(OWin):
        screen.fill((0,0,0))
        text = fontE.render("O WINS", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    elif(taken1 == True and taken2 == True and taken3 == True and taken4 ==True and taken5 == True and taken6==True and taken7 == True and taken8 ==True):
        screen.fill((0,0,0))
        text = fontE.render("TIE GAME", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    if((b[0] == b[1] and b[1] == b[2] ) or (b[0] == b[3] and b[3] == b[6])):
        if(b[0] == "x"):
            XWin = True
        elif(b[0] == "o") :
            OWin = True
    elif((b[8]==b[5] and b[8] == b[2]) or (b[8]==b[7] and b[8]==b[6])):
        if(b[8] == "x"):
            XWin = True
        elif(b[8] == "o") :
            OWin = True
    elif((b[4] == b[0] and b[4] == b[8]) or (b[4] == b[2] and b[4]==b[6]) or (b[1] == b[4] and b[4] == b[7]) or (b[4]==b[3] and b[4]==b[5])):
        if(b[4] == "x"):
            XWin = True
        elif(b[4] == "o") :
            OWin = True
    pygame.display.update()
    
