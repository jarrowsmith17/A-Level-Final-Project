from tkinter import *
from tkinter import messagebox
import sqlite3
from operator import itemgetter
import sys
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()

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
    #print("User:",str(user_details[0]),"\nPercent:",user_details[3],"%","\nAnswered Questions:",str(user_details[1]),"\nCorrect Answers:",str(user_details[2]),"\n")
    ind+=1

leaderboard_rank.sort(key=itemgetter(3), reverse=True)
##for A in range(10):
##    sort_user = leaderboard_rank[A]
##    print(sort_user)
##print (leaderboard_rank)
##print ("fini")

first=leaderboard_rank[0]	
second=leaderboard_rank[1]
third=leaderboard_rank[2]
fouth=leaderboard_rank[3]
fifth=leaderboard_rank[4]
sixth=leaderboard_rank[5]
seventh=leaderboard_rank[6]

leaderboard=Frame(root,width=300,height=h-60,bg="#151E29")
leaderboard.pack(expand = 1)
leaderboard.pack_propagate(0)
#****************FIRST****************************
first_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="red")
first_place_Frame.pack(expand = 1)
first_place_Frame.pack_propagate(0)

Label(first_place_Frame, text="1st Place").pack()
Label(first_place_Frame, text=first[0]).pack()
Label(first_place_Frame, text="Answered Questions: "+str(first[1])).pack()
Label(first_place_Frame, text="Correct Answers: "+str(first[2])).pack()
Label(first_place_Frame, text="Percent Correct: "+str(first[3])+"%").pack()
#****************SECOND***************************
sec_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="yellow")
sec_place_Frame.pack(expand = 1)
sec_place_Frame.pack_propagate(0)
#****************THIRD***************************
third_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="orange")
third_place_Frame.pack(expand = 1)
third_place_Frame.pack_propagate(0)
#*************************************************
fourth_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="purple")
fourth_place_Frame.pack(expand = 1)
fourth_place_Frame.pack_propagate(0)
#*************************************************
fifth_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="green")
fifth_place_Frame.pack(expand = 1)
fifth_place_Frame.pack_propagate(0)
#*************************************************
sixth_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="light blue")
sixth_place_Frame.pack(expand = 1)
sixth_place_Frame.pack_propagate(0)
#*************************************************
seventh_place_Frame=Frame(leaderboard,width=300,height=(h/8),bg="pink")
seventh_place_Frame.pack(expand = 1)
seventh_place_Frame.pack_propagate(0)
#*************************************************
  

root.geometry("%dx%d+0+0" % (w,h))
#root.overrideredirect(True)
root.focus_set()
root.mainloop()

