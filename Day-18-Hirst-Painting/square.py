from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.speed("slow")
for i in range(4):
    timmy.forward(200)
    timmy.right(90)

display = Screen()
display.exitonclick()
 
