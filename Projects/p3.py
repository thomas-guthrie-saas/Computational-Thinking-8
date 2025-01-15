# import
import time as wait
import turtle
import random

# define vars
r = random.randint(0,9)
x = 0

t = turtle.Turtle()
t.speed(10)

t.color("black")
turtle.Screen().bgcolor("black")

# define colors
colors = ["red","blue", "black"]

#start loop
for i in range(1000):
    t.color(colors[i%3])
    t.forward(i)
    r = random.randint(0,9)
    x + (i/100)
    t.left(91 + (x/100))
wait.sleep(5)


turtle.exitonclick()