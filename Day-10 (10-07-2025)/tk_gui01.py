from tkinter import *
import tkinter.font as tkFont

root = Tk()
root.title("My First Desktop Program")
root.iconbitmap("title.ico")
root.geometry("800x500")

lblHello = Label(root, text=" Hello World ", bg="yellow", fg="blue", 
                 font=tkFont.Font(family="Arial", size=35))
lblHello.pack()

root.mainloop()
