
# coding: utf-8

# In[ ]:

from turtle import *
from tkinter import *
# t = Turtle()
# screen = Screen()
# screen.setup(850, 850)
# screen.bgcolor("LightYellow")

colormode(255)
clear()

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

    


# Creates the Figure (F) using points in a Matrix

fmatrix = [[0,0],
          [1,0],
          [1,2],
          [2,2],
          [2,3],
          [1,3],
          [1,4],
          [3,4],
          [3,5],
          [0,5],
          [0,0]]

def drawf(matA):
    pu()
    goto(0,0)
    pd()
    
    for point in matA:
        goto(point[0],point[1])

# Here is the key part:  Return the product of two matrices a and b        
        
def matMult(a,b):        
    newmatrix = []
    
    for i in range(len(a)):
        newmatrix.append([])
        
        for j in range(2):
            newmatrix[i].append(a[i][0]*b[0][j]+a[i][1]*b[1][j])

    return newmatrix


# Define the Transformation Matrix b            

transformationMatrix = [[0,-1],
                       [1,1]]

# Multiply F-matrix= a by Transformation Matrix = b

newmat = matMult(fmatrix, transformationMatrix)
      
# Here is the first transformation        
setup()
drawf(fmatrix)

print(fmatrix)        

speed(250)

pensize(3)
color("blue")
drawf(newmat)

print(newmat)        

# Here is the second transformation

# transformationMatrix = [[0,1],
#                       [-1,0]]

exitonclick()


# In[ ]:



