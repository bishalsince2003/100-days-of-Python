from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.fd(10)
def move_backwards():
    tim.bk(10)
def move_left():
    new_heading = tim.heading() + 45
    tim.setheading(new_heading)
    tim.fd(10)
def move_right():
    new_heading = tim.heading() - 45
    tim.setheading(new_heading)
    tim.fd(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    


screen.listen()
screen.onkey(move_forwards,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()
