m = int(input())  # 4 ... 144

password = ''
counter = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a < b and c > d) and (a * b + c * d == m):
                    print(f'{a}{b}{c}{d}', end=' ')
                    counter += 1
                    if counter == 4:
                        password = str(a) + str(b) + str(c) + str(d)
if password != '':
    print()
    print(f'Password: {password}')
else:
    print()
    print('No!')
