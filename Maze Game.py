import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Keith's Maze") 
wn.setup(700,700)

#Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.