
from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
import random as r

#create a window
win=tk.Tk()
#set background color to a windOW
win.configure(bg='light gray')
#set title
win.title("coin simulator")
#set geometry
win.geometry("550x500")

#images to place
img1=Image.open('head.jpeg')
res=img1.resize((100,100))
org=ImageTk.PhotoImage(res)
# img1=ImageTk.PhotoImage(file="t2.jpeg")
img2=Image.open("tail.jpeg")
res2=img2.resize((100,100))
org2=ImageTk.PhotoImage(res2)


def start():
    l=["head","tail"]
    res=r.choice(l)
    if res=="head":
        #label image
        Label(win,width=180,height=180,image=org).place(x=180,y=150)

    elif res=="tail":
        #label image
        Label(win,width=180,height=180,image=org2).place(x=180,y=150)

Label(win,width=30,height=2,text="flip coin what you will get head or tail?",fg="black",bg="light gray",font="railway 14").place(x=85,y=90)

Button(win,text='flip coin ',fg="black",bg='dark gray',width=12,height=2,command=start).place(x=170,y=400)  
Button(win,text='exit',fg="black",bg='dark gray',width=12,height=2,command=win.destroy).place(x=290,y=400)  

win.mainloop() 