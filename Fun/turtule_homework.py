__author__ = 'dmytrol'
from turtle import Screen, Turtle
import math

screen = Screen()
screen.bgcolor(0.9, 0.9, 0.5)

jack = Turtle()

jack.color("red")
jack.shape("turtle")


def draw_triangle(k):
    h = math.sqrt(k * k + k * k)
    jack.begin_fill()
    jack.right(45)
    jack.forward(h)
    jack.right(135)
    jack.forward(k * 2)
    jack.right(135)
    jack.forward(h)
    jack.goto(0, 0)
    jack.right(45)
    jack.end_fill()


def draw_pine_tree():
    d = int(screen.textinput("Dima", "Enter the size of smallest branch of a pine-tree"))

    draw_triangle(50)

    jack.right(90)
    jack.forward(30)
    jack.left(90)
    draw_triangle(100)

    jack.right(90)
    jack.forward(80)
    jack.left(90)
    draw_triangle(150)

screen.onkey(draw_pine_tree, "p")
# screen.onkey(go_forward, "Up")
# screen.onkey(go_backward, "Down")
# screen.onkey(go_left, "Left")
# screen.onkey(go_right, "Right")

screen.listen()

screen.mainloop()