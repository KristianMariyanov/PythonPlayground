from random import randint as rand


def roll_dice():
    print('Please enter number of dice sides:')
    n = int(input())
    sum = 0
    print('Your first number is:')
    first_number = rand(1, n)
    sum += first_number
    print(first_number)
    print('Your second number is:')
    second_number = rand(1, n)
    sum += second_number
    print(second_number)
    print('Your third number is:')
    third_number = rand(1, n)
    sum += third_number
    print(third_number)
    print('Sum of all dice trows is:')
    print(sum)


if __name__ == '__main__':
    roll_dice()
