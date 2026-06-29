from turtle import Turtle,Screen
import random
tim = Turtle()
tim.shape("turtle")


colours = [ "red" , "yellow" , "violet" , "green" , "pink" ,"blue" , "orange"]
n=3
while n<12:
    tim.color(random.choice(colours))
    for _ in range (n):
        tim.forward(50)
        tim.right(360/n)
    n+=1

sc = Screen()
sc.bgcolor("black")
sc.exitonclick()