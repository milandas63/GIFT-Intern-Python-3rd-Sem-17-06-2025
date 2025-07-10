from tkinter import *
import tkinter.font as tkf

root = Tk()
root.title("L O G I N")
root.iconbitmap("login.ico")
root.geometry("500x250")

lblTitle = Label(root, text="   Login   ", bg="blue", fg="white", font=tkf.Font(family="Arial", size="20"))
lblTitle.pack()

Label(root,text="").pack()
Label(root,text="").pack()

lblUser = Label(root, text="Username: ", font=tkf.Font(family="Arial",size="15"))
lblUser.pack()

tfUser = Entry(root, text="", font=tkf.Font(family="Arial",size="12"))
tfUser.pack()

Label(root,text="").pack()

lblPass = Label(root, text="Password: ", font=tkf.Font(family="Arial",size="15"))
lblPass.pack()

tfPass = Entry(root, text="", font=tkf.Font(family="Arial",size="12"))
tfPass.pack()

Label(root,text="").pack()
Label(root,text="").pack()

btnSubmit = Button(root, text=" Submit ", font=tkf.Font(family="Arial",size="15"))
btnSubmit.pack()

root.mainloop()
