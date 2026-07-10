from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",50,"normal")

class Scoreboard(Turtle):
    def __init__(self ,position):
        super().__init__()
        self.score=0
        self.color("green")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.write(f" {self.score}",align=ALIGNMENT,font=FONT)


    def increase_score(self):
        self.clear()
        self.score+=1
        self.update_scoreboard()
        