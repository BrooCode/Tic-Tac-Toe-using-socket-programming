from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import json
import os
import time
from multiprocessing import Process

from pygame import Color

root = tk.Tk()
p1 = PhotoImage(file = 'assets\logo.png')
root.iconphoto(False, p1)

root.title("Tic Tac Toe")
root.geometry('400x500')
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

# def threadFunction():
#     os.system('python 1.py')
#     time.sleep(1)
#     os.system('python 2.py')
#     root.destroy()

def start():
    os.system('python 1.py')
    root.destroy

def player1():
    p1 = e1.get() 
    with open("data.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["player1"] = p1

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate() 
def player2():
    p1 = e2.get() 
    with open("data.json", "r+") as jsonFile:
        data = json.load(jsonFile)

        data["player2"] = p1

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()        
    

btn1 = Button(root, text="Player 1 Enter Lobby", command=player1,height= 2, width=20,foreground='red')
btn1.grid(row=4,column=1)

btn2 = Button(root, text="Player 2 Enter Lobby", command=player2,height= 2, width=20,foreground='red')
btn2.grid(row=8,column=1)

btn3 = Button(root, text="Lets Play", command=start,height= 2, width=10,foreground='red')
btn3.grid(row=10,column=1)

root.mainloop()


