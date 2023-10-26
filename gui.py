import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import getpass
from tkinter import *

from main import init
from main import update
from main import view


root = Tk()
root.title('TATA Motors Database')
# root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x300")


my_label = Label(root, text="WELCOME", font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

my_button = Button(root, text="INITIALIZE DATABASE", font=("Helvetica", 18), command=init.main)
my_button.pack(pady=20)
my_button = Button(root, text="INITIALIZE DATABASE", font=("Helvetica", 18), command=init.main)
my_button.pack(pady=20)
my_button = Button(root, text="INITIALIZE DATABASE", font=("Helvetica", 18), command=init.main)
my_button.pack(pady=20)



root.mainloop()
