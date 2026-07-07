from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard =Scoreboard()

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

    #Detect collision with food
    if snake.turtle_list[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() >280 or snake.head.ycor() < -280 :
        is_game_on=False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment)<10:
            is_game_on=False
            scoreboard.game_over()
    #if head collides with any segment in the tail:
        #trigger GAME OVER 

screen.exitonclick()