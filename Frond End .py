from tkinter import *
import tkinter.messagebox

import sys


def main():
    root=Tk()
    app=window1(root)
class window1:
    def __init__(self,root):
        self.root=root
        self.root.title('Login Window')
        self.root.geometry('1350x750+0+0')
        self.root.config(bg='crimson')
        self.frame=Frame(self.root,bg='crimson')
        self.frame.pack()
        
        self.username=StringVar()
        self.password=StringVar()
        
        
        self.title=Label(self.frame,text='<<<<<<College Admission System>>>>>> ',font=('Algerian',40,'bold'),bg='crimson',fg='ghost white')
        self.title.grid(row=0,column=0,pady=40)
        
        self.a=Label(self.frame,text='---Log_in---',relief=FLAT,bg='crimson',fg='black',width=50,height=1,font=('Comic Sans MS',20,'bold'))
        self.a.grid(row=1,column=0,rowspan=1)
        
        #--------------------------------------------------------------------------------------------------------------------
        self.loginframe1=LabelFrame(self.frame,width=1350,height=600,relief=GROOVE,bg='crimson',bd=20)
        self.loginframe1.grid(row=4,column=0)
        self.loginframe2=LabelFrame(self.frame,width=1500,height=600,relief=GROOVE,bg='crimson',bd=20)
        self.loginframe2.grid(row=5,column=0)
        
        
        #------------------------------------------------Labels and entry----------------------------------------------------
        
        self.username=Label(self.loginframe1,text='Username',bd=22,fg='cornsilk',width=20,bg='crimson',font=('Comic Sans MS',20,'bold'),relief=FLAT)
        self.username.grid(row=0,column=0)
        
        self.txtusername=Entry(self.loginframe1,width=15,font=('Comic Sans MS',20,'bold'),textvariable=self.username)
        self.txtusername.grid(row=0,column=1)
        
        self.password=Label(self.loginframe1,text='Password',bd=22,fg='cornsilk',width=20,bg='crimson',font=('Comic Sans MS',20,'bold'),relief=FLAT)
        self.password.grid(row=1,column=0)
        
        self.txtpassword=Entry(self.loginframe1,width=15,font=('Comic Sans MS',20,'bold'),textvariable=self.password,show='*')
        self.txtpassword.grid(row=1,column=1)
       # -----------------------------------------------Buttons------------------------------------------------------------------------------
        log_in=Button(self.loginframe2,text='Login',width=13,font=('Comic Sans MS',15,'bold'),cursor='hand2',command=self.new_window)
        log_in.grid(row=3,column=0,pady=20,padx=8)
        
        reset=Button(self.loginframe2,text='Reset',width=13,font=('Comic Sans MS',15,'bold'),cursor='hand2',command=self.rest)
        reset.grid(row=3,column=1,pady=20,padx=8)
        
        exit=Button(self.loginframe2,text='Exit Window',font=('Comic Sans MS',15,'bold'),cursor='hand2',width=13,command=self.iexit)
        exit.grid(row=3,column=2,pady=20,padx=8)
        # -----------------------------------------------functions---------------------------------------------------------------
    def login_system(self):
        if (self.username.get()=='' and self.username.get()==''):
            messagebox.showerror('ALL FIELDS ARE REQUIRED!')
        elif (self.username.get()=='Pankhuri' and self.username.get()=='123456'):
            self.txtusername.delete(0,END)
            self.txtpassword.delete(0,END)
            
        else:
            tkinter.messagebox('login_system ','Too Bad,Invalid login details')
            self.txtusername.delete(0,END)
            self.txtpassword.delete(0,END)
        
    def rest(self):
        '''self.username.set('')
        self.password.set('')
        self.txtusername.focus()'''
        self.txtusername.delete(0,END)
        self.txtpassword.delete(0,END)
        
    def iexit(self):
            iexit=tkinter.messagebox.askyesno('Admission Management System','Do you want to exit ?')
            if iexit>0:
                root.destroy()
            return
    
        
        
    def new_window(self):
        self.newwindow=Toplevel(self.root)
        self.app=window2(self.newwindow)
    
class window2:
    def __init__(self,root):
        self.root=root
        self.root.title('college admission system')
        self.root.geometry('1350x7520+0+0')
        self.root.configure(bg='crimson')
        
        stdid=StringVar()
        firstname=StringVar()
        surname=StringVar()
        dob=StringVar()
        age=StringVar()
        gender=StringVar()
        address=StringVar()
        mobile=StringVar()
        city=StringVar()
        state=StringVar()
        title=Label(self.root,text="Admission Management System",width=100,bd=10,relief=GROOVE, font=("Times New Roman",40,"bold")
                    ,bg="black",fg="white")
        title.pack()


        def connection():
            try:
                conn=sqlite3.connect("student.db")
            except:
                print("cannot connect to the database")
            return conn    

        def verifier():
            a=b=c=d=e=f=g=h=i=j=0
            if not firstname.get():
                studentlist.insert(END,"<>Student name is required<>\n")
                a=1
            if not stdid.get():
                studentlist.insert(END,"<>Roll no is required<>\n")
                b=1
            if not surname.get():
                studentlist.insert(END,"<>surname is required<>\n")
                c=1
            if not mobile.get():
                studentlist.insert(END,"<>Phone number is requrired<>\n")
                d=1
            if not city.get():
                studentlist.insert(END,"<>Father name is required<>\n")
                e=1
            if not address.get():
                studentlist.insert(END,"<>Address is Required<>\n")
                f=1
            if not dob.get():
                studentlist.insert(END,"<>Date of birth is Required<>\n")
                g=1
            if not state.get():
                studentlist.insert(END,"<>State is Required<>\n")
                h=1
            if not age.get():
                studentlist.insert(END,"<>Age is Required<>\n")
                i=1
            if not gender.get():
                studentlist.insert(END,"<>gender is Required<>\n")
                j=1
            if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1:
                return 1
            else:
                return 0

        def student_rec():
            global sd
            searchstd=studentlist.curselection()[0]
            sd=studentlist.get(searchstd)
            self.txtstdid.delete(0,END)
            self.txtstdid.insert(END,sd[1])
            self.txtfna.delete(0,END)
            self.txtfna.insert(END,sd[2])
            self.txtsna.delete(0,END)
            self.txtsna.insert(END,sd[3])
            self.txtdob.delete(0,END)
            self.txtdob.insert(END,sd[4])
            self.txtage.delete(0,END)
            self.txtage.insert(END,sd[5])
            self.txtgender.delete(0,END)
            self.txtgender.insert(END,sd[6])
            self.txtaddress.delete(0,END)
            self.txtaddress.insert(END,sd[8])
            self.txtcity.delete(0,END)
            self.txtcity.insert(END,sd[9])
            self.txtstate.delete(0,END)
            self.txtstate.insert(END,sd[10])
            self.txtmobile.delete(0,END)
            self.txtmobile.insert(END,sd[11])
        

        def iexit():
            iexit=tkinter.messagebox.askyesno('Admission Management System','Do you want to exit ?')
            if iexit>0:
                root.destroy()
            return
        def cleardata():
            self.txtstdid.delete(0,END)
            self.txtfna.delete(0,END)
            self.txtsna.delete(0,END)
            self.txtdob.delete(0,END)
            self.txtage.delete(0,END)
            self.txtgender.delete(0,END)
            self.txtaddress.delete(0,END)
            self.txtcity.delete(0,END)
            self.txtstate.delete(0,END)
            self.txtmobile.delete(0,END)
        def add_data():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS(stdID text,Firstname text, Surname text,Dob text, \
                            Age text, Gender text, city text,State text, Address text,Mobile text)")
                cur.execute("insert into STUDENTS values(?,?,?,?,?,?,?,?,?,?)",(stdid.get(),firstname.get(), surname.get(),dob.get(), \
                            age.get(), gender.get(), city.get(),state.get(), address.get(),mobile.get()))
                conn.commit()
                conn.close()
                studentlist.insert(END,"ADDED SUCCESSFULLY\n")
                    
        def disp_data():
            conn=connection()
            cur=conn.cursor()
            cur.execute("select * from STUDENTS")
            data=cur.fetchall()
            conn.close()
            for i in data:
                studentlist.insert(END,str(i)+"\n")
        
        def delete_data():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute("DELETE FROM STUDENTS WHERE stdID=?",(stdid.get(),))
                conn.commit()
                conn.close()
                studentlist.insert(END,"SUCCESSFULLY DELETED THE USER\n")
           
        
        def update():
            ret=verifier()
            if ret==0:
                conn=connection()
                cur=conn.cursor()
                cur.execute('UPDATE STUDENTS SET stdID=?,Firstname=?, Surname=?,Dob=?, \
                            Age=?, Gender=?, city=?,State=?, Address=?,Mobile=?',(stdid.get(),firstname.get(), surname.get(),dob.get(), \
                            age.get(), gender.get(), city.get(),state.get(), address.get(),mobile.get()))
                conn.commit()
                conn.close()
                studentlist.insert(END,"UPDATED SUCCESSFULLY\n")
            
            
            
            
            
    #------------------------------------------------Frame----------------------------------------------------------------
        mainframe=Frame(self.root,bg='crimson')
        mainframe.place(x=10,y=150)
        
        #titleframe=Frame( mainframe,bg='ghost white',bd=2,padx=54,pady=8,relief=RIDGE)
        #titleframe.pack(side=TOP)
        
        #self.titlbl=Label(titleframe,text="Admission Management System",width=39,bd=10,relief=GROOVE, font=("Times New Roman",20,"bold"),bg="black",fg="white")
        #self.titlbl.grid()
        
        buttonframe=Frame( mainframe,bg='ghost white',bd=2,padx=10,pady=10,relief=RIDGE,width=1350,height=60)
        buttonframe.pack(side=BOTTOM)
        
        #dataframe=Frame( mainframe,bg='cadet blue',bd=1,width=1300,height=400,padx=20,pady=20,relief=RIDGE)
        #dataframe.pack(side=BOTTOM)
        
        dataframeleft=LabelFrame( mainframe,width=1000,height=800,bd=1,padx=20,relief=RIDGE,
                                 font=("Times New Roman",20,"bold"),text='Student info\n')
        dataframeleft.pack(side=LEFT)
        
        dataframeright=LabelFrame( mainframe,bg='ghost white',width=1500,height=500,bd=1,padx=31,pady=3,relief=RIDGE,
                                 font=("Times New Roman",20,"bold"),text='student details\n')
        dataframeright.pack(side=RIGHT)
        
        #------------------------------------------------Labels and entry----------------------------------------------------------------
        self.lblstuid=Label(dataframeleft,text='Student id:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblstuid.grid(row=0,column=0,sticky='w')
        self.txtstdid=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=stdid,width=39)
        self.txtstdid.grid(row=0,column=1)
        
        self.lblfna=Label(dataframeleft,text='First name:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblfna.grid(row=1,column=0,sticky='w')
        self.txtfna=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=firstname,width=39)
        self.txtfna.grid(row=1,column=1)
        
        self.lblsna=Label(dataframeleft,text='Surname: ',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblsna.grid(row=2,column=0,sticky='w')
        self.txtsna=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=surname,width=39)
        self.txtsna.grid(row=2,column=1)
        
        self.lbldob=Label(dataframeleft,text='Date of Birth:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lbldob.grid(row=3,column=0,sticky='w')
        self.txtdob=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=dob,width=39)
        self.txtdob.grid(row=3,column=1)
        
        self.lblage=Label(dataframeleft,text='Age:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblage.grid(row=4,column=0,sticky='w')
        self.txtage=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=age,width=39)
        self.txtage.grid(row=4,column=1)
        
        self.lblgender=Label(dataframeleft,text='Gender:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblgender.grid(row=5,column=0,sticky='w')
        self.txtgender=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=gender,width=39)
        self.txtgender.grid(row=5,column=1)
        
        self.lbladdress=Label(dataframeleft,text='Address:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lbladdress.grid(row=6,column=0,sticky='w')
        self.txtaddress=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=address,width=39)
        self.txtaddress.grid(row=6,column=1)
        
        self.lblcity=Label(dataframeleft,text='city:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblcity.grid(row=7,column=0,sticky='w')
        self.txtcity=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=city,width=39)
        self.txtcity.grid(row=7,column=1)
        
        self.lblstate=Label(dataframeleft,text='State:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblstate.grid(row=8,column=0,sticky='w')
        self.txtstate=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=state,width=39)
        self.txtstate.grid(row=8,column=1)
        
        self.lblmobile=Label(dataframeleft,text='Mobile no.:',font=("Times New Roman",20,"bold"),padx=2,pady=2,relief=FLAT)
        self.lblmobile.grid(row=9,column=0,sticky='w')
        self.txtmobile=Entry(dataframeleft,font=("Times New Roman",20,"bold"),textvariable=mobile,width=39)
        self.txtmobile.grid(row=9,column=1)
        
        #------------------------------------------------buttons -------------------------------------------------------
        self.btnadd=Button(buttonframe,text='Add new',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=add_data)
        self.btnadd.grid(row=0,column=0)
        
        self.btndisp=Button(buttonframe,text='Display',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=disp_data)
        self.btndisp.grid(row=0,column=1)
        
        self.btnclr=Button(buttonframe,text='Clear',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=cleardata)
        self.btnclr.grid(row=0,column=2)
        
        self.btndel=Button(buttonframe,text='Delete',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=delete_data)
        self.btndel.grid(row=0,column=3)
        
        self.btnsearch=Button(buttonframe,text='Search',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4)
        self.btnsearch.grid(row=0,column=4)
        
        self.btnupdate=Button(buttonframe,text='Update',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=update)
        self.btnupdate.grid(row=0,column=5)
        
        self.btnexit=Button(buttonframe,text='Exit',font=('Comic Sans MS',20,'bold'),height=1,width=10,bd=4,command=iexit)
        self.btnexit.grid(row=0,column=6)
        #------------------------------------------------List box and scrollbar-------------------------------------------------------
        scrollbar=Scrollbar(dataframeright)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        studentlist=Listbox(dataframeright,width=41,height=16,font=('Times New Roman',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.bind('<<ListboxSelect>>',student_rec)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)
    
if __name__=='__main__':
    root=Tk()
    ob=window1(root)
    root.mainloop()  

