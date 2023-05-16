n = int(input())

for num in range(1111, 10000):
    num_to_str = str(num)

    special = True

    for j in range(4):
        digit = int(num_to_str[j])
        if digit == 0:
            special = False
            continue
        if n % digit != 0:
            special = False

    if special:
        print(num, end=' ')
