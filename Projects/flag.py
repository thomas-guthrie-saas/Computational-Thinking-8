import time as wait
import turtle

t = turtle.Turtle()

# setup
t.speed(0)
turtle.Screen().bgcolor("light blue")
x = 50
y = 500
gotox = 0
gotoy = 0
colorset = ""

def color(colorset):
    t.color(colorset)
def goto(gotox, gotoy):
    t.penup()
    t.goto(gotox, gotoy)
    t.pendown()
def stripe(x, y):
    t.begin_fill()
    for i in range(2):
        t.forward(y)
        t.left(90)
        t.forward(x)
        t.left(90)
    t.end_fill()



# stripes

# move to stripe 1
goto(-250, -100)

# stripe 1
color("red")
stripe(x,y)



# move to stripe 2
goto(-250, -50)

# stripe 2
color("white")
stripe(x,y)


# move to stripe 3
goto(-250, 0)

# stripe 3
color("red")
stripe(x,y)


# move to stripe 4
goto(-250, 50)

# stripe 4
color("white")
stripe(x,y)


# move to stripe 5
goto(-250, 100)

# stripe 5
color("red")
stripe(x,y)



# blue square
goto(-250, 50)
color("blue")
t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

turtle.exitonclick()