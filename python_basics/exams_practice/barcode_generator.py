def even(n):
    if n % 2 == 0:
        return True
    return False


num_1 = input()  # 4-digit number
num_2 = input()  # 4-digit number

for a in range(int(num_1[0]), int(num_2[0]) + 1):
    for b in range(int(num_1[1]), int(num_2[1]) + 1):
        for c in range(int(num_1[2]), int(num_2[2]) + 1):
            for d in range(int(num_1[3]), int(num_2[3]) + 1):
                if not even(a) and not even(b) and not even(c) and not even(d):
                    print(f'{a}{b}{c}{d}', end=' ')
