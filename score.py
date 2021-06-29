from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_scorefile.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=0, y=272)
        self.create_score()
        self.hideturtle()

    def create_score(self):
        self.clear()
        self.write(arg=f"Score:{self.score} Highest score : {self.highest_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.create_score()

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_scorefile.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.create_score()
