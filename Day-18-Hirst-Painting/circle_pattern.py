import turtle as t 
import random
timmy = t.Turtle()
t.colormode(255)
# timmy.shape("turtle")
timmy.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b) 

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap) ):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + size_of_gap)

draw_spirograph(1)


display = t.Screen()
display.exitonclick()
 
