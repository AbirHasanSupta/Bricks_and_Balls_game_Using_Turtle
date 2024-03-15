from turtle import Turtle
import random
colors = ['#0B4718', 'blue', 'black', '#6B0F1A', '#400A29', '#9A8301', '#BB3500']


class Bricks:
    def __init__(self):
        self.all_bricks = []

    def create_bricks(self, positions):
        for i in range(50):
            new_brick = Turtle()
            new_brick.shape('square')
            new_brick.shapesize(stretch_wid=0.9, stretch_len=2)
            new_brick.color(random.choice(colors))
            new_brick.penup()
            new_brick.goto(positions[i])
            self.all_bricks.append(new_brick)

    def remove_brick(self, brick):
        brick.hideturtle()
        self.all_bricks.remove(brick)

