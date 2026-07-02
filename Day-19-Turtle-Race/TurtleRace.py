from turtle import Turtle,Screen
import random

# tim1= Turtle(shape='turtle')
# tim2= Turtle(shape='turtle')
# tim3= Turtle(shape='turtle')
# tim4= Turtle(shape='turtle')
# tim5= Turtle(shape='turtle')
# tim6= Turtle(shape='turtle')

# tim1.color("red")
# tim2.color("yellow")
# tim3.color("green")
# tim4.color("pink")
# tim5.color("blue")
# tim6.color("orange")

screen = Screen()
screen.setup(width=500 , height=400)
user_input = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter a color: ")
print (user_input)

# tim1.penup()
# tim2.penup()
# tim3.penup()
# tim4.penup()
# tim5.penup()
# tim6.penup()

# tim1.goto(x=-230,y=125)
# tim2.goto(x=-230,y=75)
# tim3.goto(x=-230,y=25)
# tim4.goto(x=-230,y=-25)
# tim5.goto(x=-230,y=-75)
# tim6.goto(x=-230,y=-125)

game_start=False

all_turtles= []
y_positions = [-125 , -75 , -25 ,25 ,75 , 125]
colors=["red" , "pink", "orange" , "green" ,"yellow" , "blue"]
for i in range(6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230 , y = y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_input:
    game_start=True

while game_start:
    for i in all_turtles:

        if i.xcor() > 230 :
            winning_color = i.pencolor()
            if winning_color == user_input:
                print(f"Yeah! your {winning_color} turtle won the race.")
            else:
                print(f"You lose! {winning_color} turtle won the race. ")
            game_start=False

        distance= random.randint(0,10)
        i.fd(distance)
        


screen.exitonclick()

