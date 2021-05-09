from tkinter import *
import sqlite3

root=Tk()
root.title("All Items report")
root.geometry("900x7000")

titleLabel0=Label(root,text="All Items Report",font=("Stencil",30),bg='aquamarine')
titleLabel0.grid(row=0,column=0,columnspan=4)

sqlite_file = 'inventorydb.sqlite'
             
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute("select * from tblstock")
data=c.fetchall()
j=1
for row in data:
    for i in range(len(row)):
        txt=StringVar()
        e=Entry(root,textvariable=txt)
        txt.set(row[i])
        e.grid(row=j,column=i)
    j=j+1     

conn.close()

root.mainloop()
