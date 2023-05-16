def is_even(num):
    if num % 2 == 0:
        return True
    return False


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


top_100 = int(input())
top_10 = int(input())
top_1 = int(input())

for a in range(1, top_100 + 1):
    for b in range(1, top_10 + 1):
        for c in range(1, top_1 + 1):
            if is_even(a) and is_prime(b) and 2 <= b <= 7 and is_even(c):
                print(f'{a} {b} {c}')
