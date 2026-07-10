from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=2,stretch_len=2)
        self.penup()
        # self.goto(x=380, y=280)
        self.x_move=20
        self.y_move=20
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move , self.ycor()+self.y_move)

    def bounce(self):
        self.y_move *= -1
    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.x_bounce()
        # self.move()