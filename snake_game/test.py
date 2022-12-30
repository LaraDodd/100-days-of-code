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
'''screen = Screen()
tim = Turtle()
print(tim.pos())
tim.write("arg", move=False, align='left', font=('Arial', 8, 'normal'))

for i in range(1,7):
    print(i)





screen.exitonclick()'''

with open("score_data", "r") as scores:
    highscores = []
    for line in scores:
        highscores.append(line)

highscores = highscores[1:]  # slice first line off
print(highscores)

# edits the list in place, otherwise you would have to go through every value in highscores
# and strip it and then int() it and THEN append it to a new list
formatted_highscores = [int(s.strip('\n')) for s in highscores]  # list comprehension

print(highscores)
print(formatted_highscores)
