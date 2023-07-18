import re
income = 0
while True:
    data = input()
    if data == 'end of shift':
        break
    regex = r'%([A-Z]{1}[a-z]+)%.*<(\w+)>.*\|([0-9]+)\|\D*([0-9]+[\.0-9]*)\$'
    match = re.search(regex, data)
    if match:
        name, product, qty, price = match.groups()
        total_price = int(qty) * float(price)
        print(f"{name}: {product} - {total_price:.2f}")
        income += total_price
print(f"Total income: {income:.2f}")