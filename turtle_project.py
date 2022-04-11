# Authors: CRS and MB and RJL 03/28/22
# Import turtle
import turtle
from random import randrange
from threading import Timer

# Set up for tody to fill in shapes
toby_table = []

# Set up for steven to fill in shapes
steven_table = []

# Powerup Table
powerUpX = []
powerUpY = []

# Claimed areas
claimed = []

# Create Screen
window = turtle.Screen()

# Turtles
tobyP = turtle.Turtle()
stevenP = turtle.Turtle()
endTurtle = turtle.Turtle()
toby = turtle.Turtle()
steven = turtle.Turtle()
powerUp = turtle.Turtle()

# Window
window.setup(1000,1000)
window.screensize(1000, 1000)

# Scoreboard
tobyP.penup()
tobyP.hideturtle()
tobyP.setposition(-400,440)
tobyP.write("TOBY: 0",font=("Vernanda",20,"normal"))

stevenP.penup()
stevenP.hideturtle()
stevenP.setposition(300,440)
stevenP.write("STEVEN: 0",font=("Vernanda",20,"normal"))

# Vars
moving = True
canPowerUp = True
notTaken = True
steven_points = 0
toby_points = 0

#creates border
bdr = turtle.Turtle()
bdr.speed(0)
bdr.penup()
bdr.setposition(-475,-475)
bdr.pendown()
bdr.pencolor("purple")
bdr.pensize(10)
for side in range(4):
    bdr.forward(950)
    bdr.left(90)
bdr.hideturtle()

endTurtle.penup()
endTurtle.setposition(-100,-100)
endTurtle.hideturtle()

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
    global toby_points
    global powerUp
    global notTaken
    for x in range(len(toby_table)):
        if int(toby.xcor()) == toby_table[x][0] and int(toby.ycor()) == toby_table[x][1]:
            toby.end_fill()
            toby.begin_fill()
            toby_points += 1
            tobyPoints()
        elif toby.xcor() > 450 or toby.ycor() > 450 or toby.xcor() < -450 or toby.ycor() < -450:
            toby.right(180)
            toby.forward(20)
        try:
            if toby.xcor() > powerUpX[0] and notTaken or toby.ycor > powerUpY[0] and notTaken:
                notTaken = False
                powerUp.hideturtle()
                powerUp.pendown()
                powerUp.begin_fill()
                for x in range(4):
                    powerUp.forward(250)
                    powerUp.left(90)
                powerUp.end_fill()
                toby_points += 10
        except:
           print

def collision_p2():
    global steven_points
    global powerUp
    global notTaken
    for x in range(len(steven_table)):
        if int(steven.xcor()) == steven_table[x][0] and int(steven.ycor()) == steven_table[x][1]:
            steven.end_fill()
            steven.begin_fill()
            steven_points += 1
            stevenPoints()
        elif steven.xcor() > 450 or steven.ycor() > 450 or steven.xcor() < -450 or steven.ycor() < -450:
            steven.right(180)
            steven.forward(20)
        try:
            if steven.xcor() > powerUpX[0] and notTaken or steven.ycor > powerUpY[0] and notTaken:
                notTaken = False
                powerUp.hideturtle()
                powerUp.pendown()
                powerUp.begin_fill()
                for x in range(4):
                    powerUp.forward(250)
                    powerUp.left(90)
                powerUp.end_fill()
                steven_points += 10
        except:
           print

def endGame():
    global moving
    moving = False

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

def tobyPoints():
    global toby_points
    tobyP.reset()
    tobyP.hideturtle()
    tobyP.speed(0)
    tobyP.penup()
    tobyP.setposition(-400,440)
    tobyP.write("TOBY: "+str(toby_points),font=("Vernanda",20,"normal"))

def stevenPoints():
    global steven_points
    stevenP.reset()
    stevenP.hideturtle()
    stevenP.speed(0)
    stevenP.penup()
    stevenP.setposition(300,440)
    stevenP.write("STEVEN: "+str(steven_points),font=("Vernanda",20,"normal"))

def powerup():
    global canPowerUp
    global powerUp
    if canPowerUp and toby_points > 5 or canPowerUp and steven_points > 5:
        canPowerUp = False
        powerUp.penup()
        powerUp.turtlesize(1)
        powerUp.shape(name="square")
        x = randrange(-300,300,1)
        y = randrange(-300,300,1)
        powerUp.setposition(x,y)
        powerUp.write("BOMB POWERUP!",font=("Vernanda",15,"normal"))
        powerUpX.append(x)
        powerUpY.append(y)

def move():
    global moving
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

        powerup()

    if toby_points > steven_points:
        endTurtle.write("GAME OVER!\n"+"TOBY HAS WON!",font=("Vernanda",35,"normal"))
    elif toby_points < steven_points:
        endTurtle.write("GAME OVER!\n"+"STEVEN HAS WON!",font=("Vernanda",35,"normal"))
    else:
        endTurtle.write("GAME OVER!\n"+"NOBODY HAS WON!",font=("Vernanda",35,"normal"))
    window.mainloop()

# TIMER OMEGALUL
t = Timer(interval=30.0,function=endGame)
t.start()

move()