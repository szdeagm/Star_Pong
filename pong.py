from turtle import *


def tela():
    title("Star Pong")
    setup(width = 800, height = 600)
    bgcolor("black")
    goto(-380, -280)
    hideturtle()
    speed(0)
    width(3)
    color("white")
    for i in range(2):
        forward(760)
        left(90)
        forward(560)
        left(90)

tluke = Turtle()

tluke.shape("square")
tluke.color("lime")
tluke.shapesize(stretch_wid=8, stretch_len=1)
tluke.penup()
tluke.speed(0)
tluke.goto(-360, 0)   

def luke_up():
    y = tluke.ycor()
    if y < 190:
        tluke.sety(y + 20)

def luke_down():
    y = tluke.ycor()
    if y > -190:
        tluke.sety(y - 20)

darth = Turtle()

darth.shape("square")
darth.color("red")
darth.shapesize(stretch_wid=8, stretch_len=1)
darth.penup()
darth.speed(0)
darth.goto(360, 0) 

tela()
listen()
onkeypress(luke_up, "Up")
onkeypress(luke_down, "Down")
done()

