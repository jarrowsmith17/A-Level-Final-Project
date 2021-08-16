from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
from operator import itemgetter
def homepage(f0,root,homePhoto,signedUser):
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
#********************************************************
    main=Frame(f0,width=w,height=h,bg="red")
    main.pack(expand = 1)
    main.pack_propagate(0)
#********************************************************    
    nav=Frame(main,width=w,height=50,bg='#151E29')
    nav.pack(expand=1)
    nav.pack_propagate(0)

    homeF=Frame(nav,width=150,height=50,bg="#151E29")
    homeF.pack(expand=0,fill=BOTH,side=LEFT)
    homeF.pack_propagate(0)
    
    lUser=Frame(nav,width=150,height=50,bg="#151E29")
    lUser.pack(expand=0,fill=BOTH,side=RIGHT)
    lUser.pack_propagate(0)
#********************************************************
    bottom=Frame(main,width=w,height=h-50,bg='#151E29')
    bottom.pack(expand=1)
    bottom.pack_propagate(0)
#********************************************************
    def questions():
        print("Questions")
    def backH(main):
        main.pack_forget()
        from homepage import homepage
        homepage(f0,root,homePhoto,signedUser)
        
    def account(bottom):
        def close():
            exit=messagebox.askokcancel("Quit?","You are about to quit. Do you want to quit?")
            if exit==True:
                root.destroy()
        def CHANGE_password(signedUser,acc_Frame,main):
            acc_Frame.pack_forget()
            w,h=root.winfo_screenwidth(),root.winfo_screenheight()
            print("change password")
            change_password_form=Frame(main,width=w,height=h-50,bg="yellow")
            change_password_form.pack(expand=1)
            change_password_form.pack_propagate(0)

            def change_password(signedUser,change_password_form): 
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
                        account(change_password_form)
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

            Button(change_password_form,text="Enter",command=lambda:change_password(signedUser,change_password_form)).pack()
            Button(change_password_form,text="Back",command=lambda:account(change_password_form)).pack()


              
        bottom.pack_forget()
        acc_Frame=Frame(main,width=w,height=h-50,bg="#28394F")
        acc_Frame.pack(expand=1)
        acc_Frame.pack_propagate(0)
        
        acc_format_Left=Frame(acc_Frame,width=w/2,height=h/2,bg="#28394F")
        acc_format_Left.pack(expand=0,side=LEFT)
        acc_format_Left.pack_propagate(0)
        
        acc_format_Right=Frame(acc_Frame,width=w/2,height=h-80,bg="#28394F")
        acc_format_Right.pack(expand=0,fill=BOTH,side=RIGHT)
        acc_format_Right.pack_propagate(0)
    
        db_conn = sqlite3.connect('Coursework.db')

        with db_conn:

            curs = db_conn.cursor()    
            curs.execute("""SELECT Answered_Questions, Correct_Answers
                            FROM Users
                            WHERE Username = ?
                            ORDER BY Correct_Answers asc
                        """,(signedUser,))

            row = curs.fetchall()
            userStats=row[0]
            print (userStats)
            percent=format((userStats[1]/userStats[0])*100,'.1f')
            print (percent)
            
            Label(acc_format_Left,text=signedUser,font=(None,60),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text="STATS",font=(None,30),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text="Correct Questions",font=(None,20),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text=userStats[1],font=(None,15),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text="Number of Questions Answered",font=(None,20),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text=userStats[0],font=(None,15),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text="Percent",font=(None,20),fg="white",bg="#28394F").pack()
            Label(acc_format_Left,text=str(percent)+"%",font=(None,15),fg="white",bg="#28394F").pack()
            Button(acc_format_Right,text="Change Password",command=lambda:CHANGE_password(signedUser,acc_Frame,main),font=(None,15),fg="white",bg="#28394F",width=50,height=20,bd=0).pack()
            Button(acc_format_Right,text="Quit",command=lambda:close(),font=(None,15),fg="white",bg="#28394F",width=50,height=20,bd=0).pack()
    
#*******************************************************    
    results=Frame(bottom,width=w/4,height=h-50,bg="#28394F")
    results.pack(expand=0,fill=BOTH,side=LEFT)
    results.pack_propagate(0)
    
    leaderboard=Frame(bottom,width=w/4,height=h-80,bg="#213041")
    leaderboard.pack(expand=0,fill=BOTH,side=RIGHT)
    leaderboard.pack_propagate(0)

    revision=Frame(bottom,width=w/2,height=h-50,bg="#151E29")
    revision.pack(expand=0,fill=BOTH)
    revision.pack_propagate(0)

#************************NavBar**************************
    l1 = Button(homeF,command=lambda:backH(main),bd=0,bg="#151E29")
    l1.config(image=homePhoto)
    l1.pack(expand = 1)
    loggedUser = Label(lUser, text="User: "+signedUser,fg="white",bg="#151E29",font=(None,12)).pack(ipady=10)
#**********************Leaderboard***********************
    leaderboard_list = []
    db_conn = sqlite3.connect('Coursework.db')

    with db_conn:

        curs = db_conn.cursor()    
        curs.execute("""SELECT Username, Answered_Questions, Correct_Answers
                        FROM Users
                        WHERE Answered_Questions > 0
                        ORDER BY Correct_Answers asc
                    """,)

        rows = curs.fetchall()
        x=0
        for a in rows:                                                                                      
                leaderboard_list.insert(x,a)
                x+=1

    db_conn.close()

    ind=0
    leaderboard_rank = []
    while len(leaderboard_list)!= ind:
        user_details=list((leaderboard_list[ind]))
        maths = format((user_details[2]/user_details[1])*100,'.1f')
        user_details.append(float(maths))
        user_details = tuple(user_details)
        leaderboard_rank.insert(ind,user_details)
        ind+=1

    leaderboard_rank.sort(key=itemgetter(3), reverse=True)

    first=leaderboard_rank[0]	
    second=leaderboard_rank[1]
    third=leaderboard_rank[2]
    fourth=leaderboard_rank[3]
    fifth=leaderboard_rank[4]
    sixth=leaderboard_rank[5]
    seventh=leaderboard_rank[6]

    Label(leaderboard, text="Leaderboard",fg="White", bg ="#213041",font=(None,11)).pack()
    lCardHeight=((h)/8)
    #*************************************************
    first_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F", highlightcolor="white")
    first_place_Frame.pack(expand = 1)
    first_place_Frame.pack_propagate(0)

    Label(first_place_Frame, text="1st Place",fg="White", bg ="#28394F").pack()
    Label(first_place_Frame, text=first[0],fg="White", bg ="#28394F").pack()
    Label(first_place_Frame, text="Answered Questions: "+str(first[1]),fg="White", bg ="#28394F").pack()
    Label(first_place_Frame, text="Correct Answers: "+str(first[2]),fg="White", bg ="#28394F").pack()
    Label(first_place_Frame, text="Percent Correct: "+str(first[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    sec_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    sec_place_Frame.pack(expand = 1)
    sec_place_Frame.pack_propagate(0)
    
    Label(sec_place_Frame, text="2nd Place",fg="White", bg ="#28394F").pack()
    Label(sec_place_Frame, text=second[0],fg="White", bg ="#28394F").pack()
    Label(sec_place_Frame, text="Answered Questions: "+str(second[1]),fg="White", bg ="#28394F").pack()
    Label(sec_place_Frame, text="Correct Answers: "+str(second[2]),fg="White", bg ="#28394F").pack()
    Label(sec_place_Frame, text="Percent Correct: "+str(second[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    third_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    third_place_Frame.pack(expand = 1)
    third_place_Frame.pack_propagate(0)

    Label(third_place_Frame, text="3rd Place",fg="White", bg ="#28394F").pack()
    Label(third_place_Frame, text=third[0],fg="White", bg ="#28394F").pack()
    Label(third_place_Frame, text="Answered Questions: "+str(third[1]),fg="White", bg ="#28394F").pack()
    Label(third_place_Frame, text="Correct Answers: "+str(third[2]),fg="White", bg ="#28394F").pack()
    Label(third_place_Frame, text="Percent Correct: "+str(third[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    fourth_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    fourth_place_Frame.pack(expand = 1)
    fourth_place_Frame.pack_propagate(0)

    Label(fourth_place_Frame, text="4th Place",fg="White", bg ="#28394F").pack()
    Label(fourth_place_Frame, text=fourth[0],fg="White", bg ="#28394F").pack()
    Label(fourth_place_Frame, text="Answered Questions: "+str(fourth[1]),fg="White", bg ="#28394F").pack()
    Label(fourth_place_Frame, text="Correct Answers: "+str(fourth[2]),fg="White", bg ="#28394F").pack()
    Label(fourth_place_Frame, text="Percent Correct: "+str(fourth[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    fifth_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    fifth_place_Frame.pack(expand = 1)
    fifth_place_Frame.pack_propagate(0)

    Label(fifth_place_Frame, text="5th Place",fg="White", bg ="#28394F").pack()
    Label(fifth_place_Frame, text=fifth[0],fg="White", bg ="#28394F").pack()
    Label(fifth_place_Frame, text="Answered Questions: "+str(fifth[1]),fg="White", bg ="#28394F").pack()
    Label(fifth_place_Frame, text="Correct Answers: "+str(fifth[2]),fg="White", bg ="#28394F").pack()
    Label(fifth_place_Frame, text="Percent Correct: "+str(fifth[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    sixth_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    sixth_place_Frame.pack(expand = 1)
    sixth_place_Frame.pack_propagate(0)

    Label(sixth_place_Frame, text="6th Place",fg="White", bg ="#28394F").pack()
    Label(sixth_place_Frame, text=sixth[0],fg="White", bg ="#28394F").pack()
    Label(sixth_place_Frame, text="Answered Questions: "+str(sixth[1]),fg="White", bg ="#28394F").pack()
    Label(sixth_place_Frame, text="Correct Answers: "+str(sixth[2]),fg="White", bg ="#28394F").pack()
    Label(sixth_place_Frame, text="Percent Correct: "+str(sixth[3])+"%",fg="White", bg ="#28394F").pack()
    #*************************************************
    seventh_place_Frame=Frame(leaderboard,width=w/4,height=(lCardHeight),bg="#28394F")
    seventh_place_Frame.pack(expand = 1)
    seventh_place_Frame.pack_propagate(0)

    Label(seventh_place_Frame, text="7th Place",fg="White", bg ="#28394F").pack()
    Label(seventh_place_Frame, text=seventh[0],fg="White", bg ="#28394F").pack()
    Label(seventh_place_Frame, text="Answered Questions: "+str(seventh[1]),fg="White", bg ="#28394F").pack()
    Label(seventh_place_Frame, text="Correct Answers: "+str(seventh[2]),fg="White", bg ="#28394F").pack()
    Label(seventh_place_Frame, text="Percent Correct: "+str(seventh[3])+"%",fg="White", bg ="#28394F").pack()

#************************Buttons*************************
    Button(revision,text="Questions",command=lambda:questions(),width=150,height=12,bd=0, font=(None,20),bg="#213041",fg="white").pack()
    Button(revision,text="Account",width=150,height=12,bd=0, font=(None,20),bg="#213041",fg="white",command=lambda:account(bottom)).pack()


#***********************Quiz Cards***********************
    Button(results, text="Previous Quizzes",fg="White", bg ="#28394F",font=(None,11),bd=0,width=100).pack()

