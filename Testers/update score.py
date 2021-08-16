import sqlite3

signedUser= "ADMIN"
Questions_Answered = 10
correctAnswers = 5

def Select_Current_Stats():
    db_conn = sqlite3.connect("Coursework.db")

    with db_conn:

        c = db_conn.cursor()
        c.execute("""SELECT Correct_Answers, Answered_Questions
                    FROM Users
                    WHERE Username = ?                   
                    """,[signedUser])
        row = c.fetchall()
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
    
    update_stats(Questions_A, correctA)

def update_stats(Questions_A, correctA):
    db_conn = sqlite3.connect('Coursework.db')
    with db_conn:
       cur = db_conn.cursor()
       cur.execute("""UPDATE Users
                    SET Correct_Answers = ?,
                    Answered_Questions = ?
                    WHERE Username = ?""",[correctA, Questions_A, signedUser])
    db_conn.close()
    

