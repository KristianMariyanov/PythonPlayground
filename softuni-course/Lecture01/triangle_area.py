import math

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

perimeter = a + b + c
halfP = perimeter / 2

area = math.sqrt(halfP * (halfP - a) * (halfP - b) * (halfP - c))

print('The area of the triangle with sides: \na = {}\nb = {}\nc = {} \nis {}'.format(a, b, c, round(area, 2)))
