from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()
screen.setup(width=800 , height = 600)
screen.bgcolor("black")
screen.title("PING PONG GAME")
screen.tracer(0)

ball= Ball()
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
r_score = Scoreboard((100,230))
l_score = Scoreboard((-100,230))
# paddle = Turtle()
# paddle.penup()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1 , stretch_wid=5)
# paddle.goto(x=350 ,y=0)

# def go_up():
#     new_y = paddle.ycor() + 40
#     paddle.goto(paddle.xcor() , new_y)
# def go_down():
#     new_y = paddle.ycor() - 40
#     paddle.goto(paddle.xcor() , new_y)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down , "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down , "s")

game_is_on= True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()< -280:
        #needs to bounce
        ball.bounce()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()>320  or ball.distance(l_paddle) < 50 and ball.xcor()<-320:
        ball.x_bounce()
        

    #Detect paddle misses the ball 
    if ball.xcor()>380:
        ball.restart()
        l_score.increase_score()
    elif ball.xcor()<-380:
        ball.restart()
        r_score.increase_score()
        




screen.exitonclick()