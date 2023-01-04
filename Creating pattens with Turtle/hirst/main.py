import turtle
import random
import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)

def create_tuple(colour_rgb_object):
    return (colour_rgb_object[0], colour_rgb_object[1],colour_rgb_object[2])


colours = colorgram.extract("earthy.jpg", 30)
colour_tuple_list = []

for i in range(29):
    colour = colours[i]
    rgb_tuple = create_tuple(colour.rgb)
    colour_tuple_list.append(rgb_tuple)
#
# print(colour_tuple_list)

tim = Turtle()
tim.pensize(10)
tim.shape("classic")
tim.shapesize(.1,.1)
tim.penup()

# colour_tuple_list = [(229, 222, 210), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88),
#                      (207, 134, 157), (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152),
#                      (164, 80, 52), (200, 84, 111), (208, 225, 215), (143, 31, 40), (54, 167, 135),
#                      (232, 198, 110), (201, 219, 227), (229, 206, 214), (6, 109, 90), (41, 160, 185),
#                      (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199), (235, 169, 158),
#                      (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217)]

x = -225.0
y = -200.0

for y_step in range(10):
    tim.setpos(x,y)
    for x_step in range(10):
        tim.dot(20, random.choice(colour_tuple_list))
        tim.forward(50)
    y += 50.0
    print(x, y)



my_screen = Screen()
my_screen.exitonclick()
