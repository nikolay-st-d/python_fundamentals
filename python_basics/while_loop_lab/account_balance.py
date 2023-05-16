balance = 0

while True:
    add = input()

    if add == 'NoMoreMoney':
        break

    num = float(add)

    if num >= 0:
        print(f'Increase: {num:.2f}')
        balance += num
    else:
        print(f'Invalid operation!')
        break

print(f'Total: {balance:.2f}')
