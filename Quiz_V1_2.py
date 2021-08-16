from tkinter import *
from tkinter import messagebox
import sqlite3
import sys
import random
import datetime

def quiz(main,root,signedUser):
    w,h=root.winfo_screenwidth(),root.winfo_screenheight()
    frame=Frame(main,width=w,height=h,bg="#34475F")
    frame.pack(expand = 1)
    frame.pack_propagate(0)

    def quiz_type(Qtype):
        frame.pack_forget()
        if Qtype == "D":
            Difficulty()
        elif Qtype == "U":
            Unit()

            
    def Difficulty():
        global f
        f=Frame(main,width=w,height=h,bg="#34475F")
        f.pack(expand = 1)
        f.pack_propagate(0)

        global f0
        f0=Frame(f,width=w/2,height=h/2,bg="#34475F")     
        f0.pack(expand = 1)
        f0.pack_propagate(0)
        
        Easy = Button(f0, text="Easy",command=lambda: importQuestionsDiff("Easy"),font=(None,35),width=w, fg="white", bg="green", bd=0, anchor='center')
        Easy.pack(expand=1)#The height of the button. If the button displays text, the size is given in text units.

        Med = Button(f0, text="Medium",command=lambda: importQuestionsDiff("Medium"),font=(None,35),width=w, fg="white", bg="orange", bd=0, anchor='center')
        Med.pack(expand=1)

        Hard = Button(f0, text="Hard",command=lambda: importQuestionsDiff("Hard"),font=(None,35),width=w, fg="white", bg="red", bd=0, anchor='center')
        Hard.pack(expand=1)

    def Unit():
        global f
        f=Frame(main,width=w,height=h,bg="#34475F")
        f.pack(expand = 1)
        f.pack_propagate(0)

        global f0
        f0=Frame(f,width=w/2,height=h/2,bg="#34475F")     
        f0.pack(expand = 1)
        f0.pack_propagate(0)
        
        one = Button(f0, text="Unit 1",command=lambda: importQuestionsUnit("1"),font=(None,35),width=w, fg="white", bg="#00BFFF", bd=0, anchor='center')
        one.pack(expand=1)#The height of the button. If the button displays text, the size is given in text units.

        two = Button(f0, text="Unit 2",command=lambda: importQuestionsUnit("2"),font=(None,35),width=w, fg="white", bg="#00BFFF", bd=0, anchor='center')
        two.pack(expand=1)

    #*****************************************************
    def importQuestionsDiff(difficulty):
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

    def importQuestionsUnit(unit):
            global qList
            qList = []

            db_conn = sqlite3.connect("Coursework.db")
            with db_conn:
                cur = db_conn.cursor()
                cur.execute("SELECT Question, Answer, FalseAnswer1, FalseAnswer2, FalseAnswer3 FROM tbl_Questions WHERE Unit = ?",(unit,))
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
            
            cursor = qList[random.randint(0,len(qList)-1)] ##Chooses a random question from list
            qList.remove(cursor) ##removes question from the list
            x = [i for i in range(4)] ##Retrieves the four possible answers
            random.shuffle(x)
            answer_dictionary = {}
            for i in range(4): ##The loop is used to add the answers to a dictionary
                if x[i] == 0:
                        answer_dictionary.update({cursor[x[i]+1]:1})
                else:
                        answer_dictionary.update({cursor[x[i]+1]:0})

            answer_list = [v for v in answer_dictionary.keys()]##Randomly arranged the answers into a list
            ##the buttons test is indexed from this list
            question=cursor[0]
            q1L.config(text="Q"+str(Questions_Answered)+": "+question)


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

    def check(answer_dictionary,user_answer,correctAnswers,correct,incorrect,question,Questions_Answered):
            
            if answer_dictionary[user_answer] == 1:
                correctAnswers += 1
                correct.append(question)
            else:
                incorrect.append(question)
                
            quizF.pack_forget()
            
            if Questions_Answered == 10:
                buttonFrame.pack_forget()
                quizF.pack_forget()
                resultScreen(correctAnswers,Questions_Answered,correct,incorrect)
                
            runQuiz(correctAnswers,correct,incorrect,Questions_Answered)

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

        Questions_A = str(Questions_Answered+AQ)
        correctA = str(correctAnswers+CA)

        mainTxt="Well done, "+signedUser+". You scored: "+str(correctAnswers)+" Out of a possible "+str(Questions_Answered)+"."

        result_frame=Frame(f,width=w,height=h,bg='#28394F')
        result_frame.pack(expand=1)
        result_frame.pack_propagate(0)
        
        resTitle = Label(result_frame,text="RESULTS",font=(None,25),bg="#28394F",fg="white").pack(ipady=60)
        mainText = Label(result_frame,text=mainTxt,font=(None,15),bg="#28394F",fg="white").pack()

        percentage = format((correctAnswers / Questions_Answered) * 100, '.1f')
        percentage = float(percentage)

        if correctAnswers >=7:
            score=Frame(result_frame,width=w/5,height=h/5,bg='green')
            score.pack(expand=1)
            score.pack_propagate(0)
            Label(score, text=str(percentage) + "%", font=(None, 50), bg="green", fg="white").pack()
            Label(score, text=str(correctAnswers) + "/" + str(Questions_Answered), font=(None, 40), bg="green",
                  fg="white").pack()
        elif 3<correctAnswers<7:
            score=Frame(result_frame,width=w/5,height=h/5,bg='orange')
            score.pack(expand=1)
            score.pack_propagate(0)
            Label(score, text=str(percentage) + "%", font=(None, 50), bg="orange", fg="white").pack()
            Label(score, text=str(correctAnswers) + "/" + str(Questions_Answered), font=(None, 40), bg="orange",
                  fg="white").pack()
        elif 0<correctAnswers<4:
            score=Frame(result_frame,width=w/5,height=h/5,bg='red')
            score.pack(expand=1)
            score.pack_propagate(0)
            Label(score, text=str(percentage) + "%", font=(None, 50), bg="red", fg="white").pack()
            Label(score, text=str(correctAnswers) + "/" + str(Questions_Answered), font=(None, 40), bg="red",
                  fg="white").pack()

#*********************CORRECT LIST**********************************
        correctFrame = Frame(result_frame, width=w / 2, height=h, bg='#5CB900')
        correctFrame.pack(expand=1, fill=BOTH, side=LEFT)
        correctFrame.pack_propagate(0)
        Label(correctFrame,text="Questions answered correctly",bg="#5CB900",fg="white",font=(None,20)).pack()
        for a in correct:
            Label(correctFrame,text=a,bg="#5CB900",fg="white",font=(None,13)).pack()
# *********************INCORRECT LIST**********************************
        incorrectFrame = Frame(result_frame, width=w / 2, height=h, bg='#CA0000')
        incorrectFrame.pack(expand=1,fill=BOTH,side=RIGHT)
        incorrectFrame.pack_propagate(0)
        Label(incorrectFrame, text="Questions answered incorrectly", bg="#CA0000", fg="white", font=(None, 20)).pack(ipady=10)
        for a in incorrect:
            Label(incorrectFrame, text=a, bg="#CA0000", fg="white", font=(None, 13)).pack()

        update_stats(Questions_A, correctA, correctAnswers,Questions_Answered)

    def update_stats(Questions_A, correctA, correctAnswers,Questions_Answered):
        db_conn = sqlite3.connect('Coursework.db')
        with db_conn:
           cur = db_conn.cursor()
           cur.execute("""UPDATE Users
                        SET Correct_Answers = ?,
                        Answered_Questions = ?
                        WHERE Username = ?""",[correctA, Questions_A, signedUser])
           cur.execute("INSERT INTO tbl_results(Score,Date,Username)values(?,?,?)",(correctAnswers, str(datetime.date.today()),signedUser))
        db_conn.commit()
        db_conn.close()
    #*****************************************************
    btn_frame=Frame(frame,width=w/2,height=h/2,bg="#34475F")     
    btn_frame.pack(expand = 1)
    btn_frame.pack_propagate(0)
    
    Button(btn_frame,text="Unit",command=lambda: quiz_type("U"),font=(None,35),width=w, fg="white", bg="#00BFFF", bd=0, anchor='center').pack(expand=1)
    Button(btn_frame,text="Difficulty",command=lambda: quiz_type("D"),font=(None,35),width=w, fg="white", bg="#00BFFF", bd=0, anchor='center').pack(expand=1)

