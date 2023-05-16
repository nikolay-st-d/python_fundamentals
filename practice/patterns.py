num = int(input())

for i in range(1, num + 1):
    for star in range(i):
        print('*', end='')
    print()
for i in range(num - 1, 0, -1):
    for star in range(i):
        print('*', end='')
    print()