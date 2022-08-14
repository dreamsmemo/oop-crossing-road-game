from turtle import Turtle

START_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.left(90)
        self.reset()

    def move_up(self):
        moved_up_ycor = self.ycor() + MOVE_DISTANCE
        self.goto(0, moved_up_ycor)

    def reset(self):
        self.goto(START_POSITION)

    def success(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False