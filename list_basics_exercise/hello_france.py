list_of_items = input().split('|')
budget = float(input())
profit = 0
sold_items_prices = []

for item in list_of_items:
    item_valid = False
    item_type, price = item.split('->')
    item_price = float(price)

    if item_type == 'Clothes' and item_price <= 50:
        item_valid = True
    elif item_type == 'Shoes' and item_price <= 35:
        item_valid = True
    elif item_type == 'Accessories' and item_price <= 20.50:
        item_valid = True

    if item_valid and budget >= item_price:
        budget -= item_price
        new_item_price = item_price * 1.4
        sold_items_prices.append(new_item_price)
        profit += item_price * 0.4

item_prices_as_chars = []
for current_char in sold_items_prices:
    print(f'{current_char:.2f}', end=' ')
#     current_char = str(current_char)
#     item_prices_as_chars.append(current_char)
# print(' '.join(item_prices_as_chars))
print()
print(f'Profit: {profit:.2f}')
if budget + sum(sold_items_prices) >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
