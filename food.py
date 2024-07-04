from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """ Randomly assigns a new location for the food """
        pos_x = random.randint(-14, 14)
        pos_y = random.randint(-14, 14)
        self.goto((pos_x*20, pos_y*20))
