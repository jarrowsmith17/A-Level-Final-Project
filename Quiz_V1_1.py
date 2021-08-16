from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
import random

def quiz(main,root,signedUser):
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    f=Frame(main,width=w,height=h,bg="#34475F")
    f.pack(expand = 1)
    f.pack_propagate(0)

    f0=Frame(f,width=w/2,height=h/2,bg="#34475F")     
    f0.pack(expand = 1)
    f0.pack_propagate(0)

    def importQuestions(difficulty):
        print(difficulty)
        global qList
        qList = []

        db_conn = sqlite3.connect("Coursework.db")
        with db_conn:
            cur = db_conn.cursor()
            cur.execute("SELECT Question, Answer, FalseAnswer1, FalseAnswer2, FalseAnswer3 FROM tbl_Questions WHERE Difficulty = ?",(difficulty,))
            row = cur.fetchall()
            #print(row)

            for a in row:
                x=0
                qList.insert(x,a)
                x+=1
        db_conn.close()
        correctAnswers=0
        correct = []
        incorrect = []
        Questions_Answered=0
        runQuiz(correctAnswers,correct,incorrect,Questions_Answered)
        
    def check(answer_dictionary,user_answer,correctAnswers,correct,incorrect,question,Questions_Answered):
        #print (user_answer)
        if answer_dictionary[user_answer] == 1:
            print ("Correct")
            correctAnswers += 1
            #print(correctAnswers)
            correct.append(question)
            #print (correct)
        else:
            print ('incorrect')
            #print(correctAnswers)
            incorrect.append(question)
            #print (incorrect)
        quizF.pack_forget()
        
        if Questions_Answered == 10:
            print ("Fini")              
            buttonFrame.pack_forget()
            quizF.pack_forget()
            resultScreen(correctAnswers,Questions_Answered,correct,incorrect)
            
        
        runQuiz(correctAnswers,correct,incorrect,Questions_Answered)

    def runQuiz(correctAnswers,correct,incorrect,Questions_Answered):
        f0.pack_forget()
        global quizF
        quizF=Frame(f,width=w,height=h,bg='#34475F')
        quizF.pack(expand=1)
        quizF.pack_propagate(0)

        q1L_Frame=Frame(quizF,width=w, height=150,bg='#34475F')
        q1L_Frame.pack(expand=1)
        q1L_Frame.pack_propagate(0)
        
        q1L = Label(q1L_Frame,font=(None,40),fg="white",bg="#34475F")
        q1L.pack(pady=40)
        
        global buttonFrame
        buttonFrame=Frame(quizF,width=w/2,height=h/2,bg="#34475F")
        buttonFrame.pack(expand = 1)
        buttonFrame.pack_propagate(0)
        Questions_Answered+=1
        print (len(qList))
        
        cursor = qList[random.randint(0,len(qList)-1)]
        qList.remove(cursor)
        #print (cursor)
        x = [i for i in range(4)]
        random.shuffle(x)
        answer_dictionary = {}
        for i in range(4):
            if x[i] == 0:
                    answer_dictionary.update({cursor[x[i]+1]:1})
            else:
                    answer_dictionary.update({cursor[x[i]+1]:0})

        answer_list = [v for v in answer_dictionary.keys()]
        #print (cursor[0])
        
        question=cursor[0]
        q1L.config(text="Q"+str(Questions_Answered)+": "+question)
        
        #print(answer_list)

        a=Button(buttonFrame,text=answer_list[0],command=lambda:check(answer_dictionary,a.cget('text'),correctAnswers,correct,incorrect,question,Questions_Answered),font=(None,35),width=w,fg="white", bg="#FF0000", bd=0)
        a.pack(expand=1)
        b=Button(buttonFrame,text=answer_list[1],command=lambda:check(answer_dictionary,b.cget('text'),correctAnswers,correct,incorrect,question,Questions_Answered),font=(None,35),width=w, fg="white", bg="#2626FF", bd=0)
        b.pack(expand=1)
        c=Button(buttonFrame,text=answer_list[2],command=lambda:check(answer_dictionary,c.cget('text'),correctAnswers,correct,incorrect,question,Questions_Answered),font=(None,35),width=w, fg="white", bg="#00D900", bd=0)
        c.pack(expand=1)
        d=Button(buttonFrame,text=answer_list[3],command=lambda:check(answer_dictionary,d.cget('text'),correctAnswers,correct,incorrect,question,Questions_Answered),font=(None,35),width=w, fg="white", bg="#D9D900", bd=0)
        d.pack(expand=1)
        ##Personalise so that the output changes depending on score
        ##allows for a more interactive experience.
    def resultScreen(correctAnswers,Questions_Answered,correct,incorrect):
        db_conn = sqlite3.connect("Coursework.db")

        with db_conn:
            curse = db_conn.cursor()
            curse.execute("""SELECT Correct_Answers, Answered_Questions
                        FROM Users
                        WHERE Username = ?""",[signedUser])
            row = curse.fetchall()
            for a in row:
                CA=a[0]

                AQ=a[1]
        db_conn.close()

        print("Correct Answers "+str(CA))
        print("Answered Questions "+str(AQ))

        Questions_A = str(Questions_Answered+AQ)
        correctA = str(correctAnswers+CA)
            
        print ("Questions_A "+Questions_A)
        print ("CorrectA "+correctA)
            
        update_stats(Questions_A, correctA, correctAnswers,Questions_Answered)

    def update_stats(Questions_A, correctA, correctAnswers,Questions_Answered):
        db_conn = sqlite3.connect('Coursework.db')
        with db_conn:
           cur = db_conn.cursor()
           cur.execute("""UPDATE Users
                        SET Correct_Answers = ?,
                        Answered_Questions = ?
                        WHERE Username = ?""",[correctA, Questions_A, signedUser])
        db_conn.close()
		
        mainTxt="Well done, "+signedUser+". You scored: "+str(correctAnswers)+" Out of a possible "+str(Questions_Answered)+"."
        print(signedUser)
        print(correctAnswers)
        print("resultScreen")
        result_frame=Frame(f,width=w,height=h,bg='white')
        result_frame.pack(expand=1)
        result_frame.pack_propagate(0)
        resTitle = Label(result_frame,text="RESULTS",font=(None,50)).pack()
        mainText = Label(result_frame,text=mainTxt,).pack()

    Easy = Button(f0, text="Easy",command=lambda: importQuestions("Easy"),font=(None,35),width=w, fg="white", bg="green", bd=0, anchor='center')
    Easy.pack(expand=1)#The height of the button. If the button displays text, the size is given in text units.

    Med = Button(f0, text="Medium",command=lambda: importQuestions("Medium"),font=(None,35),width=w, fg="white", bg="orange", bd=0, anchor='center')
    Med.pack(expand=1)

    Hard = Button(f0, text="Hard",command=lambda: importQuestions("Hard"),font=(None,35),width=w, fg="white", bg="red", bd=0, anchor='center')
    Hard.pack(expand=1)
