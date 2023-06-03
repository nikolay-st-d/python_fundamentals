def order_calculator(product, quantity):
    result = 0
    if product == 'coffee':
        result = quantity * 1.5
    elif product == 'coke':
        result = quantity * 1.4
    elif product == 'snacks':
        result = quantity * 2
    elif product == 'water':
        result = quantity
    return result


product_order = input()
product_qty = int(input())

print(f'{order_calculator(product_order, product_qty):.2f}')
