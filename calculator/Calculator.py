#Calculator

from tkinter import *
root = Tk()
root.title("Calculator")

#creates an input box
e = Entry(root, width=35, fg="Pink", bg="White", borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonclick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#clear button function
def buttonClear():
    e.delete(0, END)

#add button function
def buttonAdd():
    firstNumber = e.get()
    global math
    math = "addition"
    global f_num
    f_num = int(firstNumber)
    e.delete(0, END)

#equal button function
def buttonEqual():
    secondNumber = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, f_num + int(secondNumber))

    if math == "subtraction":
         e.insert(0, f_num - int(secondNumber))

    if math == "multiplication":
         e.insert(0, f_num * int(secondNumber))

    if math == "division":
         e.insert(0, f_num / int(secondNumber))

#subtraction button function
def buttonSubtract():
    firstNumber = e.get()
    global math
    math = "subtraction"
    global f_num
    f_num = int(firstNumber)
    e.delete(0, END)

#multiplication button function
def buttonMultiply():
    firstNumber = e.get()
    global math
    math = "multiplication"
    global f_num
    f_num = int(firstNumber)
    e.delete(0, END)

#division button function
def buttonDivide():
    firstNumber = e.get()
    global math
    math = "division"
    global f_num
    f_num = int(firstNumber)
    e.delete(0, END)

#define the buttons
Button1 = Button(root, text="1", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(1))
Button2 = Button(root, text="2", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(2))
Button3 = Button(root, text="3", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(3))
Button4 = Button(root, text="4", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(4))
Button5 = Button(root, text="5", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(5))
Button6 = Button(root, text="6", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(6))
Button7 = Button(root, text="7", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(7))
Button8 = Button(root, text="8", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(8))
Button9 = Button(root, text="9", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(9))
Button0 = Button(root, text="0", padx=40, pady=20, fg="Hotpink", command= lambda: buttonclick(0))
Buttonadd = Button(root, text="+", padx=40, pady=20, fg="Pink", command=buttonAdd)
Buttonequal = Button(root, text="=", padx=40, pady=20, fg="Pink", command=buttonEqual)
Buttonclear = Button(root, text="Clear", padx=30, pady=19, fg="Pink", command=buttonClear)
Buttonsub = Button(root, text="-", padx=40, pady=20, fg="Pink", command=buttonSubtract)
Buttonmult = Button(root, text="*", padx=40, pady=20, fg="Pink", command=buttonMultiply)
Buttondiv = Button(root, text="/", padx=40, pady= 20, fg="Pink", command=buttonDivide)


#put the buttons on the screen
Button1.grid(row=3, column=0)
Button2.grid(row=3, column=1)
Button3.grid(row=3, column=2)

Button4.grid(row=2, column=0)
Button5.grid(row=2, column=1)
Button6.grid(row=2, column=2)

Button7.grid(row=1, column=0)
Button8.grid(row=1, column=1)
Button9.grid(row=1, column=2)

Buttonadd.grid(row=4, column=0)
Buttonequal.grid(row=5, column=1)
Buttonclear.grid(row=5, column=2)
Buttonsub.grid(row=5, column=0)
Buttonmult.grid(row=4, column=1)
Buttondiv.grid(row=4, column=2)

root.mainloop()
