from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
def loggingIN(f0,root,photo,homePhoto):
    f1=Frame(f0,width=1000, height=400,bg="#151E29")
    f1.pack(expand = 1)
    f1.pack_propagate(0)
    f2=Frame(f1, bg="#151E29", width= 500,height=400)
    f2.pack(expand = 1, side=LEFT)
    f2.pack_propagate(0)
    f3=Frame(f1, bg="#151E29", width= 500,height=400)
    f3.pack(expand = 1, side=RIGHT)
    f3.pack_propagate(0)
    f4=Frame(f3, bg="#151E29", width= 400,height=225)
    f4.pack(expand = 1)
    f4.pack_propagate(0)
    l1 = Label(f2, image = photo, width=250, height=250,bd=0)
    l1.pack(expand = 1)

    #**********************************************************

    def errorMsg():
        messagebox.showerror("Invalid Details","The username or password is incorrect")
        
    def success():
        signedUser=user.get() ##Used to keep the username of the signed in user saved throughout the program.
        f1.pack_forget() ##Used to remove the frame and its contents from the program

        from homepage import homepage ##Connects to the homepage file and imports the homepage function.
        homepage(f0,root,homePhoto,signedUser) ##Runs the homepage function and passes all the variables
                                               ##needed through with it.
    def checkUsername():
        logUser=user.get()
        db_conn = sqlite3.connect('Coursework.db')

        with db_conn:
            
            cur = db_conn.cursor()    
            cur.execute("SELECT Username FROM Users WHERE Username = ?",(logUser,))

            row = cur.fetchall()
            if not row:
                errorMsg()
                
            for a in row:
                checkPassword()
                    
        db_conn.close()
        
    def checkPassword():
        
        logUser=user.get()
        logPass=password.get()
        db_conn = sqlite3.connect('Coursework.db')

        with db_conn:
            
            cur = db_conn.cursor()    
            cur.execute("SELECT Password FROM Users WHERE Username = ?",(logUser,))

            row = cur.fetchone()
     
            for a in row:
                if logPass == a:
                    success()
                else:
                    errorMsg()
                    
        db_conn.close()
        
    def register():
        f1.pack_forget()
        from registration import reg
        reg(f0,root,homePhoto)

    #****************************************************

    Lbl_2=Label(f4, text="Username:", font=(None,20),fg="white",bg="#151E29")
    user=Entry(f4, justify="center",fg="white",bg="#1B2737",bd=0,width=40)
    Lbl_3=Label(f4, text="Password:", font=(None,20),fg="white",bg="#151E29")
    password=Entry(f4, show="*", justify="center",fg="white",bg="#1B2737",bd=0,width=40)
    BT_1 = Button(f4, text="Submit",  command=checkUsername, font=(None,12), width=20, fg="white", bg="#1B2737", bd=0, anchor='center')
    BT_2 = Button(f4, text="Register",font=(None,12), command=register, width=20, fg="white", bg="#1B2737", bd=0, anchor='center')
    blabel=Label(f4,text="",bg="#151E29")
    blabel_1=Label(f4,text="",bg="#151E29")

    Lbl_2.pack()
    user.pack(ipady=5)
    Lbl_3.pack()
    password.pack(ipady=5)
    blabel.pack()
    BT_1.pack()
    blabel_1.pack()
    BT_2.pack()
