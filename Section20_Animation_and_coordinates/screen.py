from turtle import Screen


class MyScreen():
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("My Snake Game")
        self.screen.tracer(0)
        self.screen.listen()

    def onkeyfunction(self, fun1_up, fun2_down, fun3_left,
                      fun4_right):
        self.screen.onkey(fun1_up, "Up")
        self.screen.onkey(fun2_down, "Down")
        self.screen.onkey(fun3_left, "Left")
        self.screen.onkey(fun4_right, "Right")


teste = MyScreen()
