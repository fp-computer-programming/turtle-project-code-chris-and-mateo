# Authors: CRS and MB 03/28/22
# Import turtle
import turtle

# Create Turtles and Screen
window = turtle.Screen()
toby = turtle.Turtle()
steven = turtle.Turtle()
window.setup(1000, 1000)
window.screensize(1000, 1000)
toby.color("Red")
steven.color("Blue")

# Begin and end filling
toby.begin_fill()
toby.end_fill()
steven.begin_fill()
steven.end_fill()

# Set Position of Turtles
toby.goto(-200, 0)
steven.goto(200, 0)

# Define Forward Player 1 Function
def forward_p1():
    toby.forward(50)

# Define Left Player 1 Function
def left_p1():
    toby.left(90)

# Define Right Player 1 Function
def right_p1():
    toby.right(90)

# Define Forward Player 2 Function
def forward_p2():
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