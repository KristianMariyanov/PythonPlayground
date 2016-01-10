import turtle

side = 20
turtle.speed('fastest')

size = int(input())

for row in range(size):
    for col in range(size):
        if (col % 2 == 1 and row % 2 == 0) or (col % 2 == 0 and row % 2 == 1):
            turtle.begin_fill()

        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

        turtle.end_fill()
        turtle.forward(side)

    turtle.up()
    turtle.goto(0, row*20 + 20)
    turtle.down()

turtle.exitonclick()

