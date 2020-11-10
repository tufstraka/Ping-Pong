import turtle
import winsound
import random

x = random.randint(-100,100)
y = random.randint(-100,100)

wn = turtle.Screen()
wn.title("TableTennis By @Akashik")
wn.bgpic("Desktop.png")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score_a = 0
score_b = 0


 #Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_a.goto(-380,0)

#Paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_b.goto(380,0)

#Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("circle")
Ball.color("black")
Ball.penup()
Ball.shapesize(stretch_wid=1, stretch_len=0.5)
Ball.goto(0,0)
Ball.dx = 0.1
Ball.dy = 0.1

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24 ) )

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)  


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) 

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)  

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")


#MainGameLoop
while True:
    wn.update()

    #Move the ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Correction
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy += -0.2
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)

    if Ball.ycor() < -290:
        Ball.sety(-290)   
        Ball.dy += 0.2
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)

        
    if Ball.xcor() > 390:
        Ball.goto(x,y)
        Ball.dx += -0.2
        score_a += 1
        pen.clear()
        pen.write("Player A:{} Player B:{} ".format(score_a, score_b), align="center", font=("Courier",24 ) )
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)


    if Ball.xcor() < -390:
        Ball.goto(x,y) 
        Ball.dx += 0.2
        score_b += 1
        pen.clear()
        pen.write("Player A:{} Player B:{} ".format(score_a, score_b), align="center", font=("Courier",24 ) )
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)


    #Paddle and Ball Collision
    if (Ball.xcor() > 370 and Ball.xcor() < 380)  and (Ball.ycor() < paddle_b.ycor()  + 50 and Ball.ycor() > paddle_b.ycor() - 50 ):
        Ball.setx(370)
        Ball.dx *= -1 
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)


    if Ball.xcor() < -370  and (Ball.ycor() < paddle_a.ycor()  + 50 and Ball.ycor() > paddle_a.ycor() - 50 ):
        Ball.setx(-370)
        Ball.dx *= -1
        winsound.PlaySound("Bounce (online-audio-converter.com).wav", winsound.SND_ASYNC)








    