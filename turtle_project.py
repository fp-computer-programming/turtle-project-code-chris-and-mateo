# Authors: CRS and MB and RJL 03/28/22
# Import turtle
import turtle

# Set up for tody to fill in shapes
toby_table = []

# Set up for steven to fill in shapes
steven_table = []

# Create Screen
window = turtle.Screen()

# Turtles
toby = turtle.Turtle()
steven = turtle.Turtle()
window.setup(1000, 1000)
window.screensize(1000, 1000)

# Player Input of Shape of Turtle and Color


# Begin and end filling
toby.begin_fill()
toby.end_fill()
steven.begin_fill()
steven.end_fill()

# Set Position of Toby
toby.penup()
toby.goto(-200, 0)
toby.pendown()

# Set Position of Steven
steven.penup()
steven.goto(200, 0)
steven.pendown()

# Define Forward Player 1 Function
def forward_p1():
    # Plot the pos in the table for checking later
    toby_table.append(toby.pos())
    toby.forward(50)
    # Check if the player hits the line (COLLISION LOGIC LOLOLOL)
    if len(toby_table) > 1:
        print(len(toby_table))
        for index,positions in enumerate(toby_table):
            X_startingPos = toby_table[index-1][0]
            X_endPos = toby_table[index][0]

            y_startingPos = toby_table[index-1][1]
            y_endPos = toby_table[index][1]

            turtlePos = list(toby.pos())
            x_turtlePos = turtlePos[0]
            y_turtlePos = turtlePos[1]

            if x_turtlePos > X_startingPos and x_turtlePos < X_endPos:
                print("between")
            elif x_turtlePos == X_startingPos and x_turtlePos == X_endPos:
                if y_turtlePos > y_startingPos and y_turtlePos < y_endPos:
                    print("between")


# Define Left Player 1 Function
def left_p1():
    toby.left(90)

# Define Right Player 1 Function
def right_p1():
    toby.right(90)

# Define Forward Player 2 Function
def forward_p2():
    # Plot the pos in the table for checking later
    steven_table.append(steven.position())
    steven.forward(50)



# Define Left Player 2 Function
def left_p2():
    steven.left(90)

# Define Right Player 2 Function
def right_p2():
    steven.right(90)

# Make Player 1 Move
window.onkey(forward_p1, "w")
window.onkey(left_p1, "a")
window.onkey(right_p1, "d")

# Make Player 2 Move
window.onkey(forward_p2, "Up")
window.onkey(left_p2, "Left")
window.onkey(right_p2, "Right")

# Make sure window doesn't close
window.listen()
window.mainloop()