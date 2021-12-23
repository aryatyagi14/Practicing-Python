from tkinter import *
import time
master = Tk()
master.title("Information")
l1 = Label(master, text = "Enter Countdown Time").grid(row = 0, column = 0)
e1 = Entry(master)
e1.grid(row = 0, column = 1)
def startCd():
    num = int(e1.get())
    for i in range(num):
        print(num)
        num = num - 1    
        time.sleep(1)
def reset():
    e1.delete(0, END)
b1 = Button(master, text = "START", command = startCd).grid(row =1, column = 0)
b2 = Button(master, text = "RESET", command = reset).grid(row = 1, column =1)
#2 buttons number guessing or coin toss
#number= entry where you enter your guess
#2 labels = guess and correct or not correct
