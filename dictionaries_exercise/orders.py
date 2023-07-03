products = {}
while True:
    data = input().split()
    if data[0] == 'buy':
        break
    product, price, quantity = data[0], float(data[1]), int(data[2])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][0] = price
        products[product][1] += quantity
for product, data in products.items():
    total_price = data[0] * data[1]
    print(f"{product} -> {total_price:.2f}")