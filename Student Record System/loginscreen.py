from tkinter import *
from tkinter import messagebox
import os
import sqlite3


root=Tk()
root.title("Login Screen")
root.attributes("-fullscreen",True)

varusername=StringVar()
varpassword=StringVar()


def login_clicked():
    fileexits=1
    try:
        f=open("tbllogin.txt")
    except:
        fileexits=0

    if(fileexits==0):
        messagebox.showinfo("OOps","File is empty..No user exits")           
    else:
        datalist=f.readlines()
        found=0
        for line in datalist:
            l=line.rstrip().split(',')
            if(l[0]==str(varusername.get()) and l[1]==str(varpassword.get())):
               messagebox.showinfo("Great","Login successful...")
               found=1
               root.destroy()
               os.system('menu.py')
        if(found==0):
            messagebox.showinfo("Sorry","User does not exits...")           
        f.close()    



def logindb_clicked():
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    uname=str(varusername.get())
    pwd=str(varpassword.get())

    c.execute("select * from tbllogin where username=(?) and password=(?)",(uname,pwd))
    data=c.fetchall()
    if(len(data)==0):   
        messagebox.showinfo("Sorry","User does not exits...") 
    else:
        messagebox.showinfo("Great","Login successful...")
        root.destroy()
        os.system('menu.py')   
    conn.commit()
    conn.close()

           

def create_clicked():
    root.destroy()
    os.system('createuser.py')
    

def cancel_clicked():
    root.destroy()


titleLabel=Label(root,text="Login Screen",font=("Stencil",40),bg='khaki').place(x=700,y=100);

lblusername=Label(root,text="USERNAME",font=("Stencil",30),bg='khaki').place(x=420,y=250);
lblpassword=Label(root,text="PASSWORD",font=("Stencil",30),bg='khaki').place(x=420,y=350);

txtusername=Entry(root,font=("Arial",30),bg='khaki',textvariable=varusername)
txtusername.place(x=750,y=250);
txtpassword=Entry(root,font=("Arial",30),bg='khaki',show="*",textvariable=varpassword)
txtpassword.place(x=750,y=350);


btnlogin=Button(root,text="LOGIN",font=("Stencil",20),bg='khaki',command=logindb_clicked).place(x=600,y=500);
btncreate=Button(root,text="CREATE USER",font=("Stencil",20),bg='khaki',command=create_clicked).place(x=800,y=500);
btncancel=Button(root,text="CANCEL",font=("Stencil",20),bg='khaki',command=cancel_clicked).place(x=1100,y=500);
txtusername.focus()

root.mainloop()
