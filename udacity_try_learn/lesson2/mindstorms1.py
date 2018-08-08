import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_triangle(some_turtle):
    for i in range(3):
        some_turtle.forward(100)
        some_turtle.left(120)

def draw_circle(some_turtle, radius):
    some_turtle.shape("arrow")
    some_turtle.color("blue")
    some_turtle.circle(radius)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.speed(10)
    brad.shape("turtle")
    brad.color("blue")
    brad.sety(200)

    for i in range(60):
        draw_triangle(brad)
        brad.right(6)

    window.exitonclick()


draw_art()
