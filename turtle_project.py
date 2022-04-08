# Authors: CRS and MB and RJL 03/28/22
# Import turtle
import turtle
from threading import Timer

# Set up for tody to fill in shapes
toby_table = []

# Set up for steven to fill in shapes
steven_table = []

# Claimed areas
claimed = []

# Create Screen
window = turtle.Screen()

# Turtles
toby = turtle.Turtle()
steven = turtle.Turtle()
endTurtle = turtle.Turtle()
window.setup(1000, 1000)
window.screensize(1000, 1000)

#creates border
bdr = turtle.Turtle()
bdr.speed(0)
bdr.penup()
bdr.back(350)
bdr.pendown()
bdr.left(90)
bdr.forward(350)
bdr.right(90)
for i in range(3):
    bdr.forward(700)
    bdr.right(90)
bdr.forward(350)
bdr.hideturtle()

# Player 1 Input of Shape of toby and Color
def change_color_p1(color):
    toby.pencolor(color)
    toby.fillcolor(color)
def change_shape_p1(shape):
    toby.shape(shape)

change_color_p1(window.textinput("color", "enter a color for Player 1"))
change_shape_p1(window.textinput("shape", "enter a shape for Player 1"))

# Player 2 Input of shape of steven and Color
def change_color_p2(color):
    steven.fillcolor(color)
    steven.pencolor(color)
def change_shape_p2(shape):
    steven.shape(shape)


change_color_p2(window.textinput("color", "enter a color for Player 1"))
change_shape_p2(window.textinput("shape", "enter a shape for Player 1"))


# Begin and end filling
toby.begin_fill()
steven.begin_fill()

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
    for x in range(len(toby_table)):
        if int(toby.xcor()) == toby_table[x][0] and int(toby.ycor()) == toby_table[x][1]:
            toby.end_fill()
            toby.begin_fill()
        elif toby.xcor() > 450 or toby.ycor() > 400:
            toby.back(10)

def collision_p2():
    for x in range(len(steven_table)):
        if int(steven.xcor()) == steven_table[x][0] and int(steven.ycor()) == steven_table[x][1]:
            steven.end_fill()
            steven.begin_fill()
        elif steven.xcor() > 450 or steven.ycor() > 400:
            steven.back(10)

def endGame():
    turtle.Turtle.write("GAME OVER!")

# Define Left Player 2 Function
def left_p2():
    steven.left(90)

# Define Right Player 2 Function
def right_p2():
    steven.right(90)

# Define Left Player 1 Function
def left_p1():
    toby.left(90)

# Define Right Player 1 Function
def right_p1():
    toby.right(90)


def move():
    moving = True
    while moving:
        toby.forward(5)

        steven.forward(5)

        # Make Player 1 Move
        window.onkey(left_p1, "a")
        window.onkey(right_p1, "d")

        # Make Player 2 Move
        window.onkey(left_p2, "Left")
        window.onkey(right_p2, "Right")

        window.listen()

        collision_p1()
        toby_table.append([int(toby.xcor()),int(toby.ycor())])

        collision_p2()
        steven_table.append([int(steven.xcor()),int(toby.ycor())])

# TIMER OMEGALUL
t = Timer(interval=5.0,function=endGame)
t.start()

move()