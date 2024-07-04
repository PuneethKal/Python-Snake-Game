from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.ht()
        self.write_score()

    def write_score(self):
        """Writes score to screen"""
        self.clear()
        self.write(arg=f"Score = {self.score}", align="center", font=("Times New Roman", 15, "bold"))

    def update_score(self):
        """Increment score by 1 """
        self.score += 1
        self.write_score()

    def game_over(self):
        """Writes Gave Over to screen"""
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Times New Roman", 15, "bold"))
