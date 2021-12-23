import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Space Invaders")
a1 = pygame.image.load("/Users/aryatyagi/Desktop/a1.png")
a1 = pygame.transform.scale(a1,(100,100))
a2 = pygame.image.load("/Users/aryatyagi/Desktop/a2.png")
a2 = pygame.transform.scale(a2,(90,65))
a3 = pygame.image.load("/Users/aryatyagi/Desktop/a3.png")
a3 = pygame.transform.scale(a3,(90,105))
class Alien():
    def __init__(self, x,y, image):
        self.x = x
        self.y = y
        self.ix = x
        self.iy = y
        self.cd = False
        self.speed = 1
        self.image = image
    def draw(self):
        screen.blit(self.image,(self.x, self.y))
    def moveH(self, al):
        self.x += self.speed
        if (self.x >= 560 or self.x <= -20):
            self.cd = True
        if(self.x <= -20):
            self.x +=2
    
class Player():
    def __init__(self):
        self.x = 300
        self.y = 380
        self.health = 100
        self.left = False
        self.right = False
        img = pygame.image.load("/Users/aryatyagi/Desktop/ship.png")
        img = pygame.transform.scale(img,(110,110))
        self.image = img
    def draw(self):
        screen.blit(self.image,(self.x, self.y))
    def move(self):
        change = 5
        if( self.x <= 0):
            self.x = 0
        elif(self.x >= 550):
            self.x = 550
        if (self.left):
            self.x -= change
        elif(self.right):
            self.x += change
    def showHealth(self):
        string = "Health : " + str(self.health)
        font= pygame.font.SysFont('freesans', 32)         
        msg = font.render(string, True, (255,255,255))         
        screen.blit(msg, (10,440))
class BulletP():
    def __init__(self):
        self.x = p.x +45
        self.y = p.y +10
        self.speed = 5
        self.shootU = False
        self.used = False
        img = pygame.image.load("/Users/aryatyagi/Desktop/b.png")
        img = pygame.transform.scale(img,(20,20))
        self.image = img
    def draw(self):
        screen.blit(self.image,(self.x, self.y))
    def move(self):
        if(not self.shootU): 
            self.x = p.x +45
    def shoot(self):
        if(self.shootU):
            self.y = self.y - self.speed
    def checkHit(self):
        for a in aliensB:
            if a.x +30 <= self.x +10 <= a.x +60 and a.y <= self.y <= a.y + 60 :
                aliensB.remove(a)
                self.used = True
        for a in aliensM:
            if a.x  <= self.x +10 <= a.x +70 and a.y <= self.y <= a.y + 55 :
                aliensM.remove(a)
                self.used = True
        for a in aliensT:
            if a.x  <= self.x +10 <= a.x +70 and a.y <= self.y <= a.y + 85 :
                aliensT.remove(a)
                self.used = True
class BulletA():
    def __init__(self):
        img = pygame.image.load("/Users/aryatyagi/Desktop/b.png")
        img = pygame.transform.scale(img,(20,20))
        self.image = img
        self.used = False
    def setPos(self, l):
        if(len(l) > 0):
            rand = random.randint(0, len(l) -1)
            self.x = l[rand].x
            self.y = l[rand].y
            return True
        else:
            return False
    def move(self):
        self.y += 5
    def draw(self):
        screen.blit(self.image,(self.x, self.y))
    def checkHit(self):
        if p.x <= self.x +10 <= p.x +110 and p.y <= self.y <= p.y + 110 :
            self.used = True
            p.health -=10
        
aliensT = []
aliensM = []
aliensB = []
bullets = []
bullAl = []
xcor = 10
ycor = 10
for i in range(10):
    string = "alien" + str(i)
    string = Alien(xcor,ycor,a3)
    xcor += 55
    aliensT.append(string)
ycor += 110
xcor = 20
for i in range(10):
    string = "alien" + str(i)
    string = Alien(xcor,ycor,a2)
    xcor += 55
    aliensM.append(string)
ycor += 50
xcor = 40
for i in range(10):
    string = "alien" + str(i)
    string = Alien(xcor,ycor,a1)
    xcor += 55
    aliensB.append(string)
p = Player()
b0 = BulletP()
counter = 1
bullets.append(b0)
whenShoot = 0
while True:
    
    whenShoot += 1
    if whenShoot == 50:
        i = random.randint(0,2)
        string = "al" + str(a)
        string = BulletA()
        if(i == 0 and string.setPos(aliensT)):
            string.setPos(aliensT)
            bullAl.append(string)
        elif(i == 1 and string.setPos(aliensM)):
            string.setPos(aliensM)
            bullAl.append(string)
        elif(i == 2 and string.setPos(aliensB)):
            string.setPos(aliensB)
            bullAl.append(string)
        whenShoot = 0
        
    screen.fill((0,0,0))
    #draw and move the aliens
    for a in aliensT:
        a.draw()
        a.moveH(aliensT)
        if(a.cd):
            for s in aliensT:
                s.speed = -s.speed
                s.cd = False
    for a in aliensM:
        a.draw()
        a.moveH(aliensM)
        if(a.cd):
            for s in aliensM:
                s.speed = -s.speed
                s.cd = False          
    for a in aliensB:
        a.draw()
        a.moveH(aliensB)
        if(a.cd):
            for s in aliensB:
                s.speed = -s.speed
                s.cd = False    
    #draw bullets and player
    for b in bullets:
        b.draw()
    p.draw()
    p.showHealth()
    for a in bullAl:
        a.draw()
        a.move()
        a.checkHit()
        if(a.used):
            bullAl.remove(a)
        if(a.y > 600):
            bullAl.remove(a)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                p.left = True
            elif event.key == K_RIGHT:
                p.right = True
            elif event.key == K_SPACE:
                for b in bullets:
                    b.shootU = True
                string = "b" + str(counter)
                string = BulletP()
                bullets.append(string)
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                p.left = False
            elif event.key == K_RIGHT:
                p.right = False
    for b in bullets:
        b.move()
        b.shoot()
        b.checkHit()
        if(b.used):
            bullets.remove(b)
        elif(b.y  <= -15):
            bullets.remove(b)
    p.move()

    #checking for end game
    if( p.health ==0):
        screen.fill((0,0,0))
        endfont= pygame.font.SysFont('freesans', 70)         
        msg = endfont.render("Mission Fail: GAME OVER", True, (255,255,255))         
        screen.blit(msg, (10,10))
        pygame.display.update()
        break
    
    elif(len(aliensT)  == 0 and len(aliensM)  == 0 and len(aliensB)  == 0):
        screen.fill((0,0,0))
        endfont= pygame.font.SysFont('freesans', 70)         
        msg = endfont.render("Mission Sucess: GAME OVER", True, (255,255,255))         
        screen.blit(msg, (10,10))
        pygame.display.update()
        break
    pygame.display.update()
