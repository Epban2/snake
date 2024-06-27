import random
from turtle import Turtle

BORDO = 280


class Food(Turtle):  # ereditato tutti gli attributi e metodi di Turtle()
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.random_location()

    def random_location(self):
        xcor = random.randint(-BORDO, BORDO)  # 280 perché 300 è al bordo e troppo difficile da prendere
        ycor = random.randint(-BORDO, BORDO)
        self.goto(xcor, ycor)
