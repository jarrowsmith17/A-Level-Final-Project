import sqlite3
from tkinter import *
import sys
from tkinter import messagebox
root=Tk()

signedUser="ADMIN"
w,h=root.winfo_screenwidth(),root.winfo_screenheight()

change_password_form=Frame(root,width=w,height=h-50,bg="yellow")
change_password_form.pack(expand=1)
change_password_form.pack_propagate(0)

def change_password(signedUser): 
    password = passwordEntry.get()
    NewPass = NewpasswordEntry.get()
    NewPassCheck = NewpasswordEntry2.get()

    db_conn = sqlite3.connect('Coursework.db')

    with db_conn:
        
        cur = db_conn.cursor()    
        cur.execute("SELECT Password FROM Users WHERE Username = ?",(signedUser,))
        
        row = cur.fetchone()
        print(row)
        row = str(row[0])
        if (row == password and NewPass == NewPassCheck and len(NewPass)>7):
            print ("yes")

            db_conn = sqlite3.connect('Coursework.db')
            with db_conn:
                cur=db_conn.cursor()
                cur.execute("""UPDATE Users
                        SET Password = ?
                        WHERE Username = ?""",[NewPass,signedUser])
            db_conn.close()
            messagebox.showinfo("Success","Password has been updated.")
        else:
            messagebox.showwarning("Failed","Error with the information provided. Make sure the password is correct and the new password is long enough. Passwords may not match.")
            print("no")
    db_conn.close()


passwordLabel=Label(change_password_form,text="Password: ").pack()
passwordEntry=Entry(change_password_form,show="*")
passwordEntry.pack()

NewpasswordLabel=Label(change_password_form,text="New Password: ").pack()
NewpasswordEntry=Entry(change_password_form,show="*")
NewpasswordEntry.pack()

NewpasswordLabel2=Label(change_password_form,text="New Password Again: ").pack()
NewpasswordEntry2=Entry(change_password_form,show="*")
NewpasswordEntry2.pack()

Button(change_password_form,text="Enter",command=lambda:change_password(signedUser)).pack()
root.mainloop()
