import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen Set Up
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game!")
screen.tracer(0)
screen.bgcolor("black")


# Player Set Up
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

# Score Set Up
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.car_moving()

    # Detect the collsion between turtle and cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if player.success():
        player.reset()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()