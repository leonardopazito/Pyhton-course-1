from turtle import Turtle

STARTING_POSITION = [[0, 0], [-20, 0], [-40, 0]]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments: list[Turtle] = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position: list[int] | list[float]):
        """Add a piece to the snake"""
        snake_piece = Turtle(shape="square")
        snake_piece.goto(*position)
        snake_piece.penup()
        snake_piece.color("white")
        self.segments.append(snake_piece)

    def create_snake(self):
        """Creates a snake of length 3. Each element of the snake is a Turtle
        object"""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        """Move snake continuously"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg_num - 1].pos()
            self.segments[seg_num].goto(*new_pos)
        self.head.forward(MOVE_DISTANCE)
        self.boundary()

    def extend(self):
        """Add a new segment to the snake"""
        position_to_add = [self.segments[-1].xcor(), self.segments[-1].ycor()]
        self.add_segment(position_to_add)

    def boundary(self):
        """Connect end points of the screen"""
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