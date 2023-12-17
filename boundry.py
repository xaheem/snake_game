from turtle import Turtle
class Boundry(Turtle):

    def __init__(self):
        super().__init__()

    def boundry(self):
        self.pensize(20)
        self.color("white")
        self.penup()
        self.goto(-290, -290)
        self.pendown()
        for i in range(4):
            self.forward(580)
            self.left(90)
        self.hideturtle()
