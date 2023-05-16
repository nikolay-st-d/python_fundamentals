size = input()  # "Large", "Medium" или "Small"
color = input()  # "Red", "Green" или "Yellow"
lots = int(input())
price = 0

if size == 'Large':
    if color == 'Red':
        price = 16
    elif color == 'Green':
        price = 12
    elif color == 'Yellow':
        price = 9
elif size == 'Medium':
    if color == 'Red':
        price = 13
    elif color == 'Green':
        price = 9
    elif color == 'Yellow':
        price = 7
elif size == 'Small':
    if color == 'Red':
        price = 9
    elif color == 'Green':
        price = 8
    elif color == 'Yellow':
        price = 5

income = price * lots
profit = income * 0.65

print(f'{profit:.2f} leva.')
