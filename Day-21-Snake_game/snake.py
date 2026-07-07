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
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
            

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.goto(position)
        self.turtle_list.append(new_turtle)

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.turtle_list[-1].position())

    def move(self):
        for segment in range(len(self.turtle_list)-1 , 0 , -1):        
            new_x = self.turtle_list[segment-1].xcor()
            new_y = self.turtle_list[segment-1].ycor()
            self.turtle_list[segment].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)
        
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:    
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
