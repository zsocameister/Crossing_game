from turtle import Turtle
from random import choice

STARTING_POSITIONS_Y = [i for i in range(-240, 241, 20)]
STARTING_POSITIONS_X = [i for i in range(-240, 301, 20)]
XSTART_WHILEGAMEON = 290
STARTING_GENERATE_AMOUNT = 20
CAR_GENERATE_DENSITY = 6
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.game_begin()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.generate_density = CAR_GENERATE_DENSITY
        self.times_increased = 0

    def create_car(self, starting_x=300):
        new_car = Turtle(shape="square")
        new_car.penup()
        new_car.setheading(180)
        new_car.color(choice(COLORS))
        new_car.shapesize(stretch_len=2)
        new_car.goto(x=starting_x, y=choice(STARTING_POSITIONS_Y))
        self.car_list.append(new_car)

    def game_begin(self):
        for i in range(STARTING_GENERATE_AMOUNT):
            self.create_car(choice(STARTING_POSITIONS_X))

    def move(self):
        for i in self.car_list:
            if i.xcor() > -350:
                i.forward(self.move_speed)
            else:
                self.remove_car(i)

    def remove_car(self, car_in_list):
        self.car_list.remove(car_in_list)
        car_in_list.hideturtle()

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
        self.times_increased += 1
        self.cargenerator_density_adder()

    def cargenerator_density_adder(self):
        if self.times_increased == 1 or self.times_increased == 2 or self.times_increased == 3\
                or self.times_increased == 5 or self.times_increased == 7:
           self.generate_density -= 1
