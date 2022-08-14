from turtle import Turtle
import random

COLORS = ["orange", "yellow", "light green", "olive drab", "light blue", "purple", "light pink", "turquoise"]
STARTING_MOVE_DISTANCE = 10
START_POSITION = (200, 0)
MOVE_INCREMENT = 7

class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_xcor = random.randint(50, 250)
            random_ycor = random.randint(-250, 250)
            new_car.goto(random_xcor, random_ycor)
            self.all_cars.append(new_car)

    def car_moving(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT