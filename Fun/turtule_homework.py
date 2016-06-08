__author__ = 'dmytrol'
from turtle import Screen, Turtle
import math
import random

screen = Screen()
screen.bgcolor(0.9, 0.9, 0.5)

jack = Turtle()
jack.shape("turtle")


def draw_triangle(k):
    jack.color(random.random(), random.random(), random.random())
    h = math.sqrt(k * k + k * k)
    jack.begin_fill()
    jack.right(45)
    jack.forward(h)
    jack.right(135)
    jack.forward(k * 2)
    jack.right(135)
    jack.forward(h)
    jack.penup()
    jack.goto(0, 0)
    jack.right(45)
    jack.end_fill()
    screen.listen()


def draw_pine_tree():
    d = int(screen.textinput("Attention, please!",
                             "Enter the size of smallest branch of a pine-tree (in px from 10 till 100)"))
    draw_triangle(d)

    jack.right(90)
    jack.forward(d - d / 3)
    jack.left(90)
    draw_triangle(d * 2)

    jack.right(90)
    jack.forward(d * 2 - d / 3)
    jack.left(90)
    draw_triangle(d * 3)


def go_forward():
    jack.forward(10)


def go_backward():
    jack.backward(10)


def go_left():
    jack.left(90)


def go_right():
    jack.right(90)

screen.onkey(draw_pine_tree, "p")
screen.onkey(go_forward, "Up")
screen.onkey(go_backward, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

screen.listen()
screen.mainloop()