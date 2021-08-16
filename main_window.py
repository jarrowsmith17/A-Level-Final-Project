from tkinter import *
from tkinter import messagebox
import sqlite3	
import sys
root = Tk()
root.title("Main Window")
root.configure(background="#151E29")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
print("W:",w)
print("H:",h)
f0=Frame(width=w,height=h,bg="#151E29")
f0.pack(expand = 1)
f0.pack_propagate(0)

photo = PhotoImage(file="Login_Logo.gif")
homePhoto = PhotoImage(file="Home.gif")
#**********************************************************
def close(event):
    exit=messagebox.askokcancel("Quit?","You are about to quit. Do you want to quit?")
    if exit==True:
        root.destroy()
        
from logging_in import loggingIN
loggingIN(f0,root,photo,homePhoto)
#**********************************************************
root.geometry("%dx%d+0+0" % (w,h))
#root.overrideredirect(True)
root.focus_set()
root.bind("<Escape>",close)
root.mainloop()
