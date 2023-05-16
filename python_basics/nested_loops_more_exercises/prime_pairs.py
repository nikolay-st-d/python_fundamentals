def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


start_first = int(input())
start_second = int(input())
x = int(input())
y = int(input())

for a in range(start_first, start_first + x + 1):
    for b in range(start_second, start_second + y + 1):
        if prime(a) and prime(b):
            print(a, end='')
            print(b, end=' ')
            print()
