from turtle import Turtle


class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.goto(-340, 250)
        self.hideturtle()
        self.life_count = 3
        self.write(f'Life:0{self.life_count}', align='center', font=('Courier', 20, 'bold'))

    def life_update(self):
        self.clear()
        self.write(f'Life:0{self.life_count}', align='center', font=('Courier', 20, 'bold'))

    def life_reduce(self):
        self.life_count -= 1
        self.life_update()
