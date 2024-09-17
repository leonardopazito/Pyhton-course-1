from turtle import Turtle
import pathlib
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

DATA_PATH = pathlib.Path(__file__).parent / 'data.txt'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open(DATA_PATH) as score_data:
            high_score = int(score_data.read())
        self.score = 0
        self.high_score = high_score
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score} ",
                   align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_PATH, mode="w") as score_data:
                score_data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
