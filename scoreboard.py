from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:  {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(f"{self.score}")

        self.score = 0
        self.update_score()

    def rescore(self):
        self.score += 1
        self.clear()
        self.update_score()
