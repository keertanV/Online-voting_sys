import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk, Image


def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) 

    message = client_socket.recv(1024) 
    print(message.decode()) 
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Helvetica', 50, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "BJP\n\nNarendra Modi", variable = vote, value = "bjp", indicator = 0, height = 4, width=55, command = lambda: voteCast(root,frame1,"bjp",client_socket)).grid(row = 2,column = 1)
    bjpLogo = ImageTk.PhotoImage((Image.open("img/bjp.png")).resize((105, 105), Image.BICUBIC))
    bjpImg = Label(frame1, image=bjpLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Congress\n\nRahul Gandhi", variable = vote, value = "cong", indicator = 0, height = 4, width=55, command = lambda: voteCast(root,frame1,"cong",client_socket)).grid(row = 3,column = 1)
    congLogo = ImageTk.PhotoImage((Image.open("img/congo.png")).resize((105, 105),Image.BICUBIC))
    congImg = Label(frame1, image=congLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "Aam Aadmi Party\n\nArvind Kejriwal", variable = vote, value = "aap", indicator = 0, height = 4, width=55, command = lambda: voteCast(root,frame1,"aap",client_socket) ).grid(row = 4,column = 1)
    aapLogo = ImageTk.PhotoImage((Image.open("img/amm.png")).resize((105, 105),Image.BICUBIC))
    aapImg = Label(frame1, image=aapLogo).grid(row = 4,column = 0)

    frame1.pack()
    root.mainloop()

