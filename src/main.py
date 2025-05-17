import turtle as t
from itertools import cycle

colors_list = [(235, 234, 231), (236, 35, 108), (221, 231, 237), (145, 28, 66), (239, 75, 35), (7, 148, 95), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0),
               (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (163, 211, 178)]

t.colormode(255)
screen = t.Screen()
screen.setup(width=800, height=600)  # você pode ajustar o tamanho da tela
tim = t.Turtle()
tim.penup()  # não desenha enquanto se move
tim.goto(-screen.window_width() // 2 + 170, -screen.window_height() // 2 + 50)
tim.hideturtle()
tim.pendown()  # começa a desenhar

def forward():
    tim.penup()
    tim.forward(50)
    tim.pendown()

color_iterator = cycle(colors_list)

def dot_color():
    return next(color_iterator)
row = 0

while row <= 8:
    for i in range(10):
        if i < 9:
            tim.dot(20, dot_color())
            forward()
        else:
            tim.dot(20, dot_color())
            tim.left(90)
            forward()
            tim.left(90)

    for i in range(10):
        if i < 9:
            tim.dot(20, dot_color())
            forward()
        else:
            tim.dot(20, dot_color())
            tim.right(90)
            forward()
            tim.right(90)

    row += 2



screen.exitonclick()