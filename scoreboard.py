from turtle import Turtle
import os

FONT = ("courier", 24, "normal")
ALIGN = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.high_score = 0

        if not os.path.isfile("scores.txt"):  # se non c'è il file lo crea e scrive zero
            with open("scores.txt", "w") as file:
                file.write("0")
        try:
            with open("scores.txt", "r") as file:
                hs = file.read()
                self.high_score = int(hs) if hs else 0
        except Exception as error:
            pass
        
        self.penup()
        self.goto(0, 255)
        self.score = 0
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.home()
        if self.score > self.high_score:
            self.high_score = self.score
            with (open("scores.txt", "w")) as file:  # con with open non devo fare il file.close e gestisce gli errori
                file.write(str(self.high_score))
        self.write(f"GAME OVER\nHighscore: {self.high_score}", align=ALIGN, font=("courier", 30, "normal"))
