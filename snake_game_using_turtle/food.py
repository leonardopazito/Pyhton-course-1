from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        """Create a food randomly"""
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Define the random position of food"""
        random_x_pos = random.randint(-280, 280)
        random_y_pos = random.randint(-280, 280)
        self.goto(random_x_pos, random_y_pos)
