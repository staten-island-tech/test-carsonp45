import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

""" t.forward(200) """

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)
 """
""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()
 """

""" def rectangle():
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
rectangle() """

""" def equal():
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal() """

""" for i in range(3):
    print(i) """
""" for i in range(1):
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(110)
t.speed(1000)

for i in range(59):
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(90)
    t.forward(110)
    t.left(5)
t.speed(1000) """
""" """ """ sidelength = 100
rotate = 90"""

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90) 
def doubleSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length = length * 2
doubleSquares(5) """
""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
square(100,90) 
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)
 """
""" def Square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
Square(5,90) 
def addSquares(iRange):
    length = 5
    for i in range(iRange):
        Square(length,90)
        length += 5
        t.right(5)
        t.speed(0)
addSquares(60) """
""" 
def Star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)
Star(5,144)
def addStars(iRange):
    length = 5
    for i in range(iRange):
        Star(length,144)
        length += 5
        t.right(5)
        t.speed(0)
addStars(59) """
turtle.done() 