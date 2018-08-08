import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(some_turtle, radius):
    some_turtle.shape("arrow")
    some_turtle.color("blue")
    some_turtle.circle(radius)

def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.home()
    brad.speed(10)
    brad.shape("turtle")
    brad.color("yellow")

    for i in range(60):
        draw_square(brad)
        brad.right(6)

    window.exitonclick()


draw_art()
