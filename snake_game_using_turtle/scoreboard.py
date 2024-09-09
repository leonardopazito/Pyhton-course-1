from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=FONT)

    def increase_score(self) -> None:
        "Increase the scorebord in 1 unit"
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self) -> None:
        "Change the scoreboard to a message that says 'Game Over'"
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
