import turtle

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("#E5EAEE")
screen.title("Lá cờ Nhật Bản")

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


draw_rectangle(-290, -210, 600, 400, "#B9C3CB")


draw_rectangle(-300, -200, 600, 400, "white")


pen.penup()
pen.goto(0, -120)
pen.setheading(0)
pen.pencolor("#BC002D")
pen.fillcolor("#BC002D")
pen.pendown()

pen.begin_fill()
pen.circle(120)
pen.end_fill()

turtle.done()
