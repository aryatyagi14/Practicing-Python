from tkinter import *
master = Tk()
master.title("Information")
##
##e1 = Entry(master)
##e1.insert(END, "Enter Your Name:")
##e1.grid(row = 0, column = 1)
##
##def printtxt():
##    print("NAME : "+e1.get())
##def clear():
##    e1.delete(0,END)
##l1 = Label(master, text = "NAME").grid(row = 0, column = 0)
##b1 = Button(master, text = "SHOW Name", command = printtxt).grid(row = 1, column =0)
##b2 = Button(master, text = "Clear", command = clear).grid(row = 1, column = 1)
#b1 = Button(master, text = "Click To Close", command = master.destroy)
#b1.grid(row =1, column = 0)
l1 = Label(master, text = "First Name:").grid(row = 0, column = 0)
e1 = Entry(master)
e1.grid(row = 0, column = 1)
l2 = Label(master, text = "Last Name:").grid(row = 1, column =0)
e2 = Entry(master)
e2.grid(row = 1, column = 1)
l3 = Label(master, text = "Address:").grid(row =2, column = 0)
e3 = Entry(master)
e3.grid(row = 2, column = 1)
l4 = Label(master, text = "Phone Number:").grid(row =3, column = 0)
e4 = Entry(master)
e4.grid(row = 3, column = 1)
b1 = Button(master, text = "QUIT", command = master.destroy).grid(row = 4, column = 1)
def printInfo():
    f = open("tkinterTextFile.txt", "w+")
    name = "Name: " + e1.get()+ " "+ e2.get()
    f.write(name+ "\n")
    addy = "Address: "+ e3.get()
    f.write(addy+ "\n")
    phone = "Phone #: "+ e4.get()
    f.write(phone+ "\n") 
##    print("Name: " , e1.get(), " ", e2.get())
##    print("Address: ", e3.get())
##    print("Phone #: ", e4.get())
    f.close()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    
b2 = Button(master, text = "Enter", command = printInfo).grid(row = 4, column = 0)



mainloop()

