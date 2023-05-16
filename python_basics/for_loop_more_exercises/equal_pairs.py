n = int(input())

num = 0
prev_num = 0
max_diff = 0

for i in range(n):
    a = int(input())
    b = int(input())
    num = a + b
    if i == 0:
        prev_num = num
    if num > prev_num or num < prev_num:
        diff = abs(num - prev_num)
        if diff > max_diff:
            max_diff = diff
        prev_num = num
    else:
        prev_num = num

if max_diff == 0:
    print(f'Yes, value={num}')
else:
    print(f'No, maxdiff={max_diff}')