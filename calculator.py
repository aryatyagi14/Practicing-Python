from tkinter import *
master = Tk()
master.title("Calculator")
string = ""
op = ""
global e1
e1 = Entry(master)
e1.grid(row = 0, column = 1)

def one():
    global string
    string += "1"
def two():
    global string
    string+="2"
def three():
    global string
    string+="3"
def four():
    global string
    string+="4"
def five():
    global string
    string+="5"
def six():
    global string
    string+="6"
def seven():
    global string
    string+="7"
def eight():
    global string
    string+="8"
def nine():
    global string
    string += "9"
def minus():
    global string
    global op
    op = "minus"
    string+="-"
def add():
    global string
    global op
    op = "add"
    string+="+"
def multiply():
    global string
    global op
    op = "multiply"
    string+="*"
def divide():
    global string
    global op
    op = "divide"
    string+="/"
def e():
    global string
    global e1
    print(string)
    ans = 0
    indexOp = -1
    if op == "multiply":
        indexOp = string.index("*")
    elif op == "divide":
        indexOp = string.index("/")
    elif op == "add":
        indexOp = string.index("+")
    elif op == "minus":
        indexOp = string.index("-")
    num1 = int(string[0:indexOp])
    num2 = int(string[indexOp+1:])
    if op == "multiply":
        ans = num1*num2
    elif op == "divide":
        ans = num1/num2
    elif op == "add":
        ans = num1+num2
    elif op == "minus":
        ans = num1-num2
    e1.insert(END, ans)
    string = ""
def clear():
    global e1
    e1.delete(0, END)
l1 = Label(master, text = "ANS: ").grid(row =0, column = 0)
b1 = Button(master, text = "  1  ", command = one).grid(row = 1, column = 0)
b2 = Button(master, text = "  2  ", command = two).grid(row = 1, column = 1)
b3 = Button(master, text = "  3  ", command = three).grid(row = 1, column = 2)
b4 = Button(master, text = "  4  ", command = four).grid(row = 2, column = 0)
b5 = Button(master, text = "  5  ", command = five).grid(row = 2, column = 1)
b6 = Button(master, text = "  6  ", command = six).grid(row = 2, column = 2)
b7 = Button(master, text = "  7  ", command = seven).grid(row = 3, column = 0)
b8 = Button(master, text = "  8  ", command = eight).grid(row = 3, column = 1)
b9 = Button(master, text = "  9  ", command = nine).grid(row = 3, column = 2)
bplus = Button(master, text = "  +  ", command = add).grid(row = 1, column = 4)
bminus = Button(master, text = "  -  ", command = minus).grid(row = 2, column = 4)
bmult = Button(master, text = "  *  ", command = multiply).grid(row = 3, column = 4)
bdivide = Button(master, text = "  /  ", command = divide).grid(row = 4, column = 4)
bequals = Button(master, text = "  =  ", command = e).grid(row =4, column = 1)
bclear = Button(master, text="CLEAR", command= clear).grid(row = 4,column =0)


