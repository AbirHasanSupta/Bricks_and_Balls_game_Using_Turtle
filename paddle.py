from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('black')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.goto(0, -220)

    def move_right(self):
        new_x = self.xcor() + 17
        if self.xcor() >= 385:
            new_x = 385
        self.goto(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - 17
        if self.xcor() <= -389:
            new_x = -389
        self.goto(new_x, self.ycor())
