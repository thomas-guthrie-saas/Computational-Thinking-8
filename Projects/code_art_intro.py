# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()

x = 200
y = 72

for i in range(5):
    t.forward(x)
    t.left(y)

while True:
    t.forward(x)
    print(x)
    t.left(y)
    x -= (1 * i)
    print(x)
    y += .1



# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
