import turtle


def draw_square(brad):
    for i in range(4):
        brad.forward(100)
        brad.right(90)


def draw_circle(angel):
    angel.color('blue')
    angel.circle(100)


def draw_triangle(triangle):
    for i in range(3):
        triangle.forward(100)
        triangle.right(120)


def draw_art():
    brad = turtle.Turtle()
    brad.color('yellow')
    for i in range(40):
        draw_square(brad)
        brad.right(10)


def main():
    window = turtle.Screen()
    window.bgcolor('red')
    tri = turtle.Turtle()
    tri.color('blue')
    for i in range(50):
        draw_triangle(tri)
        tri.right(10)
    # draw_art()
    # brad = turtle.Turtle()
    # draw_square(brad)
    # angel = turtle.Turtle()
    # draw_circle(angel)
    # tri = turtle.Turtle()
    # draw_triangle(tri)

    window.exitonclick()


if __name__ == '__main__':
    main()
