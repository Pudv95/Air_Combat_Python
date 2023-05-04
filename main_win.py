import subprocess
import os

def window():
    import tkinter as tk

    class hello:
        def action1(self):
            wintk.destroy() # destroying the main window
            subprocess.call(["python" , os.path.join("Atari_breakout","game.py")]) # calling/running the game.py file
            

    obj1 = hello()

    wintk = tk.Tk()
    wintk.geometry("800x550+0+0")
    

    #creating a canvas
    canvas1 = tk.Canvas(wintk)
    canvas1.pack(expand = True ,fill = "both")

    # applying background image on canvas
    image1 = os.path.join("Atari_breakout" , "background.png")
    bgimage = tk.PhotoImage(file = image1 )
    canvas1.create_image(0 ,0 ,image = bgimage)
    
    # applying heading/title of game
    image2 = os.path.join("Atari_breakout" , "heading.png")
    head_img = tk.PhotoImage(file = image2 )
    canvas1.create_image(400 ,200,image = head_img)



    #creating play button
    # play_button_img = tk.PhotoImage(file = "C:\\Users\\dell\\Desktop\\GitHub\\Atari_breakout\\playbutton1.png")
    button1 = tk.Button(wintk , text ="PLAY", font = ("arial" , 16 ,"bold") , borderwidth = 0 , width = 20 , height = 2 , bg = 	"#ff6969" , fg = "white" , command = obj1.action1)
    button1.place(x = 270, y = 300 )
    # button1 = tk.Button(wintk , image = play_button_img , borderwidth = 0 ,command = obj1.action1 )
    # button1.place(x = 270 ,y = 300)
    wintk.mainloop()
window()