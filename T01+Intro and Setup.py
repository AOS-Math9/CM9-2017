

from turtle import *
from tkinter import *
# t = Turtle()
# screen = Screen()
# screen.setup(850, 850)
# screen.bgcolor("LightYellow")

colormode(255)

def bluelines():
    speed(0)
    color(0,255,255)                       # Sets CYAN as color
    
    for i in range(21):                     # Vertical Lines
        pu()
        goto(-10+i,-10)
        pd()
        goto(-10+i,10)
        pu()
        
    for j in range(21):                    # Horizontal Lines
        pu()
        goto(-10,-10+j)
        pd()
        goto(10,-10+j)
        pu()
    

def setup():
                          # Draws an x-y grid for better visualization
    speed(0)                               # Check out the speed function 
    setworldcoordinates (-15,-15,15,15)    # Assuming these are in pixels ... really
    setposition(0,0)
    clear()
    bluelines()
    setpos(0,0)
    setheading(0)                          # Set direction to default ... face East or positve x
    pd()                                   # Pen Down to start writing
    color("Black")                         # Set the line color for grid pad
    bgcolor("LightYellow")
    
    for i in range(4):
        setpos(0,0)
        fd(10)
        rt(90)
        
    pu()                                   # Pen Up - stop writing
    setpos(0,0)

    
setup()
exitonclick()

