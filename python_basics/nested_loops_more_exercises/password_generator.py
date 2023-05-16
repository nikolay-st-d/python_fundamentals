n = int(input())
l = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(ord('a'), ord('a') + l):
            for d in range(ord('a'), ord('a') + l):
                for e in range(1, n + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{chr(c)}{chr(d)}{e}', end=' ')