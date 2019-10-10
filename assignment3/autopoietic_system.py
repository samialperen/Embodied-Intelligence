##### Author: Sami Alperen Akgun
#### University of Waterloo, ECE Department

# Python Turtle Graphics Module 
import turtle

## Adjust Display
disp = turtle.Screen()
disp.bgcolor("gold")

## Draw rectangular boundary for simulation area
pen = turtle.Turtle()
pen.penup()
pen.setposition(-300,-300)
pen.pensize(3)
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()


## Spawn catalyst
catalyst = turtle.Turtle()
catalyst.color("blue")
catalyst.shape("turtle")
catalyst.penup()

def go_straight():
    catalyst.forward(2)

turtle.listen()
turtle.onkey(go_straight,"Up")







input("Press Any Key to Execute the Program")
