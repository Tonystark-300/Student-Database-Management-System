import sqlite3
def studentdata():
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS student(ID integer PRIMARY KEY, stdID text,\
    Firstname text, Surname text,Dob text, Age text, Gender text, city text,\
     State text, Address text,Mobile text)')
    con.commit()
    con.close()
    
def addstdrec(stdID,Firstname, Surname,Dob, Age, Gender,city, State, Address,Mobile):
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('INSERT INTO student VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',stdID,Firstname, Surname,Dob, Age, Gender,city, State, Address,Mobile)
    con.commit()
    con.close()

def viewdata():
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM student')
    rows=cur.fetchall()
    con.close()
    return rows
    
def deleterec(ID):
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('DELETE FROM student WHERE ID=%d',(ID,))
    con.commit()
    con.close()
    
def searchdata(stdID='',Firstname='',Surname='',Dob='',Age='',Gender='',City='',State='',Address='',Mobile=''):
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('SELECT * FROM student WHERE stdID=%s OR Firstname=%s OR Surname=%s OR Gender=%s OR Address=%s OR \
    City=%s OR State=%s OR Address=%s OR Mobile=%s' ,(stdID,Firstname,Surname,Dob,Age,Gender,City,State,Address,Mobile))
    rows=cur.fetchall()
    con.close()
    return rows
    
def updatedata(ID,stdID='',Firstname='',Surname='',Dob='',Age='',Gender='',City='',\
              State='',Address='',Mobile=''):
    con=sqlite3.connect('studentdatabase.db')
    cur=con.cursor()
    cur.execute('UPDATE student SET stdID=%s,Firstname=%s,Surname=%s,Dob=%s,\
    Age=%s,Gender=%s,Address=%s,City=%s,State=%s,Address=%s,Mobile=%s, WHERE ID=%d',\
                (stdID,Firstname,Surname,Dob,Age,Gender,City,State,Address,Mobile,ID))
    con.commit()
    con.close()
