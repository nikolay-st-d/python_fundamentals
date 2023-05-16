import sys

n = int(input())

summ = 0
max_num = -sys.maxsize

for _ in range(n):
    num = int(input())
    summ += num
    if num > max_num:
        max_num = num

rest_num = summ - max_num
if max_num == rest_num:
    print('Yes')
    print(f'Sum = {summ - max_num}')
else:
    print('No')
    print(f'Diff = {abs(max_num - rest_num)}')