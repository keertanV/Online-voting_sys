import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
 
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((35,35),Image.BICUBIC))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    congLogo = ImageTk.PhotoImage((Image.open("img/congo.png")).resize((35,35),Image.BICUBIC))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    aapLogo = ImageTk.PhotoImage((Image.open("img/amm.png")).resize((35,35),Image.BICUBIC))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)


    Label(frame1, text="BJP              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['bjp'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Cong             :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['cong'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text=" AAP               :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['aap'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    frame1.pack()
    root.mainloop()


