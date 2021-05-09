from tkinter import *

from tkinter import ttk

import random


fortunes = [

    "2016 is your Lucky year!", "Good fortune is coming your way.",

    "Better stay in today", "Love is on the horizon",

 "Whatever will be will be.",

]

 

pbnumber = 0

def tell_fortune(): #Update Label Text

    r = random.randint(0,4)

    result.set(fortunes[r])


def pb_update():

    global pbnumber

    while pbnumber < 100:

        pbnumber += 5

       #print (pbnumber)

        pbmove.set(pbnumber)

        tell_fortune()

       

window = Tk()

window.title("Fortune Teller")
#window.wm_iconbitmap('fortuneicon.ico')

window.geometry('400x200') # Fixed window Size 400, 200
result = StringVar()
result.set('')
pbmove = IntVar()
pbmove.set('')
mainframe = ttk.Frame(window, relief='groove', borderwidth=5, padding='12 12 12 12')
mainframe.grid(column=0, row=0)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
img = PhotoImage(file='happy.png')
lbl_Header = ttk.Label(mainframe, image=img).grid(columnspan=3, row=0, sticky=(W,E))
lbl_fortune = ttk.Label(mainframe, textvariable=result).grid(columnspan=3, row=1)
pb = ttk.Progressbar(mainframe,orient='horizontal',length=300,mode='determinate', maximum=100, value=pbnumber).grid(columnspan=3,row=2, sticky=(W,E))
btn_press = ttk.Button(mainframe, text="Press Here", width = 30, command=pb_update,).grid(column=0, row=3, sticky=W)
btn_quit = ttk.Button(mainframe, text="Quit", command=exit).grid(column=1, row=3, stick=E)
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
window.mainloop()
