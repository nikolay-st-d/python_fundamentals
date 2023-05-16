n = int(input())

for num in range(1, n + 1):
    summ = 0
    special = False
    num_to_str = str(num)
    for i in range(len(num_to_str)):
        j = num_to_str[i]
        summ += int(j)
    if summ == 5 or summ == 7 or summ == 11:
        special = True
    print(f'{num} -> {special}')