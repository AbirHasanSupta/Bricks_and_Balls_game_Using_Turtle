from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(0, 245)
        self.write(f'Score:{self.score}', align='center', font=('Courier', 30, ' bold'))

    def update_score(self):
        self.clear()
        self.goto(0, 245)
        self.write(f'Score:{self.score}', align='center', font=('Courier', 30, ' bold'))

    def point(self):
        self.score += 1
        self.update_score()
