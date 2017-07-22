
from tkinter import *
from turtle import *

def square(turtle,size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)


t = Turtle()
screen = getscreen()
screen.setup(850, 850)
screen.bgcolor("LightYellow")
speed(1) # set the slowest speed to see the turtle movements
bgpic('turtle-xy-grid.gif')

malik = Turtle()      # create a turtle named malik
square(malik, 100)    # draw a square of size 100
square(malik, 75)     # draw a square of size 75
square(malik, 50)     # draw a square of size 50
square(malik, 25)     # draw a square of size 25
    

from turtle import *  # use the turtle library


# space = Screen()           # create a turtle screen (space)


def mystery(turtle,size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size / 2)
    turtle.right(90)


from turtle import *       # use the turtle library
space = Screen()           # create a turtle screen (space)
malik = Turtle()           # create a turtle named malik
mystery(malik, 250)        # draw something with size = 100

def square(turtle,size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)

from turtle import *      # use the turtle library
space = Screen()          # create a turtle screen (space)
emily = Turtle()          # create a turtle named emily
emily.setheading(90)      # Point due north
emily.forward(10)         # Offset the shapes a bit
emily.right(18)           # And turn each one a bit
square(emily,100)             # draw a square with size 100
emily.forward(10)         # Offset the shapes a bit
emily.right(18)           # And turn each one a bit
square(emily,100)             # draw a square with size 100
emily.forward(10)         # Offset the shapes a bit
emily.right(18)           # And turn each one a bit
square(emily,100)             # draw a square with size 100

space.exitonclick()
