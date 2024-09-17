from turtle import Turtle
import pathlib

FONT = ("Courier", 24, "normal")
DATA_PATH = pathlib.Path(__file__).parent / 'data.txt'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open(DATA_PATH) as score_data:
            high_level = int(score_data.read())
        self.level = 1
        self.high_level = high_level
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} High level: {self.high_level}",
                   align="left", font=FONT)

    def increase_high_level(self):
        if self.level > self.high_level:
            self.high_level = self.level
            with open(DATA_PATH, mode="w") as score_data:
                score_data.write(str(self.high_level))

    def increase_level(self):
        self.level += 1
        self.increase_high_level()
        self.update_scoreboard()

    def reset_(self):
        self.increase_high_level()
        self.level = 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=FONT)
