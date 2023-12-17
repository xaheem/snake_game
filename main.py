from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
from boundry import Boundry

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("My Snake Game.")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
boundry = Boundry()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
scoreboard.update_score()

game_is_on = True
while game_is_on:
    boundry.boundry()
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food and increase score
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        scoreboard.write("You hit the wall", align="center", font=("Courier", 15, "normal"))

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            scoreboard.write("You bit yourself", align="center", font=("Courier", 15, "normal"))


screen.exitonclick()
