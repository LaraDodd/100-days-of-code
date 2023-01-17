from turtle import Turtle, Screen

#set up screen
screen = Screen()
screen.setup(height=600, width=800)
screen.title("PING PONG Game")
screen.listen()
screen.tracer(0)


line = Turtle()
line.penup()
line.setpos(0,300)
line.pensize(20)
line.color("white")
line.setheading(270)
line.forward(50)
print(line.xcor())

#create line
line = Turtle()
line.penup()
line.setpos(0,500/2)
line.pensize(10)
line.color("white")
line.setheading(270)

while line.ycor() >= -500/2:
    line.forward(10)
    line.pendown()
    line.forward(10)
    line.penup()


screen.exitonclick()
