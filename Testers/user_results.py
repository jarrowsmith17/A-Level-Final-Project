from tkinter import *
from tkinter import messagebox
import sqlite3
from operator import itemgetter
import sys
signedUser="ADMIN"
root = Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()

leaderboard_list = []

bottom=Frame(root,width=w,height=h-50,bg='#151E29')
bottom.pack(expand=1)
bottom.pack_propagate(0)
    
results=Frame(bottom,width=w/4,height=h-50,bg="#213041")
results.pack(expand=0,fill=BOTH,side=LEFT)
results.pack_propagate(0)

Button(results, text="Previous Quizzes",fg="White", bg ="#28394F",font=(None,11),bd=0,width=100).pack()

db_conn = sqlite3.connect('Coursework.db')
with db_conn:
        curs = db_conn.cursor()    
        curs.execute("""SELECT resultID,Score,Date
                            FROM tbl_results
                            WHERE Username = ?
                        """,(signedUser,))

        row = curs.fetchall()
        print(row)
        x=0

        no_of_results=len(row)
db_conn.close()

iterations=0
while no_of_results>0 or iterations==5:
        hi=Frame(results,width=w/4,height=(h/7),bg="#28394F")
        hi.pack(expand = 1)
        hi.pack_propagate(0)
        
        user = row[iterations]
        iterations+=1
        no_of_results-=1
        Label(hi, text="", bg="#213041").pack()
        Label(hi, text="", bg="#213041").pack()
        Label(hi, text="Test ID: "+str(user[0]), fg="White", bg="#28394F",font=(None,11)).pack()
        Label(hi, text="Users Score: "+str(user[1]), fg="White", bg="#28394F",font=(None,11)).pack()
        Label(hi, text="User Percent: "+str((user[1]/10)*100)+"%", fg="White", bg="#28394F",font=(None,11)).pack()
        Label(hi, text="Date: "+str(user[2]), fg="White", bg="#28394F",font=(None,11)).pack()








root.geometry("%dx%d+0+0" % (w,h))
#root.overrideredirect(True)
root.focus_set()
root.mainloop()

