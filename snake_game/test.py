from turtle import Screen, Turtle, Screen
import time
from snake import Snake
'''
#  set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("Snakety Snake Game")
screen.listen()
screen.tracer(0)


#  initialise starting variables
snake = Snake(length=5)
game_on = True


#  main code
while game_on:
    screen.update()  # updates animation after all segments have moved one step
    time.sleep(.1)  # slows animation down by putting time delay after update

    snake.move()


screen.exitonclick()

'''
screen = Screen()
tim = Turtle()
print(tim.pos())
tim.write("arg", move=False, align='left', font=('Arial', 8, 'normal'))

for i in range(1,7):
    print(i)





screen.exitonclick()