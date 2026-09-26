import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#E5EAEE")
screen.title("Lá cờ Nga")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()


def draw_rectangle(x, y, width, height, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.color(color)
    pen.pendown()

    pen.begin_fill()
    for length in (width, height, width, height):
        pen.forward(length)
        pen.left(90)
    pen.end_fill()


x, y = -300, -200
width, height = 600, 400
stripe = height / 3


draw_rectangle(x + 10, y - 10, width, height, "#B9C3CB")

draw_rectangle(x, y, width, stripe, "#D52B1E")
draw_rectangle(x, y + stripe, width, stripe, "#0039A6")
draw_rectangle(x, y + 2 * stripe, width, stripe, "white")

turtle.done()
