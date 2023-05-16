pcs = int(input())
j_type = input()
delivery_option = input()

total = 0

if pcs < 10:
    print('Invalid order')
else:
    if j_type == '90X130':
        price = 110
        total = pcs * price
        if pcs > 30:
            total = pcs * price * 0.95
        if pcs > 60:
            total = pcs * price * 0.92
    elif j_type == '100X150':
        price = 140
        total = pcs * price
        if pcs > 40:
            total = pcs * price * 0.94
        if pcs > 80:
            total = pcs * price * 0.9
    elif j_type == '130X180':
        price = 190
        total = pcs * price
        if pcs > 20:
            total = pcs * price * 0.93
        if pcs > 50:
            total = pcs * price * 0.88
    elif j_type == '200X300':
        price = 250
        total = pcs * price
        if pcs > 25:
            total = pcs * price * 0.91
        if pcs > 50:
            total = pcs * price * 0.86

    if delivery_option == 'With delivery':
        total += 60

    if pcs > 99:
        total *= 0.96

    print(f'{total:.2f} BGN')
