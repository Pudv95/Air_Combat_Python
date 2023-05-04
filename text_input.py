import subprocess
import tkinter as tk

entry_window = tk.Tk() # generated tkinter window
entry_window.title("Players") # defined title of window
entry_window.geometry("380x150") # defined size/geometry of window
entry_window.minsize(380 , 150) # minimum size
entry_window.maxsize(380 , 150) # maximum size
entry_window.config(bg="black") # defined background color of window

player_name =[] # list for player names

global default_text , count
count = 0
default_text = tk.StringVar() # declared variable for entry widget
default_text.set("Player1") # set default value of variable

def welcome():
    global default_text , count
    name = enter1.get()
    player_name.append(name.upper())
    if count == 1:
            entry_window.destroy()
            
    enter1.delete(0,tk.END)
    count = 1
    default_text.set("Player2")

#created a text label 
text1=tk.Label(entry_window,font=("arial",12,"bold"),bg="black",fg="white",text="Enter the Player1 Name")
text1.pack() 
# text2=tk.Label(entry_window,font=("arial",10,"bold"),bg="black",fg="white",text="Enter the QUANTITY of ITEM:")
# text2.place(x=10,y=75)

#created a entry widget
enter1=tk.Entry(entry_window ,font = ("arial" , 12 , "bold"), justify = "center" , width = 35 )
enter1.configure(textvariable = default_text)
enter1.place(x=34,y=50 ) #setting entry widget coordinates

#created a button 
b1=tk.Button(entry_window,text="HOLA",font=("arial",15,"bold"),bg="cyan",command=welcome)
b1.place(x=155,y=100 ) #setting button coordinates
entry_window.mainloop() # running the tkinter rendering mainloop


