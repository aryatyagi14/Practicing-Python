import pygame, random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Flappy Bird")
bx= 300
by=300
ychange = 0
px = 400
py = 0
gap = 200
plength = 200
score = 0
scoreAdded = False
fontS = pygame.font.Font("freesansbold.ttf", 30)
fontE = pygame.font.Font("freesansbold.ttf", 80)
bird = pygame.image.load("/Users/aryatyagi/Desktop/fb.png")
background = pygame.image.load("/Users/aryatyagi/Desktop/bgl.png")
while True:
    screen.fill((255,255,255))
    screen.blit(background,(-100,-90))
    pygame.draw.rect(screen,(0,255,0),(px, py,100,plength))
    pygame.draw.rect(screen,(0,255,0), (px,py+plength+gap,100,600))
    #pygame.draw.circle(screen, (255,255,0),(bx,by),15,15)
    screen.blit(bird,(bx-62,by-62))

    s = "Score: " + str(score)
    text = fontS.render(s, True, (0,0,0), (255,255,255))
    textRect = text.get_rect()
    textRect.center = (70, 30)
    screen.blit(text, textRect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key== K_SPACE:
                ychange = -50
    if(bx-30 > px+100 and not scoreAdded):
        score +=1
        scoreAdded = True
    #checks for collision
    if((px <= bx+30 and bx-30 <px+100) and ((0<= by -30 and by-30 <= plength) or (py+plength+gap <= by+30 and by +30 <=600))):
        screen.fill((255,255,255))
        text = fontE.render("GAME OVER", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    #random pipe lengths
    if( px+100 <= 0):
        randlength = random.randint(10,350)
        plength = randlength
        px = 600
        scoreAdded = False
    #boundary limits
    if(by -30 <= 0 or by+30 >= 600):
        screen.fill((255,255,255))
        text = fontE.render("GAME OVER", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    #score limit
    if(score == 10):
        screen.fill((0,0,0))
        text = fontE.render("YOU WIN", True, (255,255,255), (0,0,0))
        textRect = text.get_rect()
        textRect.center = (300, 300)
        screen.blit(text, textRect)
        pygame.display.update()
        break
    by = by +2 +ychange
    ychange = 0
    px -=3
    pygame.display.update()



