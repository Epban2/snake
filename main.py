from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)
# se spengo il tracer, ogni volta che si vuole visualizzare lo schermo aggiornato, bisogna fare uno screen update

snake = Snake()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
food = Food()
scoreboard=Scoreboard()
while game_is_on and not snake.check_collision():  # not check_collision perche' di base ritorna false
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.random_location() #se viene colpito riposiziona sullo schermo
        snake.extend()  # aggiunge un segmento in coda
        scoreboard.increase_score()

    snake.move()
    game_is_on = snake.check_inside_screen()

scoreboard.game_over()
screen.update()
screen.exitonclick()
