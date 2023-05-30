# import colorgram

# # Uses a Hirst original dot painting to find the rgb colors then I extracted the meaningful colors
## and pasted in rgb_list

# colors = colorgram.extract('image.jpg', 20)
# colors_list = []
#
# for x in colors:
#     r = x.rgb.r
#     b = x.rgb.g
#     g = x.rgb.b
#     new_rgb = (r, g, b)
#     colors_list.append(new_rgb)
# print(colors_list)

import random as rand
from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
screen.colormode(255)

rgb_list = [(28, 162, 107), (190, 82, 41), (232, 57, 161), (232, 90, 214), (220, 174, 138), (140, 59, 108),
            (107, 215, 193), (22, 130, 57), (200, 34, 165), (210, 94, 77), (235, 53, 89), (119, 144, 191),
            (13, 88, 151), (143, 225, 207), (106, 195, 108), (136, 70, 30)]


def paint_column():
    for num in range(0, 10):
        timmy.forward(50)
        timmy.pendown()
        timmy.dot(20, rand.choice(rgb_list))
        timmy.penup()
        timmy.setheading(90)


def change_column():
    timmy.forward(50)
    timmy.setheading(0)
    timmy.forward(50)
    timmy.setheading(270)
    for num in range(0, 9):
        timmy.forward(50)


timmy.penup()
timmy.speed(0)
timmy.setheading(180)
timmy.forward(250)
timmy.setheading(270)
timmy.forward(200)

for num in range(0, 10):
    paint_column()
    change_column()

timmy.hideturtle()

screen.exitonclick()
