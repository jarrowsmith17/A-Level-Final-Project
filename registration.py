from tkinter import *
import sqlite3
def reg(f0,root,homePhoto):
    f5=Frame(f0, bg="#151E29",width=400,height=600)
    f5.pack(expand = 1)
    f5.pack_propagate(0)
    def errorMsg():
        messagebox.showwarning("Invalid Details","Fill in the information correctly")
    def userTaken():
        messagebox.showwarning("Username Taken","The username entered has been taken")
    def passMatchError():
        messagebox.showwarning("Passwords Don't Match","The passwords entered do not match.") 
    def tooSmall():
        messagebox.showwarning("Password is too short","The password entered isn't strong enough!") 
    def success():
        signedUser=User.get()
        f5.pack_forget()
        from homepage import homepage
        homepage(f0,root,homePhoto,signedUser)

    def checkUsername():
        Username=User.get() ##Gets the username from the entry widget
        if Username == "":
            errorMsg() ##Runs an error messagebox
        else:
            db_conn = sqlite3.connect('Coursework.db') ##Connects to the database

            with db_conn:
                
                cur = db_conn.cursor()    
                cur.execute("SELECT Username FROM Users WHERE Username = ?",(Username,))

                row = cur.fetchall() ##Searches for all instances
                if not row:
                    checkPassword() ##Runs the password checking function.
                for a in row:
                    userTaken() ##Runs a messagebox saying the username is taken
    def checkPassword():
        p1=Pass.get()
        p2=confirmPass.get()
        if p1 == p2:
            print("Matching")
            passw=len(p1)
            if passw<=7:
                tooSmall()
            else:
                namesEntered()
        else:
            passMatchError()

    def namesEntered():
        fname=Fore.get()
        sname=Sur.get()
        cGroup=classGroup.get()
        if fname == "" or sname == "" or cGroup == "":
            errorMsg()
        else:
            enterSystem()    
            
    def enterSystem():
        Username=User.get()
        Password=Pass.get()
        Forename=Fore.get()
        Surname=Sur.get()
        Class=classGroup.get()
        accType=v.get()
        if accType==1:
            accType="Student"
        else:
            accType="Teacher"
        print (accType)
        db_conn = sqlite3.connect('Coursework.db')

        theCursor  = db_conn.cursor()

        db_conn.execute("INSERT INTO Users(Username,Password,Forename,Surname,Class,Account_Type)values(?,?,?,?,?,?)",
                            (Username,Password,Forename,Surname,Class,accType))
        db_conn.commit()


        db_conn.close()
        checkSuccess()
    def checkSuccess():
        
        Username=User.get()
        db_conn = sqlite3.connect('Coursework.db')

        with db_conn:
            
            cur = db_conn.cursor()    
            cur.execute("SELECT Username FROM Users WHERE Username = ?",(Username,))

            row = cur.fetchall()
            if not row:
                errorMsg()
                
            for a in row:
                success()
                    
        db_conn.close()
        success()   

    #*********************************
    title=Label(f5, text="Registration", fg="white",bg="#151E29",font=(None,20))

    intro=Label(f5,font=(None,10), text="""
    Welcome to the registration form. To enjoy
    a personalised experience it is required that
    users create an account. Please fill in the
    form below to register, once registered you
    will be logged in.""",fg="white",bg="#151E29")

    Lbl_1=Label(f5, text="Username",fg="white",bg="#151E29",font=(None,12))
    User = Entry(f5,width=40, justify="center",fg="white",bg="#1B2737",bd=0)

    Lbl_2=Label(f5,text="Password",fg="white",bg="#151E29",font=(None,12))
    Pass=Entry(f5,show="*",width=40, justify="center",fg="white",bg="#1B2737",bd=0)

    Lbl_3=Label(f5,text="Confirm Password",fg="white",bg="#151E29",font=(None,12))
    confirmPass=Entry(f5,show="*",width=40, justify="center",fg="white",bg="#1B2737",bd=0)

    Lbl_4=Label(f5,text="Forename",fg="white",bg="#151E29",font=(None,12))
    Fore=Entry(f5,width=40, justify="center",fg="white",bg="#1B2737",bd=0)

    Lbl_5=Label(f5,text="Surname",fg="white",bg="#151E29",font=(None,12))
    Sur=Entry(f5,width=40, justify="center",fg="white",bg="#1B2737",bd=0)
    
    Lbl_6=Label(f5,text="Class",fg="white",bg="#151E29",font=(None,12))
    classGroup=Entry(f5,width=40, justify="center",fg="white",bg="#1B2737",bd=0)

    v = IntVar()

    r1 = Radiobutton(f5, text="Student", variable=v, value=1,fg="orange",bg="#1B2737",font=(None,12),activebackground="#1B2737",activeforeground="black")
    r2 = Radiobutton(f5, text="Teacher", variable=v, value=2,fg="orange",bg="#1B2737",font=(None,12),activebackground="#1B2737",activeforeground="black")
    
    blank_1=Label(f5,text="",fg="white",bg="#151E29",font=(None,12))

    BT_1=Button(f5, text="Submit", command=checkUsername,width=20,fg="white",bg="#1B2737",bd=0, anchor='center',font=(None,12))
    #****************************************
    title.pack()
    intro.pack()
    Lbl_1.pack()
    User.pack(ipady=5)
    Lbl_2.pack()
    Pass.pack(ipady=5)
    Lbl_3.pack()
    confirmPass.pack(ipady=5)
    Lbl_4.pack()
    Fore.pack(ipady=5)
    Lbl_5.pack()
    Sur.pack(ipady=5)
    Lbl_6.pack()
    classGroup.pack(ipady=5)
    r1.pack(ipady=3)
    r2.pack()
    blank_1.pack()
    BT_1.pack(ipady=3)

