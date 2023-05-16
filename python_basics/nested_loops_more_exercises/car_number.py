def even(num):
    if num % 2 == 0:
        return True
    return False


num_1 = int(input())
num_2 = int(input())

for a in range(num_1, num_2 + 1):
    for b in range(num_1, num_2 + 1):
        for c in range(num_1, num_2 + 1):
            for d in range(num_1, num_2 + 1):
                if (even(a) and not even(d)) or (not even(a) and even(d)):
                    if a > d and even(b + c):
                        print(f'{a}{b}{c}{d}', end=' ')