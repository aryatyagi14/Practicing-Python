from tkinter import *
import random
master = Tk()
master.title("Choose A Game")
global score
score = 0
def heads():
    global userM
    userM = "heads"
def tails():
    global userM
    userM = "tails"
def enter():
    global userM
    global score
    compM = ""
    rand = random.randint(0,1)
    if rand  == 1:
        compM = "heads"
    else:
        compM = "tails"
    if userM == compM:
        score+= 1
        print("You are correct, you and the computer put ", userM)
        print("Score: ", score)
    else:
        print("You didnt put the same thing as the computer...")
        
def guess():
    guess = int(e1.get())
    e1.delete(0, END)
    if(guess == rand):
        print("You are Correct!!")
    elif(guess > rand):
        print("Your Guess is too HIGH.")
    elif(guess < rand):
        print("Your Guess is too LOW.")
def openCoinToss():
    masterCT = Tk()
    masterCT.title("Coin Toss")
    l1 = Label(masterCT, text ="Choose One: ").grid(row =0, column =0)
    headsB = Button(masterCT, text = "Heads", command=heads).grid(row=0,column=1)
    tailsB = Button(masterCT,text="Tails",command = tails).grid(row=0,column=2)
    enterB = Button(masterCT, text="Enter:", command = enter).grid(row =1, column=0)
def openGuessingGame():
    global rand
    global e1
    masterGG = Tk()
    masterGG.title("Number Guessing Game")
    l1= Label(masterGG,text="Enter Guess :").grid(row=0, column=0)
    rand = random.randint(1,100)
    e1 = Entry(masterGG)
    e1.grid(row =0, column = 1)
##    print(e1.get())
    enter=Button(masterGG,text="Enter",command=guess).grid(row=1,column=1)
ctB = Button(master, text = "Coin Toss", command = openCoinToss).grid(row = 0, column = 0)
gbB = Button(master, text = "Number Guessing Game", command = openGuessingGame).grid(row=0,column =1)
