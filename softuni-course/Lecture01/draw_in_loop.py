import turtle

side_size = int(input('Enter size of side:'))
angle = int(input('Enter angle:'))

screen = turtle.Screen()
turtle.color('red')

while True:
    turtle.forward(side_size)
    turtle.left(angle)