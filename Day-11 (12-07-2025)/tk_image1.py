from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Manipulation")

img_photo = ImageTk.PhotoImage(Image.open("goodmorning5.jpg"))
lbl_photo = Label(root, image=img_photo)
lbl_photo.pack()

root.mainloop()

