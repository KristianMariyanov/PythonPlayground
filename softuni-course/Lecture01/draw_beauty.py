import turtle

turtle.speed('fastest')
screen = turtle.Screen();

i = 10
for _ in range(750):
    turtle.left(i % 48)
    turtle.forward(10)
    i += 1

turtle.up()
turtle.setposition(0, 100)
turtle.down()
turtle.left(110)
turtle.forward(200)

screen.exitonclick()


