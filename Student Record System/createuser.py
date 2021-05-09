from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("Create User Screen")
root.attributes("-fullscreen",True)

varusername=StringVar()
varpassword=StringVar()


def create_clicked():
    fileexits=1
    try:
        f=open("tbllogin.txt")
    except:
        fileexits=0

    if(fileexits==0):
        datalist=[]
        datalist.append(str(varusername.get())+","+str(varpassword.get())+"\n")
        messagebox.showinfo("Great","User created")           
    else:
        datalist=f.readlines()
        found=0
        for line in datalist:
            l=line.rstrip().split(',')
            print(l[0],l[1],str(varusername.get),str(varusername.get))
            if(l[0]==str(varusername.get()) and l[1]==str(varpassword.get())):
               messagebox.showinfo("Error","User already exits...")
               found=1
        if(found==0):
            datalist.append(str(varusername.get())+","+str(varpassword.get())+"\n")
            messagebox.showinfo("Great","User created...")           
        f.close()    
    
    f=open("tbllogin.txt","w")
    f.writelines(datalist)
    f.close()
           

def createdb_clicked():
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    uname=str(varusername.get())
    pwd=str(varpassword.get())

    c.execute("select * from tbllogin where username=(?) and password=(?)",(uname,pwd))
    data=c.fetchall()
    if(len(data)==0):   
        c.execute("insert into tbllogin (username,password) values (?,?)",(uname,pwd))
        messagebox.showinfo("Great","User created...")
    else:
         messagebox.showinfo("Error","User already exits...")    
    conn.commit()
    conn.close()


    

    

def clear_clicked():
    varusername.set("")
    varpassword.set("")

def back_clicked():
    import os
    root.destroy()
    os.system('loginscreen.py')
    


titleLabel=Label(root,text="Create User Screen",font=("Stencil",40),bg='aquamarine').place(x=550,y=100);

lblusername=Label(root,text="USERNAME",font=("Stencil",30),bg='aquamarine').place(x=420,y=250);
lblpassword=Label(root,text="PASSWORD",font=("Stencil",30),bg='aquamarine').place(x=420,y=350);

txtusername=Entry(root,font=("Arial",30),bg='aquamarine',textvariable=varusername)
txtusername.place(x=750,y=250);
txtpassword=Entry(root,font=("Arial",30),bg='aquamarine',show="*",textvariable=varpassword)
txtpassword.place(x=750,y=350);


btncreate=Button(root,text="CREATE",font=("Stencil",20),bg='aquamarine',command=createdb_clicked).place(x=650,y=500);
btnclear=Button(root,text="CLEAR",font=("Stencil",20),bg='aquamarine',command=clear_clicked).place(x=850,y=500);
btnback=Button(root,text="BACK",font=("Stencil",20),bg='aquamarine',command=back_clicked).place(x=1050,y=500);

txtusername.focus()

root.mainloop()
