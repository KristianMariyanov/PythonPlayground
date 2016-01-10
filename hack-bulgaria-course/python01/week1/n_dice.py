from random import randint as rand


def roll_dice():
    print('Please enter number of dice sides:')
    n = int(input())
    print('Your random number is:')
    print(rand(1, n))


if __name__ == '__main__':
    roll_dice()
