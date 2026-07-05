from turtle import Turtle,Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# position=[(0,0),(-20,0),(-40,0)]
# turtle_list = []

# for i in position:
#     new_turtle = Turtle()
#     new_turtle.penup()
#     new_turtle.color("white")
#     new_turtle.shape("square")
#     new_turtle.goto(i)
#     turtle_list.append(new_turtle)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

is_game_on= True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # for segment in range(len(turtle_list)-1 , 0 , -1):        
    #     new_x = turtle_list[segment-1].xcor()
    #     new_y = turtle_list[segment-1].ycor()
    #     turtle_list[segment].goto(new_x,new_y)
    # turtle_list[0].fd(20)
    # turtle_list[0].left(90)



screen.exitonclick()