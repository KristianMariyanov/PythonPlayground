input_string = input('Enter string: ')
symbol = input('Enter symbol: ')

position = input_string.find(symbol)

if position is -1:
    print('The symbol "{}" not exist in the string "{}"'.format(symbol, input_string))
    print(input_string)
else:
    starting_index = position + len(symbol) + 1
    print(input_string[starting_index:])
