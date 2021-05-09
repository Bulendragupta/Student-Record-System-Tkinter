from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import tkinter.ttk as TTK


root=Tk()
root.title("Stock Updation Screen")
root.attributes("-fullscreen",True)

varicode=StringVar()
variname=StringVar()
varrate=StringVar()
varqoh=StringVar()
vardoi=StringVar()
varqtyissued=StringVar()

    
def clear_clicked():
    varicode.set("")
    variname.set("")
    varrate.set("")
    varqoh.set("")
    vardoi.set("")
    varqtyissued.set("")
    

def issue_clicked():
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    vic=varicode.get()
    vin=variname.get()
    vr=varrate.get()
    vqoh=varqoh.get()
    vdoi=vardoi.get()
    vqtyissued=varqtyissued.get()
    
    c.execute("update tblstock set qoh=qoh-(?) where icode=(?)",(vqtyissued,vic))
    conn.commit()
    messagebox.showinfo("Great","Stock Updated...")

    c.execute("insert into tblissue(icode,doi,qtyissued) values (?,?,?)",(vic,vdoi,vqtyissued))
    messagebox.showinfo("Great","Inserted...")
    conn.commit()
    conn.close()
    clear_clicked()
    #txticode['values']=getIcodesList()
    
def cancel_clicked():
    root.destroy()

def getIcodesList():
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute("select icode from tblstock")
    icodelist=[row[0] for row in c.fetchall()]
    conn.close()
    return icodelist
    

def  onItemClicked(event):
    sqlite_file = 'inventorydb.sqlite'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()   
    vic=varicode.get()
    c.execute("select * from tblstock where icode=(?)",(vic,))
    for row in c.fetchall():
        variname.set(row[1])
        varrate.set(row[2])
        varqoh.set(row[3])
    
    conn.commit()
    conn.close()



titleLabel=Label(root,text="Stock Updation Screen",font=("Stencil",30),bg='khaki').place(x=600,y=100);

lblicode=Label(root,text="ITEM CODE",font=("Stencil",20),bg='khaki').place(x=520,y=250);
lbliname=Label(root,text="ITEM NAME",font=("Stencil",20),bg='khaki').place(x=520,y=350);
lblrate=Label(root,text="RATE",font=("Stencil",20),bg='khaki').place(x=520,y=450);
lblqoh=Label(root,text="QOH",font=("Stencil",20),bg='khaki').place(x=520,y=550);

lblrate=Label(root,text="DOI",font=("Stencil",20),bg='khaki').place(x=520,y=650);
lblqoh=Label(root,text="QTY ISSUED",font=("Stencil",20),bg='khaki').place(x=520,y=750);


txticode=TTK.Combobox(root,font=("Arial",20),textvariable=varicode)
txticode.place(x=850,y=250);
txticode.bind("<<ComboboxSelected>>", onItemClicked)

icodelist=getIcodesList()
txticode['values']=icodelist

txtiname=Entry(root,font=("Arial",20),bg='khaki',textvariable=variname,state="disable")
txtiname.place(x=850,y=350);
txtrate=Entry(root,font=("Arial",20),bg='khaki',textvariable=varrate,state="disable")
txtrate.place(x=850,y=450);
txtqoh=Entry(root,font=("Arial",20),bg='khaki',textvariable=varqoh,state="disable")
txtqoh.place(x=850,y=550);

txtdoi=Entry(root,font=("Arial",20),bg='khaki',textvariable=vardoi)
txtdoi.place(x=850,y=650);
txtqtyissued=Entry(root,font=("Arial",20),bg='khaki',textvariable=varqtyissued)
txtqtyissued.place(x=850,y=750);


btnissue=Button(root,text="ISSUE",font=("Stencil",20),bg='khaki',command=issue_clicked).place(x=500,y=900);
btnclear=Button(root,text="CLEAR",font=("Stencil",20),bg='khaki',command=clear_clicked).place(x=700,y=900);
btncancel=Button(root,text="CANCEL",font=("Stencil",20),bg='khaki',command=cancel_clicked).place(x=900,y=900);

root.mainloop()
