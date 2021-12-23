import pygame
import random
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Balloon Game")
score = 0
speed = 1
end = False
pop = pygame.mixer.Sound("/Users/aryatyagi/Desktop/bp.wav")
pop.set_volume(0.1)
class Balloon():
    def __init__(self):
        self.image = pygame.image.load("/Users/aryatyagi/Desktop/rb.png")
        self.image = pygame.transform.scale(self.image,(200,170))
        self.x = random.randint(30,610)
        self.y = 510
        self.color = (255,0,0)
        self.lcolor = (0,0,0)
        self.letter = chr(random.randint(97,122))
    def draw(self):
        screen.blit(self.image,(self.x-95, self.y-70))
        font= pygame.font.SysFont('freesans', 32)         
        msg = font.render(self.letter, True, self.lcolor)         
        screen.blit(msg, (self.x,self.y))
    def move(self):
        self.y -= speed

b0 = Balloon()
counter = 1
balloons = []
balloons.append(b0)
while True:
    screen.fill((255,255,255))
    font= pygame.font.SysFont('freesans', 32)         
    msg = font.render("Score: " + str(score), True, (0,0,0))         
    screen.blit(msg, (10,10))
    for balloon in balloons:
        balloon.draw()
        balloon.move()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            for balloon in balloons:
                if score%2 == 0 and score != 0:
                    speed += 1
                if event.key == ord(balloon.letter):
                    pop.play()
                    balloons.remove(balloon)
                    score += 1
                    break
                else:
                    score -= 1
                
            string = "b"+str(counter)
            counter+= 1
            string = Balloon()
            balloons.append(string)
    for ball in balloons:
        if ball.y +40 <= 0:
            end = True
    if(end):
        break
    pygame.display.update()
screen.fill((0,0,0))
font= pygame.font.SysFont('freesans', 32)         
msg = font.render("Score: " + str(score), True, (255,255,255))         
screen.blit(msg, (10,10))
font= pygame.font.SysFont('freesans', 100)         
msg = font.render("GAME OVER" , True, (255,255,255))         
screen.blit(msg, (100,100))
pygame.display.update()






