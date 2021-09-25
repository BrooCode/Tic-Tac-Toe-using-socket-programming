from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os

from pygame import Color

root = tk.Tk()
p1 = PhotoImage(file = 'assets\logo.png')
root.iconphoto(False, p1)

root.title("Tic Tac Toe")
root.geometry('500x500')
root.configure(bg='black')

load= Image.open("assets\logo1.png")
render = ImageTk.PhotoImage(load)
img = Label(root, image=render,highlightthickness = 0, bd = 0)
img.place(x=50, y=0)


tk.Label(root, text="",bg='black').grid(row=0,pady=100)
fname = tk.Label(root, text="First Player Name",font=('Helvetica', 20," italic"),foreground='white',bg='black').grid(row=2,column=1)
sname = tk.Label(root, text="Second Player Name",font=('Arial', 20," italic"),foreground='white',bg='black').grid(row=6,column=1)

e1 = tk.Entry(root, width= 60)
e2 = tk.Entry(root, width= 60)
e1.grid(row=3, column=1,pady=3)
e2.grid(row=7, column=1,pady=5)

def player1():
    p1 = e1.get()    


btn1 = Button(root, text="Lets Play", command=player1,height= 2, width=10,foreground='red')
btn1.grid(row=8,column=1)


root.mainloop()


