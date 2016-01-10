import turtle

side_height = int(input('Enter size of side: '))

screen = turtle.Screen()

turtle.color('red')
for _ in range(4):
    turtle.forward(side_height)
    turtle.left(90)

screen.exitonclick()
