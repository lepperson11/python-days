from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(( 350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="o", fun=r_paddle.up)
screen.onkey(key="l", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()
        ball.ball_speed()
        
        

    if ball.xcor() > 400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
        
        
        
    
    if ball.xcor() < -400:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()
        

screen.exitonclick()