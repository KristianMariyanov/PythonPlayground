monday = [400, 250, 105, 402, 205, 500, 400]
tuesday = [290, 210, 320, 520, 405, 300, 195]

points = [monday, tuesday]

for tup in zip(*points):
    print(tup)
