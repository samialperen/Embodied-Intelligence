##### Author: Sami Alperen Akgun
#### University of Waterloo, ECE Department

import turtle # Python Turtle Graphics Module 
import random 

## Adjust Display
disp = turtle.Screen()
disp.bgcolor("gold")

## Draw rectangular boundary and grids
grid_length = 40
area_length = 400

pen = turtle.Turtle()
pen.speed(10)
pen.penup()

def draw_main_square(length):
    pen.setposition(-length/2,-length/2)
    pen.pensize(3)
    pen.pendown()
    for i in range(4):
        pen.forward(length)
        pen.left(90)
    pen.penup()

def draw_vertical_lines(width,length):
    pen.setposition(-length/2,-length/2)
    pen.pendown()
    for i in range( int(length/(2*grid_length)) ):
        pen.forward(width)
        pen.left(90)        
        pen.forward(length)
        pen.right(90)
        pen.forward(width)
        pen.right(90)
        pen.forward(length)
        pen.left(90)
    pen.penup()

def draw_horizontal_lines(height,length):
    pen.setposition(-length/2,-length/2)
    pen.left(90)
    pen.pendown()
    for i in range ( int(length/(2*grid_length)) ):
        pen.forward(height)
        pen.right(90)
        pen.forward(length)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
        pen.forward(length)
        pen.right(90)
    pen.penup()


draw_main_square(area_length)
draw_vertical_lines(grid_length,area_length)
draw_horizontal_lines(grid_length,area_length)
pen.hideturtle()


## Spawn catalyst in a random position
catalyst = turtle.Turtle()
catalyst.penup()
catalyst.color("blue")
catalyst.shape("turtle")

random_pos_x = random.randint( (-area_length//2)+ (grid_length//2) ,(area_length//2)- (grid_length//2) )
catalyst_pos_x = random_pos_x - (random_pos_x % (grid_length//2) )
random_pos_y = random.randint( (-area_length//2)+ (grid_length//2) ,(area_length//2)- (grid_length//2) )
catalyst_pos_y = random_pos_y - (random_pos_y % (grid_length//2) )

# Catalyst shouldn't spawn on intersection of grid lines
if (catalyst_pos_x % grid_length) == 0:
    catalyst_pos_x = catalyst_pos_x + (grid_length//2)
if (catalyst_pos_y % grid_length) == 0:
    catalyst_pos_y = catalyst_pos_y + (grid_length//2)   

catalyst.setposition(catalyst_pos_x,catalyst_pos_y)


## Spawn Substrates
substrate_number = (area_length//grid_length)**2 - 1   #-1 is due to catalyst
substrates = []
for i in range(substrate_number):
    substrates.append(turtle.Turtle())

for substrate in substrates:
    substrate.penup()
    substrate.speed(10)
    substrate.shape("circle")
    substrate.color("green")

# Numbers start from bottom left. For example,
# ......
# substrate 11 - substrate 12 - ... substrate 20  <-- one above of last room in the screen
# subsrate 1   - substrate 2  - ... substrate 10  <-- last row in the screen 
subst_index = 0
for y in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
    for x in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
        if ( x == catalyst_pos_x) and ( y == catalyst_pos_y):
            continue
        else:            
            substrates[subst_index].setposition(x,y)
            subst_index += 1


## Production (Number 4 in Paper Appendix)    

# Find neighbor substrates to catalyst
n = [] # occupied neighbor's index
for i in range(substrate_number):
    if ( substrates[i].xcor() == catalyst.xcor() ) and ( substrates[i].ycor() == (catalyst.ycor() + grid_length)):
        n.append(i) # north of catalyst is occupied
    if ( substrates[i].xcor() == catalyst.xcor() ) and ( substrates[i].ycor() == (catalyst.ycor() - grid_length)):
        n.append(i) # south of catalyst is occupied
    if ( substrates[i].xcor() == (catalyst.xcor() + grid_length) ) and (substrates[i].ycor() == catalyst.ycor() ):
        n.append(i) # east of catalyst is occupied
    if ( substrates[i].xcor() == (catalyst.xcor() - grid_length) ) and (substrates[i].ycor() == catalyst.ycor() ):
        n.append(i) # west of catalyst is occupied


print("Oh yeah")


input("Press Any Key to Execute the Program")
