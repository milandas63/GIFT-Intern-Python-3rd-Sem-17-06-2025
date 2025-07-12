from tkinter import *
import tkinter.font as tkf

root = Tk()
root.title("Simple Calculator")
var1 = 0
var2 = 0
result = IntVar()

display = Entry(root, text="", font=tkf.Font(family="Arial", size=12))
display.grid(row=0, column=0, columnspan=3)

def Show(num):
    previous = display.get()
    display.insert(len(previous), num)
    return

def Plus():
    var1 = int(display.get())
    print("+",var1)
    display.delete(0,END)
    return

def Clear():
    display.delete(0, END)
    var1 = 0
    var2 = 0
    return

def Equal():
    var2 = int(display.get())
    print(var1,var2)
    result = (int(var1) + int(var2))
    display.delete(0,END)
    display.insert(0,result)
    return

button_7 = Button(root, text="7", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(7))
button_8 = Button(root, text="8", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(8))
button_9 = Button(root, text="9", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(9))
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4 = Button(root, text="4", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(4))
button_5 = Button(root, text="5", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(5))
button_6 = Button(root, text="6", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(6))
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1 = Button(root, text="1", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(1))
button_2 = Button(root, text="2", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(2))
button_3 = Button(root, text="3", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(3))
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0 = Button(root, text="0",    padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Show(0))
button_plus = Button(root, text="+", padx=50, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Plus())
button_0.grid(row=4, column=0)
button_plus.grid(row=4, column=1, columnspan=2)

button_c = Button(root, text="C", padx=20, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Clear())
button_equal = Button(root, text="=", padx=50, pady=20, font=tkf.Font(family="Arial", size=12), command=lambda: Equal())
button_c.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
