import turtle

turtle.bgcolor('yellow')

screen = turtle.Screen();

pen = turtle.Turtle()
pen.pensize(10)
pen.color('green')

pen.up()
pen.setposition(-100, 100)
pen.down()
pen.circle(50)
pen.up()
pen.setposition(100, 100)
pen.down()
pen.circle(50)
pen.up()
pen.setposition(-200, 0)
pen.down()
pen.right(90)
for _ in range(180):
    pen.forward(3.5)
    pen.left(1)

screen.exitonclick()
