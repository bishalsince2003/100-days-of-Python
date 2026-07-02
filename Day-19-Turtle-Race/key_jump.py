from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)

screen.listen()
screen.onkey(move_forwards,"space")
screen.exitonclick()
