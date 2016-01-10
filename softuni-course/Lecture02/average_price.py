# prices = []
# while True:
#     price = input('Enter price: ')
#     if price == 'stop':
#         break
#     if price is not '':
#         prices.append(int(price))
#
# if len(prices) < 2:
#     print('Prices are not enough:')
# else:
#     avg = float(sum(prices)/len(prices))
#     print('{0:.2f}'.format(avg))

from decimal import *

prices = []
while True:
    price = input('Enter price: ')
    if price == 'stop' and len(prices) > 2:
        break
    elif price == 'stop' and len(prices) <= 2:
        print('Prices are not enough:')
        print('Please enter more prices')
        continue
    try:
        prices.append(Decimal(price))
    except InvalidOperation:
        print('This is not the valid number... Try again.')

new_list = []

[new_list.append(e) for e in prices  if e == min(prices) or max(prices)]

print(new_list)

avg = Decimal(sum(new_list)/len(new_list))
print('{0:.2f}'.format(avg))