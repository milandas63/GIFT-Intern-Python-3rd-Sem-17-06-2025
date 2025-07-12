from tkinter import *
import tkinter.font as tkf

def extract():
    name = ent_user.get()
    print(name)
    lbl_result.config(text="Username: "+name)
    return

root = Tk()
root.title("Location Defined Login")

lbl_title = Label(root, text=" L O G I N ", bg="cyan", fg="blue", font=tkf.Font(family="Arial", size="20"))
lbl_title.grid(row=0, column=0, columnspan=4)

Label(root, text="").grid(row=1, column=0, columnspan=4)
Label(root, text="").grid(row=2, column=0, columnspan=4)
Label(root, text="").grid(row=3, column=0, columnspan=4)

lbl_user = Label(root, text="  Username: ")
lbl_user.grid(row=4, column=0, columnspan=4)

ent_user = Entry(root, font=tkf.Font(family="Arial", size=14))
ent_user.grid(row=5, column=0, columnspan=4)

Label(root, text="").grid(row=6, column=0, columnspan=4)

lbl_pw = Label(root, text="  Password: ")
lbl_pw.grid(row=7, column=0, columnspan=4)

ent_pw = Entry(root, font=tkf.Font(family="Arial", size=14))
ent_pw.grid(row=8, column=0, columnspan=4)

Label(root, text="").grid(row=9, column=0, columnspan=4)
Label(root, text="").grid(row=10, column=0, columnspan=4)
Label(root, text="").grid(row=11, column=0, columnspan=4)

btn_submit = Button(root, text="Submit", command=extract)
btn_submit.grid(row=12, column=0, columnspan=2)

btn_exit = Button(root, text="Exit")
btn_exit.grid(row=12, column=2, columnspan=2)

Label(root, text="").grid(row=13, column=0, columnspan=4)
Label(root, text="").grid(row=14, column=0, columnspan=4)

lbl_result = Label(root, text=" ")
lbl_result.grid(row=15, column=0, columnspan=4)

root.mainloop()
