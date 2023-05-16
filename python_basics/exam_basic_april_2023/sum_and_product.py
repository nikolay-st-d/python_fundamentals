n = int(input())

found = False

for a in range(1, 10):
    if found:
        break
    for b in range(9, a, -1):
        if found:
            break
        for c in range(9):
            if found:
                break
            for d in range(9, c, -1):
                if (a + b + c + d) == (a * b * c * d) and n % 10 == 5:
                    found = True
                    print(f'{a}{b}{c}{d}')
                    break
                if int((a * b * c * d) / (a + b + c + d)) == 3 and n % 3 == 0:
                    found = True
                    print(f'{d}{c}{b}{a}')
                    break

if not found:
    print('Nothing found')