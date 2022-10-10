from tkinter import*
from tkinter import ttk, messagebox
import tkinter as tk
import sqlite3
from tkinter.font import BOLD

#DataBase Call

try:
    db=sqlite3.connect('CMS_Data.db')
    cr=db.cursor()
    cr.execute("create table College(Name txt Primary Key, Registration int, Roll int, Gender txt, DOB txt, Contact int, Email txt, Address txt)")
    db.commit()
except:
    print("Table is already available!")

#Window Setup

class college:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1280x720')
        self.root.title('College Management System V.0')

#Background Img Creation(Remeber To Change The Path as per your system)
        bg_image=tk.PhotoImage(file = "/home/sam/Desktop/Coding/Project/clg_bg.gif")
        bg_label=Label(root,image=bg_image)
        bg_label.place(relx=0,rely=0)
        bg_label.image=bg_image

#Title
        title=Label(self.root, text="College Management System",bd=10, font=('Roboto',40, 'bold'),bg='#40E0D0',fg='White')
        title.pack(side=TOP,fill=BOTH)

#Welcome PopUp Message
        messagebox.showinfo("Greetings",  "Welcome To College Management System Ver.0")

#Login Page
        self.Username=StringVar()
        self.Password=StringVar()

        En=Label(text='ADMIN LOGIN',font=('Times New Roman', 40, BOLD),background='#b3e5ff')
        En.place(x=470,y=200)
                
        lbl_username=Label(text='Username',bg='#8FBC8F',fg='#000000',font=('Open Sans', 20, 'bold'),background='#e5fa7f')
        lbl_username.place(x=390,y=300)
            
        text_username=Entry(font=('Open Sans', 20, 'bold'),bd=2, relief=GROOVE,textvar=self.Username)
        text_username.place(x=570,y=300,width=350,height=45)
            
        lbl_password=Label(text='Password',bg='#e5fa7f',font=('Open Sans', 20, 'bold'))
        lbl_password.place(x=390,y=400)
            
        text_password=Entry(root, show ='*',textvar=self.Password)
        text_password.place(x=570,y=400,width=350,height=45)

        login=Button(text='Login',bg='#3cc74c',fg='Black',font=('Rockwell Condensed', 20, 'bold'), command=self.login_system)
        login.place(x=600,y=490,width=100,height=50)

#Bottom 2 Buttons
        self.Registerbtn=Button(text='Register New Student',bg='#ffcb52',fg='Black',font=('Rockwell Condensed', 20, 'bold'),state=DISABLED,command=lambda :RegisterNewStudent())
        self.Registerbtn.place(x=100,y=600,width=500,height=50)
        
        self.Displaybtn=Button(text='Display Student Information',bg='#ffcb52',fg='Black',font=('Rockwell Condensed', 20, 'bold'),state=DISABLED,command=lambda :DisplayStudentInformation())
        self.Displaybtn.place(x=640,y=600,width=500,height=50)

#Login System
    def login_system(self):
        user=(self.Username.get())
        pass1=(self.Password.get())
    
        if (user==str('admin')) and (pass1==str(54321)):
            self.Registerbtn.config(state=NORMAL)
            self.Displaybtn.config(state=NORMAL)
        else:
            messagebox.showinfo("Admin Login","Invalid Username or Password!")
            self.Username.set("")
            self.Password.set("")

#Registration Page

def RegisterNewStudent():
    root.destroy()
    w=Tk()
        
    x=StringVar()
    y=StringVar()
    z=StringVar()
    m=StringVar()
    n=StringVar()
    o=StringVar()
    p=StringVar()
        
        
    w.title("Register New Student")
    w.geometry('1550x780')
    w.configure(background="white")  

#Registration Page Button Systems
                
    def insert():
        cr.execute("insert into College(Name, Registration, Roll, Gender, DOB , Contact, Email, Address) values(?,?,?,?,?,?,?,?)",(text_name.get(),text_registration.get(),text_roll.get(),combo_gender.get(),text_dob.get(),text_Contact.get(),text_email.get(),text_Address.get('1.0',END)))
        db.commit()
        messagebox.showinfo("Success", "Student Data Saved Successfully")
        
        
    def update():
        cr.execute("update College set Registration=?, Roll=?, Gender=?, DOB=?, Contact=?, Email=?, Address=? where Name=?",(text_registration.get(),text_roll.get(),combo_gender.get(),text_dob.get(),text_Contact.get(),text_email.get(),text_Address.get('1.0',END),text_name.get()))
        db.commit()
        messagebox.showinfo("Success", "Student Data Updated Successfully")
        
        
    def delete():
        cr.execute("delete from College where Name=?",(text_name.get(),))
        db.commit()
        messagebox.showinfo("Success", "Student Data Deleted Successfully")
        
    def Reset():
        x.set("")
        y.set("")
        z.set("")
        m.set("")
        n.set("")
        o.set("")
        p.set("")
        text_Address.delete('1.0',END)
        messagebox.showinfo("Success", "Reset Successfully Done.")

    L1= tk.Label(w, text="Register New Student", font=('Arial',50, 'bold'),relief=GROOVE,bg="#00CED1",fg="black", width=80)
    L1.pack()
    
#Frame Setup
    Manage_Frame=Frame(w, bd=4, relief=RIDGE,bg='#FFE194')
    Manage_Frame.place(x=0,y=80,width=1550,height=700)

#Registration Page
    
    m_title=Label(Manage_Frame, text='Manage Student Data',bg='#FFE194',fg='#2F4F4F',font=('Edwardian Script ITC', 35, 'bold'))
    m_title.place(x=490,y=20)
       
    lbl_name=Label(Manage_Frame, text='Name',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_name.place(x=3,y=150)
       
    text_name=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE, textvar=x)
    text_name.place(x=100,y=150,width=350,height=45)
       
    lbl_registration=Label(Manage_Frame, text='Registration No.',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_registration.place(x=470,y=150)
       
    text_registration=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE ,textvar=y)
    text_registration.place(x=680,y=150,width=350,height=45)
       
    lbl_roll=Label(Manage_Frame, text='Roll No. ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_roll.place(x=1040,y=150)
       
    text_roll=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE ,textvar=z)
    text_roll.place(x=1150,y=150,width=350,height=45)
    
    lbl_Gender=Label(Manage_Frame, text='Gender ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Gender.place(x=3,y=250)
       
    combo_gender=ttk.Combobox(Manage_Frame, font=('times new roman', 20, 'bold'),state='readonly',textvar=m)
    combo_gender['values']=('Male','Female','Others')
    combo_gender.place(x=100,y=250,width=350,height=45)
    
    lbl_dob=Label(Manage_Frame, text='D.O.B ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_dob.place(x=470,y=250)
       
    text_dob=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE,textvar=n)
    text_dob.place(x=680,y=250,width=350,height=45)
       
    lbl_Contact=Label(Manage_Frame, text='Contact ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Contact.place(x=1040,y=250)
       
    text_Contact=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE,textvar=o)
    text_Contact.place(x=1150,y=250,width=350,height=45)
       
    lbl_email=Label(Manage_Frame, text='Email ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_email.place(x=3,y=350)
       
    text_email=Entry(Manage_Frame,font=('times new roman', 20, 'bold'),bd=2, relief=GROOVE,textvar=p)
    text_email.place(x=100,y=350,width=350,height=45)
       
    lbl_Address=Label(Manage_Frame, text='Address ',bg='#FFE194',fg='#000000',font=('times new roman', 20, 'bold'))
    lbl_Address.place(x=480,y=350)
       
    text_Address=Text(Manage_Frame,width=30, height=4, font=('',15),relief=GROOVE)
    text_Address.place(x=680,y=350,width=350,height=100)

#Button Frame
    btn_Frame=Frame(Manage_Frame, bd=4, relief=RIDGE,bg='#29AB87')
    btn_Frame.place(x=15,y=500,width=1500,height=80)

#Button Setup (Registration Page)

    Addbtn=Button(btn_Frame,text='Submit',font=('Lucida Calligraphy', 16, 'bold'),bg='#29ff62',command=insert)
    Addbtn.place(x=10,y=15,width=250)
       
    updatebtn=Button(btn_Frame,text='Update',font=('Lucida Calligraphy', 16, 'bold'),bg='#ffe229',command=update)
    updatebtn.place(x=415,y=15,width=250)
       
    deletebtn=Button(btn_Frame,text='Delete',font=('Lucida Calligraphy', 16, 'bold'),bg='#ff294d',command=delete)
    deletebtn.place(x=820,y=15,width=250)
       
    Resetbtn=Button(btn_Frame,text='Reset',font=('Lucida Calligraphy',16, 'bold'),bg='#1696f7',command=Reset)
    Resetbtn.place(x=1225,y=15,width=250)

    backbtn=Button(Manage_Frame,text='Display Student Information',font=('times new roman',16, 'bold'),bg='#2E8B57',fg='white',command=lambda :DisplayStudentInformation())
    backbtn.place(x=300,y=620,width=350)
    
    exitbtn=Button(Manage_Frame,text='Exit Page',font=('times new roman',16, 'bold'),bg='#2E8B57',fg='white',command=w.destroy)
    exitbtn.place(x=900,y=620,width=350)  

#Display All Info System
def DisplayStudentInformation():
    m=Tk()
    
    e=StringVar()
    f=StringVar()
    
    
    
    m.title("Display Student Information")
    m.geometry('1520x800')
    m.configure(background='#01796F')

#Cursor Function
    
    def get_cursor():
        cursor_row=College_table.focus()
        contents=College_table.item(cursor_row)
        row=contents['values']
        
    
#Print(row)
        x.set(row[0])
        y.set(row[1])
        z.set(row[2])
        m.set(row[3])
        n.set(row[4])
        o.set(row[5])
        p.set(row[6])
        text_Address.delete('1.0',END)
        text_Address.insert(END,row[7])
    
    def search_data():
        cr.execute("select * from College where "+str(combo_search.get())+" LIKE '%"+str(text_Search.get())+"%'")
        rows=cr.fetchall()
        if len(rows)!=0:
            College_table.delete(*College_table.get_children())
            for row in rows:
                College_table.insert('', END, values= row)
                db.commit() 
                
                
    def fetch_data():
        cr.execute("select * from College")
        data=cr.fetchall()
        if len(data)!=0:
            College_table.delete(*College_table.get_children()) 
            for i in data:
                College_table.insert('', END, values= i)
                db.commit()   

#Display Student Info Page Setup

    L1= tk.Label(m, text="Display Student Information",relief=GROOVE,bg="#00CED1",fg="black", width=80)
    L1.config(font=("Colonna MT", 50, 'bold'))
    L1.pack()
   
    #Frame Setup
    Display_Frame=Frame(m, bd=4, relief=RIDGE,bg='#5F9EA0')
    Display_Frame.place(x=15,y=90,width=1500,height=650)
    
    #Button
    
    exitbtn=Button(m,text='Exit Page',font=('times new roman',16, 'bold'),bg='#ff4747',fg='white',command=m.destroy)
    exitbtn.place(x=550,y=750,width=350)
    
#Display Student Info Page Buttons/Labels

    lbl_search=Label(Display_Frame, text='Search By',bg='#5F9EA0',fg='white',font=('times new roman', 20, 'bold'))
    lbl_search.grid(row=0, column=0, pady=10,padx=20, sticky="w")
       
       
    combo_search=ttk.Combobox(Display_Frame, width=10, font=('times new roman',14, 'bold'),state='readonly', textvar=e)
    combo_search['values']=('Name','Registration','Roll','Contact')
    combo_search.grid(row=0, column=1, pady=10,padx=20, sticky="w")
       
       
    text_Search=Entry(Display_Frame,width=20, font=('times new roman', 14, 'bold'),bd=5, relief=GROOVE, textvar=f)
    text_Search.grid(row=0, column=2, pady=10,padx=20, sticky="w")
       
    searchbtn=Button(Display_Frame,text='Search', font=('times new roman', 10, 'bold'),width=10,pady=10,bg='#1C2951',fg='white',command=lambda :search_data())
    searchbtn.grid(row=0,column=3,padx=10,pady=10)
       
    showallbtn=Button(Display_Frame,text='Show All', font=('times new roman', 10, 'bold'),width=10,pady=10,bg='#1C2951',fg='white',command=lambda :fetch_data())
    showallbtn.grid(row=0,column=4,padx=10,pady=10)    
    
    Table_Frame=Frame(Display_Frame, bd=4, relief=RIDGE,bg='#422000')
    Table_Frame.place(x=5,y=70,width=1480,height=550)
    
    scroll_x=Scrollbar(Table_Frame, orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame, orient=VERTICAL)
       
    College_table=ttk.Treeview(Table_Frame, columns=("name","registration","roll","gender","dob","contact","email", "Address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
       
    scroll_x.config(command =College_table.xview)
    scroll_y.config(command =College_table.yview)
    
    College_table.heading("name", text="Name")
    College_table.heading("registration", text="Registration No.")
    College_table.heading("roll", text="Roll No.")
    College_table.heading("gender", text="Gender")
    College_table.heading("dob", text="D.O.B")
    College_table.heading("contact", text="Contact")
    College_table.heading("email", text="Email")
    College_table.heading("Address", text="Address")
       
    College_table['show']='headings'
    
    College_table.column('name',width=100)
    College_table.column('registration',width=100)
    College_table.column('roll',width=100)
    College_table.column('gender',width=100)
    College_table.column('dob',width=100)
    College_table.column('contact',width=100)
    College_table.column('email',width=150)
    College_table.column('Address',width=460)
    College_table.pack(fill=BOTH,expand=1)
      

#End Loops
root=Tk()
shw=college(root)
root.mainloop()
