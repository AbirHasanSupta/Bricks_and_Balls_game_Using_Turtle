from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce_x(self):
        self.x_move *= -1

    def ball_bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.ball_bounce_y()
        self.goto(0, 0)
        self.move_speed = 0.05


