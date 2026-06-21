from turtle import *
import random

jogador1 = 0
jogador2 = 0

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

p = Turtle()
def placar():
    p.hideturtle()
    p.color("white")
    p.penup()
    p.goto(-250, -285)
    p.speed(0)
    p.write(f"Jogador 1: {jogador1}  |  Jogador 2: {jogador2}", font = ("Courrier", 13, "bold"), align = "center")
    
b = Turtle()
def bola():
    b.shape("circle")
    b.color("pink")
    b.penup()
    b.goto(0,0)
    b.dx = 6
    b.dy = 6

def bola_mov():
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)
    global jogador1, jogador2

    if b.ycor() > 250:
        b.sety(250)
        b.dy *= -1
    if b.ycor() < -250:
        b.sety(-250)
        b.dy *= -1
    if b.xcor() > 370:
        b.goto(0,0)
        b.dx *= -1
        jogador1 += 1
        p.clear()
        p.write(f"Jogador 1:{jogador1}  | Jogador 2: {jogador2}", font = ("Courrier", 13, "bold"), align = "center")
    if b.xcor() < -370:
        b.goto(0,0)
        b.dx *= -1
        jogador2 += 1
        p.clear()
        p.write(f"Jogador 1:{jogador1}  | Jogador 2: {jogador2}", font = ("Courrier", 13, "bold"), align = "center")
    if (b.xcor() < -350 and b.xcor() > -370) and (b.ycor() < tluke.ycor() + 80 and b.ycor() > tluke.ycor() - 80):
        b.setx(370)
        b.dx *= -1
    if (b.xcor() < 350 and b.xcor() > 370) and (b.ycor() < darth.ycor() + 80 and b.ycor() > darth.ycor() - 80):
        b.setx(-370)
        b.dx *= -1

    update()
    ontimer(bola_mov, 10)

tela()
placar()
bola()
listen()

#teclas
onkeypress(luke_up, "Up")
onkeypress(luke_down, "Down")

#loop do jogo

bola_mov()   
done()

