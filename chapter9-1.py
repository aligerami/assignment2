from tkinter import *

class move_ball:
    def __init__(self):
        window=Tk()
        frame=Frame(window)
        frame.pack()
        self.x=IntVar()
        self.y=IntVar()
        self.canvas=Canvas(window,width=400,height=400,bg="white")

        coord = 10, 10, 80, 80
        self.ball=self.canvas.create_oval(coord,outline="gray",fill="red",width=2)
        self.canvas.pack()
        leftB= Button(frame,text="left",command=self.got_to_the_left)
        leftB.grid(row = 1,column = 1)
        rightB= Button(frame,text="right",command=self.got_to_the_right)
        rightB.grid(row = 1,column = 2)
        upB= Button(frame,text="up",command=self.got_to_the_up)
        upB.grid(row = 1,column = 3)
        downB= Button(frame,text="down",command=self.got_to_the_down)
        downB.grid(row = 1,column = 4)
        
        window.mainloop()
    
    
    
    
    def got_to_the_left(self):
       self.canvas.move(self.ball,-1,0)
    def got_to_the_right(self):
       self.canvas.move(self.ball,1,0)
    def got_to_the_up(self):
       self.canvas.move(self.ball,0,-1)
    def got_to_the_down(self):
       self.canvas.move(self.ball,0,1)
    
move_ball()