#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.up()

turtle.left(270)

turtle.goto(-15,108)


turtle.pensize(3)

turtle.color("red")

turtle.up()

turtle.down()

turtle.begin_fill()

turtle.circle(4)

turtle.end_fill() #end of left eye

turtle.up()

turtle.left(90)

turtle.forward(55)

turtle.left(90)

turtle.forward(13)

turtle.down()

turtle.begin_fill()

turtle.circle(4)

turtle.end_fill() #end of right eye

turtle.up()

turtle.goto(111,-90)

turtle.left(90)

turtle.forward(45)

turtle.color("brown")

turtle.pensize(10)

turtle.right(200)

turtle.left(90)

turtle.down()

turtle.forward(50)

turtle.up() #end of blunt

turtle.color("orange")

turtle.pensize(5)

turtle.down()

turtle.begin_fill()

turtle.circle(3)

turtle.end_fill()

turtle.color("red")

turtle.pensize(3)

turtle.begin_fill()

turtle.circle(2)

turtle.end_fill()

turtle.up()

turtle.goto(146,-33)

turtle.left(45)

turtle.color("green")

turtle.right(15)

turtle.pensize(20)

turtle.down()

turtle.forward(50)

turtle.backward(50)

turtle.up()

turtle.left(10)

turtle.down()

turtle.begin_fill()

turtle.pensize(15)

turtle.forward(150)

turtle.right(90)

turtle.forward(190)

turtle.right(90)

turtle.forward(150)

turtle.right(90)

turtle.forward(190)

turtle.end_fill()

turtle.up()

turtle.color("black")

turtle.right(90)

turtle.forward(100)

turtle.forward(30)

turtle.right(180)

turtle.pensize(4)

turtle.down()

turtle.forward(20)

turtle.forward(15)

turtle.left(90)

turtle.forward(50)

turtle.left(90)

turtle.forward(40)

turtle.left(180)

turtle.forward(100)

turtle.up()

turtle.left(90)

turtle.forward(10)

turtle.forward(5)

turtle.down()

turtle.forward(10)

turtle.forward(10)

turtle.forward(15)

turtle.backward(35)

turtle.left(90)

turtle.forward(20)

turtle.forward(10)

turtle.right(90)

turtle.forward(35)

turtle.left(90)

turtle.forward(40)

turtle.forward(10)

turtle.forward(10)

turtle.left(90)

turtle.forward(30)

turtle.up()

turtle.right(180)

turtle.forward(80)

turtle.backward(15)

turtle.down()

turtle.forward(10)

turtle.forward(20)

turtle.forward(5)

turtle.right(90)

turtle.forward(50)

turtle.forward(20)

turtle.forward(10)

turtle.forward(10)

turtle.right(90)

turtle.forward(50)

turtle.right(90)

turtle.forward(90)

turtle.right(90)

turtle.forward(20)

turtle.up()

turtle.goto(111,-90)

turtle.left(90)

turtle.forward(30)

turtle.forward(20)

turtle.forward(10)

turtle.forward(5)

turtle.color("white")

turtle.left(30)

turtle.forward(20)

turtle.pensize(2)

turtle.begin_fill()

turtle.down()

turtle.begin_fill()

turtle.forward(5)

turtle.forward(10)

turtle.right(20)

turtle.right(30)

turtle.forward(10)

turtle.forward(5)

turtle.left(45)

turtle.forward(15)

turtle.forward(5)

turtle.right(45)

turtle.forward(20)

turtle.forward(8)

turtle.right(40)

turtle.forward(15)

turtle.right(40)

turtle.right(40)

turtle.forward(20)

turtle.right(45)

turtle.right(45)

turtle.forward(20)

turtle.left(45)

turtle.forward(10)

turtle.right(45)

turtle.right(45)

turtle.right(180)

turtle.forward(8)

turtle.right(90)

turtle.forward(30)

turtle.left(90)

turtle.left(90)

turtle.left(90)

turtle.left(45)

turtle.left(5)

turtle.forward(8)

turtle.forward(5)

turtle.forward(3)

turtle.end_fill()






#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
