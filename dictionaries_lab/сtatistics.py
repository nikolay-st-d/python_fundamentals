stock = {}

while True:
    data = input()

    if data == 'statistics':
        break

    key, value = data.split(':')
    value = int(value)
    if key in stock:
        stock[key] += value
    else:
        stock[key] = value

print("Products in stock:")
for key, value in stock.items():
    print(f'- {key}: {value}')
print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")