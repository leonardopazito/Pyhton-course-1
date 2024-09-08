from turtle import Turtle

STARTING_POSITION = [[0, 0], [-20, 0], [-40, 0]]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        """Create a snake of length 3"""
        self.snake_list: list[Turtle] = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        """Create a snake of length 3"""
        for position in STARTING_POSITION:
            snake_piece = Turtle(shape="square")
            snake_piece.goto(*position)
            snake_piece.penup()
            snake_piece.color("white")
            self.snake_list.append(snake_piece)

    def move(self):
        """Move the snake continuously"""
        for seg_num in range(len(self.snake_list) - 1, 0, -1):
            new_pos = self.snake_list[seg_num - 1].pos()
            self.snake_list[seg_num].goto(*new_pos)
        self.head.forward(MOVE_DISTANCE)
        self.boundary()

    def boundary(self):
        """Connect the end points of screen"""
        x_pos, y_pos = self.head.pos()
        if x_pos >= 300:
            self.head.goto(-300, y_pos)
        elif x_pos <= -300:
            self.head.goto(300, y_pos)
        elif y_pos <= -300:
            self.head.goto(x_pos, 300)
        elif y_pos >= 300:
            self.head.goto(x_pos, -300)

    def up(self):
        """Move the head up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the head down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the head left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Move the head right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
