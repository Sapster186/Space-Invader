import turtle


class TurtleMovements:
    def __init__(self):
        self.TT = turtle.Turtle()
        self.screen = self.TT.getscreen()
        self.alien = turtle.Turtle()
        self.boundaryxpos = 280
        self.boundaryxneg = -280
        self.boundaryypos = -120
        self.boundaryyneg = -280


    def change(self):
        self.TT.shape("images/space-invaders.gif")
        self.TT.shapesize(stretch_wid=1, stretch_len=1, outline=1)


    def Turtle(self):
        self.TT.penup()
        self.TT.goto(0,-200)
        self.screen.listen()
        self.screen.onkeypress(self.move_left,'Left')
        self.screen.onkeypress(self.move_right, 'Right')
        self.screen.onkeypress(self.move_up, 'Up')
        self.screen.onkeypress(self.move_down, "Down")

    def move_left(self):
        if self.TT.xcor() >= self.boundaryxneg:
            self.TT.backward(10)
        else:
            pass
    def move_right(self):
        if self.TT.xcor() < self.boundaryxpos:
            self.TT.forward(10)
        else:
            pass
    def move_up(self):
        if self.TT.ycor() < self.boundaryypos:
            self.TT.setheading(90)
            self.TT.forward(10)
            self.TT.setheading(360)
        else:
            pass


    def move_down(self):
        self.TT.setheading(90)
        self.TT.backward(10)
        self.TT.setheading(360)


    def GameScreen(self, Bgcolor):
        self.screen.bgcolor(Bgcolor)
        self.screen.register_shape("images/space-invaders.gif")
        self.change()
        self.Turtle()


        self.screen.mainloop()

    def enemy_aliens(self):
        self.screen.register_shape("images/alien-ship.gif")




