import re

furniture = []
total_price = 0
while True:
    data = input()
    if data == 'Purchase':
        break
    regex = r'>>([A-Za-z\_]+)<<([0-9]+[\.0-9]*)!([0-9]+)'
    match = re.search(regex, data)
    if match:
        name, price, quantity = match.groups()
        furniture.append(name)
        total_price += float(price) * int(quantity)
print('Bought furniture:')
for element in furniture:
    print(element)
print(f'Total money spend: {total_price:.2f}')