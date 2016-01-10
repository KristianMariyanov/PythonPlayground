full_name = input('Enter your name: ')

list_of_names = full_name.split()

for index, name in enumerate(list_of_names):
    if name[0].islower():
        del list_of_names[index]

[print(name[0] + '.', end='') for name in list_of_names]