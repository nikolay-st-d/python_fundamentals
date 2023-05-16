from sys import maxsize

n = int(input())
max_num = -maxsize
min_num = maxsize
for _ in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
