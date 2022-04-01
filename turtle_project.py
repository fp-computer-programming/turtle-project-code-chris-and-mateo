# Authors: CRS and MB and RJL 03/28/22
# Import turtle
from calendar import c
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

# Player 1 Input of Shape of toby and Color
# def change_color_p1(color):
#     toby.pencolor(color)
# def change_shape_p1(shape):
#     toby.shape(shape)

# change_color_p1(window.textinput("color", "enter a color for Player 1"))
# change_shape_p1(window.textinput("shape", "enter a shape for Player 1"))

# # Player 2 Input of shape of steven and Color
# def change_color_p2(color):
#     steven.pencolor(color)
# def change_shape_p2(shape):
#     steven.shape(shape)

# change_color_p2(window.textinput("color", "enter a color for Player 1"))
# change_shape_p2(window.textinput("shape", "enter a shape for Player 1"))


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

# Collision
def collision_p1():
    print()

# Define Forward Player 1 Function
def forward_p1():
    # Plot the pos in the table for checking later
    for x in range(10):
        toby_table.append(toby.pos())
        toby.forward(x)
        # Check if the player hits the line (COLLISION LOGIC LOLOLOL)
        collision_p1()


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
