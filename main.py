from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Score
from life import Life
import time


screen = Screen()
screen.bgcolor('skyblue')
screen.title('Brick n Balls')
screen.setup(width=850, height=600)

screen.tracer(0)
screen.listen()

score = Score()
life = Life()
ball = Ball()
line = Turtle()
bricks = Bricks()
paddle = Paddle()

screen.onkeypress(paddle.move_right, 'Right')
screen.onkeypress(paddle.move_left, 'Left')

line.shape('square')
line.shapesize(stretch_wid=1, stretch_len=43)
line.color('grey')
line.penup()
line.goto(0, 225)

bricks_positions = ([(x, 157) for x in range(-400, 400, 44)] +
                    [(x, 130) for x in range(-356, 356, 44)] +
                    [(x, 103) for x in range(-290, 290, 44)])
bricks.create_bricks(positions=bricks_positions)

screen_is_on = True
while screen_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.xcor() > 400 or ball.xcor() < -400:
        ball.ball_bounce_x()
    if ball.ycor() > 200:
        ball.ball_bounce_y()
    if ball.ycor() < -285:
        life.life_reduce()
        if life.life_count == 0:
            game_over = Turtle()
            game_over.hideturtle()
            game_over.penup()
            game_over.goto(0, -40)
            game_over.write('Game Over!!', align='center', font=('Courier', 70, 'bold'))
            screen_is_on = False
        time.sleep(0.5)
        ball.reset_position()
    if ball.distance(paddle) < 30 and ball.ycor() > -240:
        ball.ball_bounce_y()
    if bricks.all_bricks == []:
        game_over = Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.goto(0, -40)
        game_over.write("You've Won!!", align='center', font=('Courier', 70, 'bold'))
        screen_is_on = False

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 30:
            score.point()
            bricks.remove_brick(brick)
            ball.ball_bounce_y()
            ball.move_speed *= 0.9


screen.exitonclick()