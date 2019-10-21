##### Author: Sami Alperen Akgun
#### University of Waterloo, ECE Department

import turtle # Python Turtle Graphics Module 
import random 

## Adjust Display
disp = turtle.Screen()
disp.bgcolor("gold")

global_iteration = 0
#####################################################
## Draw rectangular boundary and grids
grid_length = 40
area_length = 400

pen = turtle.Turtle()
pen.speed(10)
pen.penup()

text_pen = turtle.Turtle()
text_pen.speed(10)
text_pen.penup()

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

def display_global_time(height,length):
    text_pen.setposition(-grid_length,length//2 +grid_length//2)
    text_pen.pendown()
    text_pen.write("T = " +str(global_iteration), font=("Arial", 16,"bold"))
    text_pen.penup()

draw_main_square(area_length)
draw_vertical_lines(grid_length,area_length)
draw_horizontal_lines(grid_length,area_length)
display_global_time(grid_length,area_length)
pen.hideturtle()
text_pen.hideturtle()
#####################################################


#####################################################
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

#catalyst_pos_x = -60
#catalyst_pos_y = -100
#catalyst_index = 23
catalyst.setposition(catalyst_pos_x,catalyst_pos_y)


## Spawn Substrates
substrate_number = (area_length//grid_length)**2 - 1   #-1 is due to catalyst
substrates = []

substrate_number = 99
for i in range(substrate_number+1):
    substrates.append(turtle.Turtle())

for substrate in substrates:
    substrate.penup()
    substrate.speed(10)
    substrate.shape("circle")
    substrate.color("green")

#substrates[13].setposition(-60,-140)
#substrates[22].setposition(-100,-100)
#substrates[32].setposition(-100,-60)
#substrates[34].setposition(-20,-60)

# Numbers start from bottom left. For example,
# ......
# substrate 11 - substrate 12 - ... substrate 20  <-- one above of last room in the screen
# subsrate 1   - substrate 2  - ... substrate 10  <-- last row in the screen 
subst_index = 0
for y in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
    for x in range( (-area_length//2)+ (grid_length//2), (area_length//2) + (grid_length//2), grid_length):
        if ( x == catalyst_pos_x) and ( y == catalyst_pos_y):
            catalyst_index = subst_index
            substrates[subst_index].hideturtle()
            subst_index += 1 
            continue
        else:            
            substrates[subst_index].setposition(x,y)
            subst_index += 1

#####################################################

##################################################### 
def check_substrate_neighbors(current_grid,substrates,substrate_number,catalyst_index,grid_shift,n_holes,n_link,n_bounded_link):
    # This function checks whether current_grid's neighbors contain substrate and returns
    # index of neighbor grids that contain substrates  
    n = []
    for i in range(substrate_number):
        if i in n_holes:
            continue #Do not check holes
        if i in n_link:
            continue #Do not check links
        if i in n_bounded_link:
            continue #Do not check bounded links
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

def create_link(n_link,n_hole,n_subst,substrates):
    # n contains indexes of grids that contain adjacent substrates
    # substrates held all of the substrates in the area    
    global global_iteration
    removed_subst = [] #either removed or turned to link
    i = 0
    while i < len(n_subst)-1:
        if ( n_subst[i+1] - n_subst[i]) == 1:
                substrates[ n_subst[i] ].color("red") #create Link
                substrates[ n_subst[i +1] ].hideturtle() #create hole
                n_link.append(n_subst[i]) #log link grid position
                n_holes.append(n_subst[i+1])
                removed_subst.append(n_subst[i]) #log the substrate grid position so that we don't keep hole index
                removed_subst.append(n_subst[i +1]) #log the substrate grid position so that we don't keep hole index
                i += 2
        else:
            i += 1                  
        input("Press Enter to see next instant")
        # Change iteration time and display it
        global_iteration += 1
        text_pen.clear()
        display_global_time(grid_length,area_length)



    # Delete necessary substrates (either hole or turned to link)
    if len(removed_subst) != 0:
        for i in range(len(removed_subst)):
            n_subst.remove(removed_subst[i])


    removed_subst = [] #either removed or turned to link
    i = 0
    while i < len(n_subst)-1:
        if ( n_subst[i+1] - n_subst[i]) == 10:
                substrates[ n_subst[i] ].color("red") #create Link
                substrates[ n_subst[i +1] ].hideturtle() #create hole
                n_link.append(n_subst[i]) #log link grid position
                n_holes.append(n_subst[i+1])
                removed_subst.append(n_subst[i]) #log the substrate grid position so that we don't keep hole index
                removed_subst.append(n_subst[i +1]) #log the substrate grid position so that we don't keep hole index
                i += 2
        else:
            i += 1

                  
        input("Press Enter to see next instant")
        # Change iteration time and display it
        global_iteration += 1
        text_pen.clear()
        display_global_time(grid_length,area_length)
    # Delete necessary substrates (either hole or turned to link)
    if len(removed_subst) != 0:
        for i in range(len(removed_subst)):
            n_subst.remove(removed_subst[i])



def check_link_neighbors(n_link,substrates,grid_shift,current_ind):
    # This function checks whether current_grid's neighbors contain link and returns
    # index of neighbor grids that contain links
    n_bounded = []
    current_grid = substrates[current_ind]
    for i in range(len(n_link)-1):
        if i in n_holes:
            continue
        if i in n_substrates:
            continue
        if i in n_bounded_link:
            continue
        if ( substrates[ n_link[i] ].xcor() == current_grid.xcor() ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_bounded.append(current_ind+grid_shift) # north of catalyst is occupied
        if ( substrates[n_link[i]].xcor() == current_grid.xcor() ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_bounded.append(current_ind-grid_shift) # south of catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() + grid_length) ) and (substrates[n_link[i]].ycor() == current_grid.ycor() ):
            n_bounded.append(current_ind +1) # east of catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() - grid_length) ) and (substrates[n_link[i]].ycor() == current_grid.ycor() ):
            n_bounded.append(current_ind -1) # west of catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_bounded.append(current_ind + grid_shift +1) # north-east of catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_bounded.append(current_ind + grid_shift -1) # north-west catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_bounded.append(current_ind-grid_shift + 1) # south-east catalyst is occupied
        if ( substrates[n_link[i]].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[n_link[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_bounded.append(current_ind-grid_shift -1) # south-west of catalyst is occupied

    return n_bounded      



def create_bounded_link(current_link_index,neighbor_links,substrates):
    n_bound = []
    substrates[current_link_index].color("blue")
    n_bound.append(current_link_index)
    for i in range(len(neighbor_links)):
        substrates[neighbor_links[i]].color("blue")
        n_bound.append(neighbor_links[i]) 
    return n_bound

def check_hole_neighbors(n_holes,current_grid,substrates,grid_shift):
    # This function checks whether current_grid's neighbors contain holes and returns
    # index of neighbor grids that contain holes  
    n_hole_neighbors = []
    for i in range(len(n_holes)):
        if ( substrates[n_holes[i] ].xcor() == current_grid.xcor() ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_hole_neighbors.append(catalyst_index+grid_shift) # north of catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == current_grid.xcor() ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_hole_neighbors.append(catalyst_index-grid_shift) # south of catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() + grid_length) ) and (substrates[n_holes[i]].ycor() == current_grid.ycor() ):
            n_hole_neighbors.append(catalyst_index +1) # east of catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() - grid_length) ) and (substrates[n_holes[i]].ycor() == current_grid.ycor() ):
            n_hole_neighbors.append(catalyst_index -1) # west of catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_hole_neighbors.append(catalyst_index + grid_shift +1) # north-east of catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() + grid_length)):
            n_hole_neighbors.append(catalyst_index + grid_shift -1) # north-west catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() + grid_length) ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_hole_neighbors.append(catalyst_index-grid_shift + 1) # south-east catalyst is occupied
        if ( substrates[n_holes[i] ].xcor() == (current_grid.xcor() - grid_length) ) and ( substrates[n_holes[i]].ycor() == (current_grid.ycor() - grid_length)):
            n_hole_neighbors.append(catalyst_index-grid_shift -1) # south-west of catalyst is occupied

    return n_hole_neighbors

def move_catalyst(desired_grid,substrates):
    # Instead of mapping grid number to exact position, I use small trick.
    # I am using using substrates to get exact location info
    x_desired = substrates[desired_grid].position()[0]
    y_desired = substrates[desired_grid].position()[1]
    catalyst.goto(x_desired,y_desired)
    global global_iteration
    global_iteration += 1
    text_pen.clear()
    display_global_time(grid_length,area_length)


#####################################################

#####################################################
## Production (Number 4 in Paper Appendix)    
n_substrates = [] # occupied neighbor's index
n_holes = []
n_link = []
n_bounded_link = []

try:
    while True:
        n_substrates = check_substrate_neighbors(catalyst,substrates,substrate_number,catalyst_index,area_length//grid_length,n_holes,n_link,n_bounded_link)
        delete_nonadjacent_neighbors(n_substrates,catalyst_index, area_length//grid_length)

        create_link(n_link,n_holes,n_substrates,substrates)
        n_link_neighbors = []
        for i in range(len(n_link)):
            current_link_ind = n_link[i]
            del n_link[i] #To not check the grid with itself
            n_link_neighbors = check_link_neighbors(n_link,substrates, area_length//grid_length,current_link_ind)
            if len(n_link_neighbors) != 0: #there are neighbor links 
                n_bounded_link = create_bounded_link(current_link_ind,n_link_neighbors,substrates)
            n_link.insert(i,current_link_ind)
        
        n_hole_neighbors = check_hole_neighbors(n_holes,catalyst,substrates,area_length//grid_length)
        if len(n_hole_neighbors) != 0:
            n_holes.append(catalyst_index)
            catalyst_index = random.choice(n_hole_neighbors)
            if catalyst_index in n_holes:
                n_holes.remove(catalyst_index)
            input("Press Enter to see next instant")
            move_catalyst(catalyst_index,substrates)

except KeyboardInterrupt:
    pass






input("Press Any Key to Execute the Program")
