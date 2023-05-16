i = 1
while i > 0:
    num = float(input())
    if num >= 0:
        print(f'Result: {num * 2:.2f}')
    else:
        print('Negative number!')
        break
    i += 1
