import turtle

a = turtle.speed(0)
b = turtle.Screen()

def star(size,color):
    turtle.fillcolor(color)
    turtle.begin_fill()

    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

star(350,"olive")
b.exitonclick()