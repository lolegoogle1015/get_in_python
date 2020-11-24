#Simple Pong
#By @TokyoEdTech

import turtle
import time

# Screen ( Window)

screen = turtle.Screen()
screen.setup(width=800, height=(600)
screen.bgpic('sky.gif')
time.sleep(2)
screen.update()


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.5
ball.dy = 0.5

# Score
score_a = 0
score_b = 0

def player_score():
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: {}".format(score_b), align="center", font=("Courier", 24, "normal"))

# Function

def paddle_a_up():
    y = paddle_a.ycor() #return y coordinate
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() #return y coordinate
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #return y coordinate
    y += 10
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() #return y coordinate
    y -= 10
    paddle_b.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")




#Main game loop

while True:
    wn.update()



    # Move the Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    if ball.ycor() > 200:
        ball.sety(200)
        ball.dy*= -1


    if ball.ycor() < -200:
        ball.sety(-200)
        ball.dy*= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
    player_score()

    # PAddle and ball collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
