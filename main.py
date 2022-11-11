import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle crossing game")
screen.setup(width=600, height=600)
screen.tracer(0)

loop_count = 0
game_is_on = True
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)

while game_is_on:
    time.sleep(0.1)
    cars.move()
    if loop_count % cars.generate_density == 0:
        cars.create_car()
    if player.at_finish():
        player.finish_return()
        cars.increase_speed()
        scoreboard.increase_score()
    for i in cars.car_list:
        if player.distance(i) < 20 and player.ycor() >i.ycor() or player.distance(i) < 25 and player.ycor() < i.ycor():
            scoreboard.game_over()
            game_is_on = False
    loop_count += 1
    screen.update()
screen.exitonclick()