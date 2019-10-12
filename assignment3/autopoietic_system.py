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

# random_pos_x = random.randint( (-area_length//2)+ (grid_length//2) ,(area_length//2)- (grid_length//2) )
# catalyst_pos_x = random_pos_x - (random_pos_x % (grid_length//2) )
# random_pos_y = random.randint( (-area_length//2)+ (grid_length//2) ,(area_length//2)- (grid_length//2) )
# catalyst_pos_y = random_pos_y - (random_pos_y % (grid_length//2) )

# # Catalyst shouldn't spawn on intersection of grid lines
# if (catalyst_pos_x % grid_length) == 0:
#     catalyst_pos_x = catalyst_pos_x + (grid_length//2)
# if (catalyst_pos_y % grid_length) == 0:
#     catalyst_pos_y = catalyst_pos_y + (grid_length//2)   

catalyst_pos_x = -60
catalyst_pos_y = -100
catalyst_index = 23
catalyst.setposition(catalyst_pos_x,catalyst_pos_y)


## Spawn Substrates
substrate_number = (area_length//grid_length)**2 - 1   #-1 is due to catalyst
substrates = []

substrate_number = 4
for i in range(4):
    substrates.append(turtle.Turtle())



# for i in range(substrate_number+1):
#    substrates.append(turtle.Turtle())

for substrate in substrates:
    substrate.penup()
    substrate.speed(10)
    substrate.shape("circle")
    substrate.color("green")

substrates[0].setposition(-60,-140)
substrates[1].setposition(-100,-100)
substrates[2].setposition(-100,-60)
substrates[3].setposition(-20,-60)



# Numbers start from bottom left. For example,
# ......
# substrate 11 - substrate 12 - ... substrate 20  <-- one above of last room in the screen
# subsrate 1   - substrate 2  - ... substrate 10  <-- last row in the screen 
# subst_index = 0
# for y in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
#     for x in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
#         if ( x == catalyst_pos_x) and ( y == catalyst_pos_y):
#             catalyst_index = subst_index
#             substrates[subst_index].hideturtle()
#             subst_index += 1 
#             continue
#         else:            
#             substrates[subst_index].setposition(x,y)
#             subst_index += 1


## Production (Number 4 in Paper Appendix)    

def check_substrate_neighbors(n,current_grid,substrates,substrate_number,catalyst_index,grid_shift):
    # This function checks whether current_grid's neighbors contain substrate and returns
    # index of neighbor grids that contain substrates  

    for i in range(substrate_number):
        if ( substrates[i].xcor() == current_grid.xcor() ) and ( substrates[i].ycor() == (current_grid.ycor() + grid_length)):
            n.append(catalyst_index+grid_shift) # north of catalyst is occupied
        if ( substrates[i].xcor() == current_grid.xcor() ) and ( substrates[i].ycor() == (current_grid.ycor() - grid_length)):
            n.append(catalyst_index-grid_shift) # south of catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() + grid_length) ) and (substrates[i].ycor() == current_grid.ycor() ):
            n.append(catalyst_index +1) # east of catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() - grid_length) ) and (substrates[i].ycor() == current_grid.ycor() ):
            n.append(catalyst_index -1) # west of catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[i].ycor() == (current_grid.ycor() + grid_length)):
            n.append(catalyst_index + grid_shift +1) # north-east of catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[i].ycor() == (current_grid.ycor() + grid_length)):
            n.append(catalyst_index + grid_shift -1) # north-west catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[i].ycor() == (current_grid.ycor() - grid_length)):
            n.append(catalyst_index-grid_shift + 1) # south-east catalyst is occupied
        if ( substrates[i].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[i].ycor() == (current_grid.ycor() - grid_length)):
            n.append(catalyst_index-grid_shift -1) # south-west of catalyst is occupied

    return n
    
                            #total_y_grid_number works as well since grids are square

def delete_nonadjacent_neighbors(n,catalyst_index,total_x_grid_number):
    if catalyst_index - total_x_grid_number -1 in n: #south-west neighbor
        if (catalyst_index-1 not in n) and (catalyst_index - total_x_grid_number not in n):
            n.remove(catalyst_index - total_x_grid_number -1 )
    if catalyst_index - total_x_grid_number in n: #south
        if (catalyst_index-1-total_x_grid_number not in n) and (catalyst_index - total_x_grid_number+1 not in n):
            n.remove(catalyst_index - total_x_grid_number)
    if catalyst_index - total_x_grid_number +1 in n: #south-east
        if (catalyst_index-total_x_grid_number not in n) and (catalyst_index +1 not in n):
            n.remove(catalyst_index - total_x_grid_number +1)
    if catalyst_index -1 in n: #west
        if (catalyst_index-1-total_x_grid_number not in n) and (catalyst_index +total_x_grid_number-1 not in n):
            n.remove(catalyst_index -1)
    if catalyst_index +1 in n: #east
        if (catalyst_index+1-total_x_grid_number not in n) and (catalyst_index +total_x_grid_number+1 not in n):
            n.remove(catalyst_index +1)
    if catalyst_index +total_x_grid_number -1 in n: #north-west
        if (catalyst_index-1 not in n) and (catalyst_index +total_x_grid_number not in n):
            n.remove(catalyst_index +total_x_grid_number -1)
    if catalyst_index +total_x_grid_number in n: #north
        if (catalyst_index-1+total_x_grid_number not in n) and (catalyst_index +total_x_grid_number+1 not in n):
            n.remove(catalyst_index +total_x_grid_number)
    if catalyst_index +total_x_grid_number +1 in n: #north-east
        if (catalyst_index+1 not in n) and (catalyst_index +total_x_grid_number not in n):
            n.remove(catalyst_index +total_x_grid_number +1)

    

        


# Find neighbor substrates to catalyst
n1 = [] # occupied neighbor's index
n1 = check_substrate_neighbors(n1,catalyst,substrates,substrate_number,catalyst_index,area_length//grid_length)

delete_nonadjacent_neighbors(n1,catalyst_index, area_length//grid_length)





#for i in range(substrate_number):
    # if ( substrates[i].xcor() == catalyst.xcor() ) and ( substrates[i].ycor() == (catalyst.ycor() + grid_length)):
    #     n.append(i) # north of catalyst is occupied
    # if ( substrates[i].xcor() == catalyst.xcor() ) and ( substrates[i].ycor() == (catalyst.ycor() - grid_length)):
    #     n.append(i) # south of catalyst is occupied
    # if ( substrates[i].xcor() == (catalyst.xcor() + grid_length) ) and (substrates[i].ycor() == catalyst.ycor() ):
    #     n.append(i) # east of catalyst is occupied
    # if ( substrates[i].xcor() == (catalyst.xcor() - grid_length) ) and (substrates[i].ycor() == catalyst.ycor() ):
    #     n.append(i) # west of catalyst is occupied

print("Oh yeah")



input("Press Any Key to Execute the Program")
