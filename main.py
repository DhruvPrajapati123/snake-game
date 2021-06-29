from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)
x_list = [0, -20, -40]

# for turtle in range(0, 3):
#     new_segment = Turtle()
#     new_segment.shape("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(x=x_list[turtle], y=0)
#     segments.append(new_segment)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect the collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.segments[0].xcor() > 285 or snake.segments[0].xcor() < -285 or snake.segments[0].ycor() > 285 or \
            snake.segments[0].ycor() < -285:
        # is_game_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    # detect collision with head to any other segment in tail
    # for segment in snake.segments:
    #     if segment == snake.segments[0]:
    #         pass
    #     elif snake.segments[0].distance(segment) < 10:
    #         is_game_on = False
    #         score.game_over()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset()
            snake.reset()
screen.exitonclick()
