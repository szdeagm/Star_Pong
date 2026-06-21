from turtle import *
import random

def tela():
    title("Star Pong")
    setup(width = 800, height = 600)
    bgcolor("black")
    goto(-380, -250)
    hideturtle()
    speed(0)
    width(3)
    color("white")
    for i in range(2):
        forward(760)
        left(90)
        forward(500)
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
    if y < 160:
        tluke.sety(y + 20)

def luke_down():
    y = tluke.ycor()
    if y > -160:
        tluke.sety(y - 20)

darth = Turtle()

darth.shape("square")
darth.color("red")
darth.shapesize(stretch_wid=8, stretch_len=1)
darth.penup()
darth.speed(0)
darth.goto(360, 0) 

def placar():
    p = Turtle()
    p.hideturtle()
    p.color("white")
    p.penup()
    p.goto(-250, -285)
    p.speed(0)
    p.write("Jogador 1: 0 | Jogador 2: 0", font = ("Courrier", 13, "bold"), align = "center")
    
b = Turtle()
def bola():
    b.shape("circle")
    b.color("pink")
    b.penup()
    b.goto(0,0)
    b.dx = 0
    b.dy = 0

tela()
placar()
bola()

listen()

#teclas
onkeypress(luke_up, "Up")
onkeypress(luke_down, "Down")
done()

