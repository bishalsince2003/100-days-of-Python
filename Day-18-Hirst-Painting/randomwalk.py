import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


tim.shape("turtle")
tim.pensize(10)
tim.speed("fastest")

colours = [ "red" , "yellow" , "violet" , "green" , "pink" ,"blue" , "orange" ,"maroon" , "brown"]

# def direct():
#     direction = random.choice(["right" , "left"])

#     if direction == "left":
#         tim.left(90)
#     else:
#         tim.right(90)



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) 

direction=[0,90,180,270]

for _ in range(200):
    tim.color(random_color())
    # tim.color(random.choice(colours))
    tim.forward(30)
    # direct()
    tim.setheading(random.choice(direction))



screen = t.Screen()
screen.exitonclick()