from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE =20
UP = 90 
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :

    def __init__(self):
        self.turtle_list = []
        self.create_snake()

    def create_snake(self):
        for i in STARTING_POSITION:
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.goto(i)
            self.turtle_list.append(new_turtle)

    def move(self):
        for segment in range(len(self.turtle_list)-1 , 0 , -1):        
            new_x = self.turtle_list[segment-1].xcor()
            new_y = self.turtle_list[segment-1].ycor()
            self.turtle_list[segment].goto(new_x,new_y)
        self.turtle_list[0].fd(MOVE_DISTANCE)
        
    
    def up(self):
        if self.turtle_list[0].heading() != DOWN:
            self.turtle_list[0].setheading(UP)

    def down(self):
        if self.turtle_list[0].heading() != UP:    
            self.turtle_list[0].setheading(DOWN)

    def left(self):
        if self.turtle_list[0].heading() != RIGHT:
            self.turtle_list[0].setheading(LEFT)
    def right(self):
        if self.turtle_list[0].heading() != LEFT:
            self.turtle_list[0].setheading(RIGHT)
